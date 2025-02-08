from typing import Optional
import asyncio
import colorama
from .eosd import *

from CommonClient import (
	CommonContext,
	get_base_parser,
	logger,
	server_loop,
	gui_enabled,
)

class T6Context(CommonContext):
	"""Touhou 6 Game Context"""
	def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
		super().__init__(server_address, password)
		self.game = "Touhou 6"
		self.items_handling = 0b111  # Item from starting inventory, own world and other world
		self.pending_death_link = False

		self.eosd = None # eosdState

		# List of items/locations
		self.all_location_ids = None
		self.location_name_to_ap_id = None
		self.location_ap_id_to_name = None
		self.item_name_to_ap_id = None
		self.item_ap_id_to_name = None
		self.previous_location_checked = None

		self.is_connected = False

		# Counter
		self.difficulties = 0

		self.options = None
		self.otherDifficulties = True
		self.ExtraMenu = False

	async def server_auth(self, password_requested: bool = False):
		if password_requested and not self.password:
			await super().server_auth(password_requested)
		await self.get_username()
		await self.send_connect()

	def on_package(self, cmd: str, args: dict):
		if cmd == "Connected":
			self.all_location_ids = set(args["missing_locations"] + args["checked_locations"])
			self.options = args["slot_data"] # Yaml Options
			self.is_connected = True

			if self.eosd is not None:
				self.eosd.reset()

			asyncio.create_task(self.send_msgs([{"cmd": "GetDataPackage", "games": ["Touhou 6"]}]))

		if cmd == "ReceivedItems":
			asyncio.create_task(self.give_item(args["items"]))

		elif cmd == "DataPackage":
			if not self.all_location_ids:
				# Connected package not recieved yet, wait for datapackage request after connected package
				return
			self.location_name_to_ap_id = args["data"]["games"]["Touhou 6"]["location_name_to_id"]
			self.location_name_to_ap_id = {
				name: loc_id for name, loc_id in
				self.location_name_to_ap_id.items() if loc_id in self.all_location_ids
			}
			self.location_ap_id_to_name = {v: k for k, v in self.location_name_to_ap_id.items()}
			self.item_name_to_ap_id = args["data"]["games"]["Touhou 6"]["item_name_to_id"]
			self.item_ap_id_to_name = {v: k for k, v in self.item_name_to_ap_id.items()}
		elif cmd == "Bounced":
			tags = args.get("tags", [])
			# we can skip checking "DeathLink" in ctx.tags, as otherwise we wouldn't have been send this
			if "DeathLink" in tags and self.last_death_link != args["data"]["time"]:
				self.on_deathlink(args["data"])

	def client_recieved_initial_server_data(self):
		"""
		This method waits until the client finishes the initial conversation with the server.
		This means:
			- All LocationInfo packages recieved - requested only if patch files dont exist.
			- DataPackage package recieved (id_to_name maps and name_to_id maps are popualted)
			- Connection package recieved (slot number populated)
			- RoomInfo package recieved (seed name populated)
		"""
		return self.is_connected

	async def wait_for_initial_connection_info(self):
		"""
		This method waits until the client finishes the initial conversation with the server.
		See client_recieved_initial_server_data for wait requirements.
		"""
		if self.client_recieved_initial_server_data():
			return

		logger.info("Waiting for connect from server...")
		while not self.client_recieved_initial_server_data():
			await asyncio.sleep(1)

	async def give_item(self, items):
		"""
		Give an item to the player. This method will always give the oldest
		item that the player has recieved from AP, but not in game yet.

		:NetworkItem item: The item to give to the player
		"""

		isNormalMode = self.options['mode'] == 1
		isExtraStageLinear = self.options['extra_stage'] == 1
		isExtraStageApart = self.options['extra_stage'] == 2

		# We wait for the link to be etablished to the game before giving any items
		while self.eosd is None:
			await asyncio.sleep(0.5)

		for item in items:
			match item.item:
				case 60000: # Life
					self.eosd.addLife()
				case 60001: # Bomb
					self.eosd.addBomb()
				case 60002: # Lower Difficulty
					self.difficulties += 1
					self.eosd.unlockDifficulty(self.difficulties, isNormalMode)
				case 60003: # Reimu A
					self.eosd.unlockCharacter(0)
				case 60004: # Reimu B
					self.eosd.unlockCharacter(1)
				case 60005: # Marisa A
					self.eosd.unlockCharacter(2)
				case 60006: # Marisa B
					self.eosd.unlockCharacter(3)
				case 60013: # Next Stage
					if self.eosd.stages < 6:
						self.eosd.addStage()
					elif self.eosd.stages >= 6 and isExtraStageLinear:
						self.eosd.unlockExtraStage()
				case 60014 | 60018: # Ending Remilia
					character = REIMU if item.item == 60014 else MARISA
					self.eosd.addEndingRemilia(character)
					if self.checkVictory():
						await self.send_msgs([{"cmd": 'StatusUpdate', "status": 30}])
				case 60019 | 60020: # Ending Flandre
					character = REIMU if item.item == 60019 else MARISA
					self.eosd.addEndingFlandre(character)
					if self.checkVictory():
						await self.send_msgs([{"cmd": 'StatusUpdate', "status": 30}])
				case 60015: # 25 Power Point
					self.eosd.add25Power()
				case 60016: # 1 Continue
					self.eosd.addContinues()
				case 60017: # Extra Stage
					if isExtraStageApart:
						self.eosd.unlockExtraStage()
				case 60030: # 1 Power Point
					self.eosd.add1Power()
				case _:
					print(f"[EOSD] Unknown Item: {item}")

		# Update the stage list
		self.eosd.updateStageList()

	async def update_locations_checked(self):
		"""
		Check if any locations has been checked since last called, if a location has ben checked, we send a message and update ou list of checked locatio
		"""

		shot_type = self.options['shot_type']
		difficulty_check = self.options['difficulty_check']

		if difficulty_check:
			if shot_type:
				current_locations = {
					# Reimu A
					91162: self.eosd.isBossBeaten(0, 0, 0, 0, 0),
					91163: self.eosd.isBossBeaten(0, 0, 1, 0, 0),
					91165: self.eosd.isBossBeaten(0, 1, 0, 0, 0),
					91166: self.eosd.isBossBeaten(0, 1, 1, 0, 0),
					91168: self.eosd.isBossBeaten(0, 2, 0, 0, 0),
					91169: self.eosd.isBossBeaten(0, 2, 1, 0, 0),
					91171: self.eosd.isBossBeaten(0, 3, 0, 0, 0),
					91172: self.eosd.isBossBeaten(0, 3, 1, 0, 0),
					91174: self.eosd.isBossBeaten(0, 4, 0, 0, 0),
					91175: self.eosd.isBossBeaten(0, 4, 1, 0, 0),

					91270: self.eosd.isBossBeaten(0, 0, 0, 0, 1),
					91271: self.eosd.isBossBeaten(0, 0, 1, 0, 1),
					91273: self.eosd.isBossBeaten(0, 1, 0, 0, 1),
					91274: self.eosd.isBossBeaten(0, 1, 1, 0, 1),
					91276: self.eosd.isBossBeaten(0, 2, 0, 0, 1),
					91277: self.eosd.isBossBeaten(0, 2, 1, 0, 1),
					91279: self.eosd.isBossBeaten(0, 3, 0, 0, 1),
					91280: self.eosd.isBossBeaten(0, 3, 1, 0, 1),
					91282: self.eosd.isBossBeaten(0, 4, 0, 0, 1),
					91283: self.eosd.isBossBeaten(0, 4, 1, 0, 1),
					91285: self.eosd.isBossBeaten(0, 5, 0, 0, 1),
					91286: self.eosd.isBossBeaten(0, 5, 1, 0, 1),

					91378: self.eosd.isBossBeaten(0, 0, 0, 0, 2),
					91379: self.eosd.isBossBeaten(0, 0, 1, 0, 2),
					91381: self.eosd.isBossBeaten(0, 1, 0, 0, 2),
					91382: self.eosd.isBossBeaten(0, 1, 1, 0, 2),
					91384: self.eosd.isBossBeaten(0, 2, 0, 0, 2),
					91385: self.eosd.isBossBeaten(0, 2, 1, 0, 2),
					91387: self.eosd.isBossBeaten(0, 3, 0, 0, 2),
					91388: self.eosd.isBossBeaten(0, 3, 1, 0, 2),
					91390: self.eosd.isBossBeaten(0, 4, 0, 0, 2),
					91391: self.eosd.isBossBeaten(0, 4, 1, 0, 2),
					91393: self.eosd.isBossBeaten(0, 5, 0, 0, 2),
					91394: self.eosd.isBossBeaten(0, 5, 1, 0, 2),

					91486: self.eosd.isBossBeaten(0, 0, 0, 0, 3),
					91487: self.eosd.isBossBeaten(0, 0, 1, 0, 3),
					91489: self.eosd.isBossBeaten(0, 1, 0, 0, 3),
					91490: self.eosd.isBossBeaten(0, 1, 1, 0, 3),
					91492: self.eosd.isBossBeaten(0, 2, 0, 0, 3),
					91493: self.eosd.isBossBeaten(0, 2, 1, 0, 3),
					91495: self.eosd.isBossBeaten(0, 3, 0, 0, 3),
					91496: self.eosd.isBossBeaten(0, 3, 1, 0, 3),
					91498: self.eosd.isBossBeaten(0, 4, 0, 0, 3),
					91499: self.eosd.isBossBeaten(0, 4, 1, 0, 3),
					91501: self.eosd.isBossBeaten(0, 5, 0, 0, 3),
					91502: self.eosd.isBossBeaten(0, 5, 1, 0, 3),

					91044: self.eosd.isBossBeaten(0, 0, 1, 0),
					91047: self.eosd.isBossBeaten(0, 1, 1, 0),
					91050: self.eosd.isBossBeaten(0, 2, 1, 0),
					91053: self.eosd.isBossBeaten(0, 3, 1, 0),
					91056: self.eosd.isBossBeaten(0, 4, 1, 0),
					91059: self.eosd.isBossBeaten(0, 5, 1, 0),

					91060: self.eosd.isBossBeaten(0, 6, 0, 0),
					91061: self.eosd.isBossBeaten(0, 6, 1, 0),
					91062: self.eosd.isBossBeaten(0, 6, 1, 0),

					# Reimu B
					91180: self.eosd.isBossBeaten(0, 0, 0, 1, 0),
					91181: self.eosd.isBossBeaten(0, 0, 1, 1, 0),
					91183: self.eosd.isBossBeaten(0, 1, 0, 1, 0),
					91184: self.eosd.isBossBeaten(0, 1, 1, 1, 0),
					91186: self.eosd.isBossBeaten(0, 2, 0, 1, 0),
					91187: self.eosd.isBossBeaten(0, 2, 1, 1, 0),
					91189: self.eosd.isBossBeaten(0, 3, 0, 1, 0),
					91190: self.eosd.isBossBeaten(0, 3, 1, 1, 0),
					91192: self.eosd.isBossBeaten(0, 4, 0, 1, 0),
					91193: self.eosd.isBossBeaten(0, 4, 1, 1, 0),

					91288: self.eosd.isBossBeaten(0, 0, 0, 1, 1),
					91289: self.eosd.isBossBeaten(0, 0, 1, 1, 1),
					91291: self.eosd.isBossBeaten(0, 1, 0, 1, 1),
					91292: self.eosd.isBossBeaten(0, 1, 1, 1, 1),
					91294: self.eosd.isBossBeaten(0, 2, 0, 1, 1),
					91295: self.eosd.isBossBeaten(0, 2, 1, 1, 1),
					91297: self.eosd.isBossBeaten(0, 3, 0, 1, 1),
					91298: self.eosd.isBossBeaten(0, 3, 1, 1, 1),
					91300: self.eosd.isBossBeaten(0, 4, 0, 1, 1),
					91301: self.eosd.isBossBeaten(0, 4, 1, 1, 1),
					91303: self.eosd.isBossBeaten(0, 5, 0, 1, 1),
					91304: self.eosd.isBossBeaten(0, 5, 1, 1, 1),

					91396: self.eosd.isBossBeaten(0, 0, 0, 1, 2),
					91397: self.eosd.isBossBeaten(0, 0, 1, 1, 2),
					91399: self.eosd.isBossBeaten(0, 1, 0, 1, 2),
					91400: self.eosd.isBossBeaten(0, 1, 1, 1, 2),
					91402: self.eosd.isBossBeaten(0, 2, 0, 1, 2),
					91403: self.eosd.isBossBeaten(0, 2, 1, 1, 2),
					91405: self.eosd.isBossBeaten(0, 3, 0, 1, 2),
					91406: self.eosd.isBossBeaten(0, 3, 1, 1, 2),
					91408: self.eosd.isBossBeaten(0, 4, 0, 1, 2),
					91409: self.eosd.isBossBeaten(0, 4, 1, 1, 2),
					91411: self.eosd.isBossBeaten(0, 5, 0, 1, 2),
					91412: self.eosd.isBossBeaten(0, 5, 1, 1, 2),

					91504: self.eosd.isBossBeaten(0, 0, 0, 1, 3),
					91505: self.eosd.isBossBeaten(0, 0, 1, 1, 3),
					91507: self.eosd.isBossBeaten(0, 1, 0, 1, 3),
					91508: self.eosd.isBossBeaten(0, 1, 1, 1, 3),
					91510: self.eosd.isBossBeaten(0, 2, 0, 1, 3),
					91511: self.eosd.isBossBeaten(0, 2, 1, 1, 3),
					91513: self.eosd.isBossBeaten(0, 3, 0, 1, 3),
					91514: self.eosd.isBossBeaten(0, 3, 1, 1, 3),
					91516: self.eosd.isBossBeaten(0, 4, 0, 1, 3),
					91517: self.eosd.isBossBeaten(0, 4, 1, 1, 3),
					91519: self.eosd.isBossBeaten(0, 5, 0, 1, 3),
					91520: self.eosd.isBossBeaten(0, 5, 1, 1, 3),

					91065: self.eosd.isBossBeaten(0, 0, 1, 1),
					91068: self.eosd.isBossBeaten(0, 1, 1, 1),
					91071: self.eosd.isBossBeaten(0, 2, 1, 1),
					91074: self.eosd.isBossBeaten(0, 3, 1, 1),
					91077: self.eosd.isBossBeaten(0, 4, 1, 1),
					91080: self.eosd.isBossBeaten(0, 5, 1, 1),

					91081: self.eosd.isBossBeaten(0, 6, 0, 1),
					91082: self.eosd.isBossBeaten(0, 6, 1, 1),
					91083: self.eosd.isBossBeaten(0, 6, 1, 1),

					# Marisa A
					91198: self.eosd.isBossBeaten(1, 0, 0, 0, 0),
					91199: self.eosd.isBossBeaten(1, 0, 1, 0, 0),
					91201: self.eosd.isBossBeaten(1, 1, 0, 0, 0),
					91202: self.eosd.isBossBeaten(1, 1, 1, 0, 0),
					91204: self.eosd.isBossBeaten(1, 2, 0, 0, 0),
					91205: self.eosd.isBossBeaten(1, 2, 1, 0, 0),
					91207: self.eosd.isBossBeaten(1, 3, 0, 0, 0),
					91208: self.eosd.isBossBeaten(1, 3, 1, 0, 0),
					91210: self.eosd.isBossBeaten(1, 4, 0, 0, 0),
					91211: self.eosd.isBossBeaten(1, 4, 1, 0, 0),

					91306: self.eosd.isBossBeaten(1, 0, 0, 0, 1),
					91307: self.eosd.isBossBeaten(1, 0, 1, 0, 1),
					91309: self.eosd.isBossBeaten(1, 1, 0, 0, 1),
					91310: self.eosd.isBossBeaten(1, 1, 1, 0, 1),
					91312: self.eosd.isBossBeaten(1, 2, 0, 0, 1),
					91313: self.eosd.isBossBeaten(1, 2, 1, 0, 1),
					91315: self.eosd.isBossBeaten(1, 3, 0, 0, 1),
					91316: self.eosd.isBossBeaten(1, 3, 1, 0, 1),
					91318: self.eosd.isBossBeaten(1, 4, 0, 0, 1),
					91319: self.eosd.isBossBeaten(1, 4, 1, 0, 1),
					91321: self.eosd.isBossBeaten(1, 5, 0, 0, 1),
					91322: self.eosd.isBossBeaten(1, 5, 1, 0, 1),

					91414: self.eosd.isBossBeaten(1, 0, 0, 0, 2),
					91415: self.eosd.isBossBeaten(1, 0, 1, 0, 2),
					91417: self.eosd.isBossBeaten(1, 1, 0, 0, 2),
					91418: self.eosd.isBossBeaten(1, 1, 1, 0, 2),
					91420: self.eosd.isBossBeaten(1, 2, 0, 0, 2),
					91421: self.eosd.isBossBeaten(1, 2, 1, 0, 2),
					91423: self.eosd.isBossBeaten(1, 3, 0, 0, 2),
					91424: self.eosd.isBossBeaten(1, 3, 1, 0, 2),
					91426: self.eosd.isBossBeaten(1, 4, 0, 0, 2),
					91427: self.eosd.isBossBeaten(1, 4, 1, 0, 2),
					91429: self.eosd.isBossBeaten(1, 5, 0, 0, 2),
					91430: self.eosd.isBossBeaten(1, 5, 1, 0, 2),

					91522: self.eosd.isBossBeaten(1, 0, 0, 0, 3),
					91523: self.eosd.isBossBeaten(1, 0, 1, 0, 3),
					91525: self.eosd.isBossBeaten(1, 1, 0, 0, 3),
					91526: self.eosd.isBossBeaten(1, 1, 1, 0, 3),
					91528: self.eosd.isBossBeaten(1, 2, 0, 0, 3),
					91529: self.eosd.isBossBeaten(1, 2, 1, 0, 3),
					91531: self.eosd.isBossBeaten(1, 3, 0, 0, 3),
					91532: self.eosd.isBossBeaten(1, 3, 1, 0, 3),
					91534: self.eosd.isBossBeaten(1, 4, 0, 0, 3),
					91535: self.eosd.isBossBeaten(1, 4, 1, 0, 3),
					91537: self.eosd.isBossBeaten(1, 5, 0, 0, 3),
					91538: self.eosd.isBossBeaten(1, 5, 1, 0, 3),

					91086: self.eosd.isBossBeaten(1, 0, 1, 0),
					91089: self.eosd.isBossBeaten(1, 1, 1, 0),
					91092: self.eosd.isBossBeaten(1, 2, 1, 0),
					91095: self.eosd.isBossBeaten(1, 3, 1, 0),
					91098: self.eosd.isBossBeaten(1, 4, 1, 0),
					91101: self.eosd.isBossBeaten(1, 5, 1, 0),

					91102: self.eosd.isBossBeaten(1, 6, 0, 0),
					91103: self.eosd.isBossBeaten(1, 6, 1, 0),
					91104: self.eosd.isBossBeaten(1, 6, 1, 0),

					# Marisa B
					91216: self.eosd.isBossBeaten(1, 0, 0, 1, 0),
					91217: self.eosd.isBossBeaten(1, 0, 1, 1, 0),
					91219: self.eosd.isBossBeaten(1, 1, 0, 1, 0),
					91220: self.eosd.isBossBeaten(1, 1, 1, 1, 0),
					91222: self.eosd.isBossBeaten(1, 2, 0, 1, 0),
					91223: self.eosd.isBossBeaten(1, 2, 1, 1, 0),
					91225: self.eosd.isBossBeaten(1, 3, 0, 1, 0),
					91226: self.eosd.isBossBeaten(1, 3, 1, 1, 0),
					91228: self.eosd.isBossBeaten(1, 4, 0, 1, 0),
					91229: self.eosd.isBossBeaten(1, 4, 1, 1, 0),

					91324: self.eosd.isBossBeaten(1, 0, 0, 1, 1),
					91325: self.eosd.isBossBeaten(1, 0, 1, 1, 1),
					91327: self.eosd.isBossBeaten(1, 1, 0, 1, 1),
					91328: self.eosd.isBossBeaten(1, 1, 1, 1, 1),
					91330: self.eosd.isBossBeaten(1, 2, 0, 1, 1),
					91331: self.eosd.isBossBeaten(1, 2, 1, 1, 1),
					91333: self.eosd.isBossBeaten(1, 3, 0, 1, 1),
					91334: self.eosd.isBossBeaten(1, 3, 1, 1, 1),
					91336: self.eosd.isBossBeaten(1, 4, 0, 1, 1),
					91337: self.eosd.isBossBeaten(1, 4, 1, 1, 1),
					91339: self.eosd.isBossBeaten(1, 5, 0, 1, 1),
					91340: self.eosd.isBossBeaten(1, 5, 1, 1, 1),

					91432: self.eosd.isBossBeaten(1, 0, 0, 1, 2),
					91433: self.eosd.isBossBeaten(1, 0, 1, 1, 2),
					91435: self.eosd.isBossBeaten(1, 1, 0, 1, 2),
					91436: self.eosd.isBossBeaten(1, 1, 1, 1, 2),
					91438: self.eosd.isBossBeaten(1, 2, 0, 1, 2),
					91439: self.eosd.isBossBeaten(1, 2, 1, 1, 2),
					91441: self.eosd.isBossBeaten(1, 3, 0, 1, 2),
					91442: self.eosd.isBossBeaten(1, 3, 1, 1, 2),
					91444: self.eosd.isBossBeaten(1, 4, 0, 1, 2),
					91445: self.eosd.isBossBeaten(1, 4, 1, 1, 2),
					91447: self.eosd.isBossBeaten(1, 5, 0, 1, 2),
					91448: self.eosd.isBossBeaten(1, 5, 1, 1, 2),

					91540: self.eosd.isBossBeaten(1, 0, 0, 1, 3),
					91541: self.eosd.isBossBeaten(1, 0, 1, 1, 3),
					91543: self.eosd.isBossBeaten(1, 1, 0, 1, 3),
					91544: self.eosd.isBossBeaten(1, 1, 1, 1, 3),
					91546: self.eosd.isBossBeaten(1, 2, 0, 1, 3),
					91547: self.eosd.isBossBeaten(1, 2, 1, 1, 3),
					91549: self.eosd.isBossBeaten(1, 3, 0, 1, 3),
					91550: self.eosd.isBossBeaten(1, 3, 1, 1, 3),
					91552: self.eosd.isBossBeaten(1, 4, 0, 1, 3),
					91553: self.eosd.isBossBeaten(1, 4, 1, 1, 3),
					91555: self.eosd.isBossBeaten(1, 5, 0, 1, 3),
					91556: self.eosd.isBossBeaten(1, 5, 1, 1, 3),

					91107: self.eosd.isBossBeaten(1, 0, 1, 1),
					91110: self.eosd.isBossBeaten(1, 1, 1, 1),
					91113: self.eosd.isBossBeaten(1, 2, 1, 1),
					91116: self.eosd.isBossBeaten(1, 3, 1, 1),
					91119: self.eosd.isBossBeaten(1, 4, 1, 1),
					91122: self.eosd.isBossBeaten(1, 5, 1, 1),

					91123: self.eosd.isBossBeaten(1, 6, 0, 1),
					91124: self.eosd.isBossBeaten(1, 6, 1, 1),
					91125: self.eosd.isBossBeaten(1, 6, 1, 1),
				}
			else:
				current_locations = {
					# Reimu
					91126: self.eosd.isBossBeaten(0, 0, 0, -1, 0),
					91127: self.eosd.isBossBeaten(0, 0, 1, -1, 0),
					91129: self.eosd.isBossBeaten(0, 1, 0, -1, 0),
					91130: self.eosd.isBossBeaten(0, 1, 1, -1, 0),
					91132: self.eosd.isBossBeaten(0, 2, 0, -1, 0),
					91133: self.eosd.isBossBeaten(0, 2, 1, -1, 0),
					91135: self.eosd.isBossBeaten(0, 3, 0, -1, 0),
					91136: self.eosd.isBossBeaten(0, 3, 1, -1, 0),
					91138: self.eosd.isBossBeaten(0, 4, 0, -1, 0),
					91139: self.eosd.isBossBeaten(0, 4, 1, -1, 0),

					91234: self.eosd.isBossBeaten(0, 0, 0, -1, 1),
					91235: self.eosd.isBossBeaten(0, 0, 1, -1, 1),
					91237: self.eosd.isBossBeaten(0, 1, 0, -1, 1),
					91238: self.eosd.isBossBeaten(0, 1, 1, -1, 1),
					91240: self.eosd.isBossBeaten(0, 2, 0, -1, 1),
					91241: self.eosd.isBossBeaten(0, 2, 1, -1, 1),
					91243: self.eosd.isBossBeaten(0, 3, 0, -1, 1),
					91244: self.eosd.isBossBeaten(0, 3, 1, -1, 1),
					91246: self.eosd.isBossBeaten(0, 4, 0, -1, 1),
					91247: self.eosd.isBossBeaten(0, 4, 1, -1, 1),
					91249: self.eosd.isBossBeaten(0, 5, 0, -1, 1),
					91250: self.eosd.isBossBeaten(0, 5, 1, -1, 1),

					91342: self.eosd.isBossBeaten(0, 0, 0, -1, 2),
					91343: self.eosd.isBossBeaten(0, 0, 1, -1, 2),
					91345: self.eosd.isBossBeaten(0, 1, 0, -1, 2),
					91346: self.eosd.isBossBeaten(0, 1, 1, -1, 2),
					91348: self.eosd.isBossBeaten(0, 2, 0, -1, 2),
					91349: self.eosd.isBossBeaten(0, 2, 1, -1, 2),
					91351: self.eosd.isBossBeaten(0, 3, 0, -1, 2),
					91352: self.eosd.isBossBeaten(0, 3, 1, -1, 2),
					91354: self.eosd.isBossBeaten(0, 4, 0, -1, 2),
					91355: self.eosd.isBossBeaten(0, 4, 1, -1, 2),
					91357: self.eosd.isBossBeaten(0, 5, 0, -1, 2),
					91358: self.eosd.isBossBeaten(0, 5, 1, -1, 2),

					91450: self.eosd.isBossBeaten(0, 0, 0, -1, 3),
					91451: self.eosd.isBossBeaten(0, 0, 1, -1, 3),
					91453: self.eosd.isBossBeaten(0, 1, 0, -1, 3),
					91454: self.eosd.isBossBeaten(0, 1, 1, -1, 3),
					91456: self.eosd.isBossBeaten(0, 2, 0, -1, 3),
					91457: self.eosd.isBossBeaten(0, 2, 1, -1, 3),
					91459: self.eosd.isBossBeaten(0, 3, 0, -1, 3),
					91460: self.eosd.isBossBeaten(0, 3, 1, -1, 3),
					91462: self.eosd.isBossBeaten(0, 4, 0, -1, 3),
					91463: self.eosd.isBossBeaten(0, 4, 1, -1, 3),
					91465: self.eosd.isBossBeaten(0, 5, 0, -1, 3),
					91466: self.eosd.isBossBeaten(0, 5, 1, -1, 3),

					91034: self.eosd.isBossBeaten(0, 0, 1),
					91003: self.eosd.isBossBeaten(0, 1, 1),
					91005: self.eosd.isBossBeaten(0, 2, 1),
					91009: self.eosd.isBossBeaten(0, 3, 1),
					91011: self.eosd.isBossBeaten(0, 4, 1),
					91014: self.eosd.isBossBeaten(0, 5, 1),

					91036: self.eosd.isBossBeaten(0, 6, 0),
					91037: self.eosd.isBossBeaten(0, 6, 1),
					91038: self.eosd.isBossBeaten(0, 6, 1),

					# Marisa
					91144: self.eosd.isBossBeaten(1, 0, 0, -1, 0),
					91145: self.eosd.isBossBeaten(1, 0, 1, -1, 0),
					91147: self.eosd.isBossBeaten(1, 1, 0, -1, 0),
					91148: self.eosd.isBossBeaten(1, 1, 1, -1, 0),
					91150: self.eosd.isBossBeaten(1, 2, 0, -1, 0),
					91151: self.eosd.isBossBeaten(1, 2, 1, -1, 0),
					91153: self.eosd.isBossBeaten(1, 3, 0, -1, 0),
					91154: self.eosd.isBossBeaten(1, 3, 1, -1, 0),
					91156: self.eosd.isBossBeaten(1, 4, 0, -1, 0),
					91157: self.eosd.isBossBeaten(1, 4, 1, -1, 0),

					91252: self.eosd.isBossBeaten(1, 0, 0, -1, 1),
					91253: self.eosd.isBossBeaten(1, 0, 1, -1, 1),
					91255: self.eosd.isBossBeaten(1, 1, 0, -1, 1),
					91256: self.eosd.isBossBeaten(1, 1, 1, -1, 1),
					91258: self.eosd.isBossBeaten(1, 2, 0, -1, 1),
					91259: self.eosd.isBossBeaten(1, 2, 1, -1, 1),
					91261: self.eosd.isBossBeaten(1, 3, 0, -1, 1),
					91262: self.eosd.isBossBeaten(1, 3, 1, -1, 1),
					91264: self.eosd.isBossBeaten(1, 4, 0, -1, 1),
					91265: self.eosd.isBossBeaten(1, 4, 1, -1, 1),
					91267: self.eosd.isBossBeaten(1, 5, 0, -1, 1),
					91268: self.eosd.isBossBeaten(1, 5, 1, -1, 1),

					91360: self.eosd.isBossBeaten(1, 0, 0, -1, 2),
					91361: self.eosd.isBossBeaten(1, 0, 1, -1, 2),
					91363: self.eosd.isBossBeaten(1, 1, 0, -1, 2),
					91364: self.eosd.isBossBeaten(1, 1, 1, -1, 2),
					91366: self.eosd.isBossBeaten(1, 2, 0, -1, 2),
					91367: self.eosd.isBossBeaten(1, 2, 1, -1, 2),
					91369: self.eosd.isBossBeaten(1, 3, 0, -1, 2),
					91370: self.eosd.isBossBeaten(1, 3, 1, -1, 2),
					91372: self.eosd.isBossBeaten(1, 4, 0, -1, 2),
					91373: self.eosd.isBossBeaten(1, 4, 1, -1, 2),
					91375: self.eosd.isBossBeaten(1, 5, 0, -1, 2),
					91376: self.eosd.isBossBeaten(1, 5, 1, -1, 2),

					91468: self.eosd.isBossBeaten(1, 0, 0, -1, 3),
					91469: self.eosd.isBossBeaten(1, 0, 1, -1, 3),
					91471: self.eosd.isBossBeaten(1, 1, 0, -1, 3),
					91472: self.eosd.isBossBeaten(1, 1, 1, -1, 3),
					91474: self.eosd.isBossBeaten(1, 2, 0, -1, 3),
					91475: self.eosd.isBossBeaten(1, 2, 1, -1, 3),
					91477: self.eosd.isBossBeaten(1, 3, 0, -1, 3),
					91478: self.eosd.isBossBeaten(1, 3, 1, -1, 3),
					91480: self.eosd.isBossBeaten(1, 4, 0, -1, 3),
					91481: self.eosd.isBossBeaten(1, 4, 1, -1, 3),
					91483: self.eosd.isBossBeaten(1, 5, 0, -1, 3),
					91484: self.eosd.isBossBeaten(1, 5, 1, -1, 3),

					91035: self.eosd.isBossBeaten(1, 0, 1),
					91020: self.eosd.isBossBeaten(1, 1, 1),
					91022: self.eosd.isBossBeaten(1, 2, 1),
					91026: self.eosd.isBossBeaten(1, 3, 1),
					91028: self.eosd.isBossBeaten(1, 4, 1),
					91031: self.eosd.isBossBeaten(1, 5, 1),

					91039: self.eosd.isBossBeaten(1, 6, 0),
					91040: self.eosd.isBossBeaten(1, 6, 1),
					91041: self.eosd.isBossBeaten(1, 6, 1),
				}
		else:
			if shot_type:
				current_locations = {
					91042: self.eosd.isBossBeaten(0, 0, 0, 0),
					91043: self.eosd.isBossBeaten(0, 0, 1, 0),
					91044: self.eosd.isBossBeaten(0, 0, 1, 0),
					91045: self.eosd.isBossBeaten(0, 1, 0, 0),
					91046: self.eosd.isBossBeaten(0, 1, 1, 0),
					91047: self.eosd.isBossBeaten(0, 1, 1, 0),
					91048: self.eosd.isBossBeaten(0, 2, 0, 0),
					91049: self.eosd.isBossBeaten(0, 2, 1, 0),
					91050: self.eosd.isBossBeaten(0, 2, 1, 0),
					91051: self.eosd.isBossBeaten(0, 3, 0, 0),
					91052: self.eosd.isBossBeaten(0, 3, 1, 0),
					91053: self.eosd.isBossBeaten(0, 3, 1, 0),
					91054: self.eosd.isBossBeaten(0, 4, 0, 0),
					91055: self.eosd.isBossBeaten(0, 4, 1, 0),
					91056: self.eosd.isBossBeaten(0, 4, 1, 0),
					91057: self.eosd.isBossBeaten(0, 5, 0, 0),
					91058: self.eosd.isBossBeaten(0, 5, 1, 0),
					91059: self.eosd.isBossBeaten(0, 5, 1, 0),
					91060: self.eosd.isBossBeaten(0, 6, 0, 0),
					91061: self.eosd.isBossBeaten(0, 6, 1, 0),
					91062: self.eosd.isBossBeaten(0, 6, 1, 0),

					91063: self.eosd.isBossBeaten(0, 0, 0, 1),
					91064: self.eosd.isBossBeaten(0, 0, 1, 1),
					91065: self.eosd.isBossBeaten(0, 0, 1, 1),
					91066: self.eosd.isBossBeaten(0, 1, 0, 1),
					91067: self.eosd.isBossBeaten(0, 1, 1, 1),
					91068: self.eosd.isBossBeaten(0, 1, 1, 1),
					91069: self.eosd.isBossBeaten(0, 2, 0, 1),
					91070: self.eosd.isBossBeaten(0, 2, 1, 1),
					91071: self.eosd.isBossBeaten(0, 2, 1, 1),
					91072: self.eosd.isBossBeaten(0, 3, 0, 1),
					91073: self.eosd.isBossBeaten(0, 3, 1, 1),
					91074: self.eosd.isBossBeaten(0, 3, 1, 1),
					91075: self.eosd.isBossBeaten(0, 4, 0, 1),
					91076: self.eosd.isBossBeaten(0, 4, 1, 1),
					91077: self.eosd.isBossBeaten(0, 4, 1, 1),
					91078: self.eosd.isBossBeaten(0, 5, 0, 1),
					91079: self.eosd.isBossBeaten(0, 5, 1, 1),
					91080: self.eosd.isBossBeaten(0, 5, 1, 1),
					91081: self.eosd.isBossBeaten(0, 6, 0, 1),
					91082: self.eosd.isBossBeaten(0, 6, 1, 1),
					91083: self.eosd.isBossBeaten(0, 6, 1, 1),

					91084: self.eosd.isBossBeaten(1, 0, 0, 0),
					91085: self.eosd.isBossBeaten(1, 0, 1, 0),
					91086: self.eosd.isBossBeaten(1, 0, 1, 0),
					91087: self.eosd.isBossBeaten(1, 1, 0, 0),
					91088: self.eosd.isBossBeaten(1, 1, 1, 0),
					91089: self.eosd.isBossBeaten(1, 1, 1, 0),
					91090: self.eosd.isBossBeaten(1, 2, 0, 0),
					91091: self.eosd.isBossBeaten(1, 2, 1, 0),
					91092: self.eosd.isBossBeaten(1, 2, 1, 0),
					91093: self.eosd.isBossBeaten(1, 3, 0, 0),
					91094: self.eosd.isBossBeaten(1, 3, 1, 0),
					91095: self.eosd.isBossBeaten(1, 3, 1, 0),
					91096: self.eosd.isBossBeaten(1, 4, 0, 0),
					91097: self.eosd.isBossBeaten(1, 4, 1, 0),
					91098: self.eosd.isBossBeaten(1, 4, 1, 0),
					91099: self.eosd.isBossBeaten(1, 5, 0, 0),
					91100: self.eosd.isBossBeaten(1, 5, 1, 0),
					91101: self.eosd.isBossBeaten(1, 5, 1, 0),
					91102: self.eosd.isBossBeaten(1, 6, 0, 0),
					91103: self.eosd.isBossBeaten(1, 6, 1, 0),
					91104: self.eosd.isBossBeaten(1, 6, 1, 0),

					91105: self.eosd.isBossBeaten(1, 0, 0, 1),
					91106: self.eosd.isBossBeaten(1, 0, 1, 1),
					91107: self.eosd.isBossBeaten(1, 0, 1, 1),
					91108: self.eosd.isBossBeaten(1, 1, 0, 1),
					91109: self.eosd.isBossBeaten(1, 1, 1, 1),
					91110: self.eosd.isBossBeaten(1, 1, 1, 1),
					91111: self.eosd.isBossBeaten(1, 2, 0, 1),
					91112: self.eosd.isBossBeaten(1, 2, 1, 1),
					91113: self.eosd.isBossBeaten(1, 2, 1, 1),
					91114: self.eosd.isBossBeaten(1, 3, 0, 1),
					91115: self.eosd.isBossBeaten(1, 3, 1, 1),
					91116: self.eosd.isBossBeaten(1, 3, 1, 1),
					91117: self.eosd.isBossBeaten(1, 4, 0, 1),
					91118: self.eosd.isBossBeaten(1, 4, 1, 1),
					91119: self.eosd.isBossBeaten(1, 4, 1, 1),
					91120: self.eosd.isBossBeaten(1, 5, 0, 1),
					91121: self.eosd.isBossBeaten(1, 5, 1, 1),
					91122: self.eosd.isBossBeaten(1, 5, 1, 1),
					91123: self.eosd.isBossBeaten(1, 6, 0, 1),
					91124: self.eosd.isBossBeaten(1, 6, 1, 1),
					91125: self.eosd.isBossBeaten(1, 6, 1, 1),
				}
			else:
				current_locations = {
					91000: self.eosd.isBossBeaten(0, 0, 0),
					91001: self.eosd.isBossBeaten(0, 0, 1),
					91034: self.eosd.isBossBeaten(0, 0, 1),
					91002: self.eosd.isBossBeaten(0, 1, 0),
					91004: self.eosd.isBossBeaten(0, 1, 1),
					91003: self.eosd.isBossBeaten(0, 1, 1),
					91006: self.eosd.isBossBeaten(0, 2, 0),
					91007: self.eosd.isBossBeaten(0, 2, 1),
					91005: self.eosd.isBossBeaten(0, 2, 1),
					91008: self.eosd.isBossBeaten(0, 3, 0),
					91010: self.eosd.isBossBeaten(0, 3, 1),
					91009: self.eosd.isBossBeaten(0, 3, 1),
					91012: self.eosd.isBossBeaten(0, 4, 0),
					91013: self.eosd.isBossBeaten(0, 4, 1),
					91011: self.eosd.isBossBeaten(0, 4, 1),
					91015: self.eosd.isBossBeaten(0, 5, 0),
					91016: self.eosd.isBossBeaten(0, 5, 1),
					91014: self.eosd.isBossBeaten(0, 5, 1),
					91017: self.eosd.isBossBeaten(1, 0, 0),
					91018: self.eosd.isBossBeaten(1, 0, 1),
					91035: self.eosd.isBossBeaten(1, 0, 1),
					91019: self.eosd.isBossBeaten(1, 1, 0),
					91021: self.eosd.isBossBeaten(1, 1, 1),
					91020: self.eosd.isBossBeaten(1, 1, 1),
					91023: self.eosd.isBossBeaten(1, 2, 0),
					91024: self.eosd.isBossBeaten(1, 2, 1),
					91022: self.eosd.isBossBeaten(1, 2, 1),
					91025: self.eosd.isBossBeaten(1, 3, 0),
					91027: self.eosd.isBossBeaten(1, 3, 1),
					91026: self.eosd.isBossBeaten(1, 3, 1),
					91029: self.eosd.isBossBeaten(1, 4, 0),
					91030: self.eosd.isBossBeaten(1, 4, 1),
					91028: self.eosd.isBossBeaten(1, 4, 1),
					91032: self.eosd.isBossBeaten(1, 5, 0),
					91033: self.eosd.isBossBeaten(1, 5, 1),
					91031: self.eosd.isBossBeaten(1, 5, 1),
					91036: self.eosd.isBossBeaten(0, 6, 0),
					91037: self.eosd.isBossBeaten(0, 6, 1),
					91038: self.eosd.isBossBeaten(0, 6, 1),
					91039: self.eosd.isBossBeaten(1, 6, 0),
					91040: self.eosd.isBossBeaten(1, 6, 1),
					91041: self.eosd.isBossBeaten(1, 6, 1),
				}

		if self.previous_location_checked != current_locations:
			locations = []

			for id, value in current_locations.items():
				if value:
					locations.append(id)

			self.previous_location_checked = current_locations
			await self.send_msgs([{"cmd": 'LocationChecks', "locations": locations}])

	def on_deathlink(self, data):
		self.pending_death_link = True
		return super().on_deathlink(data)

	async def send_death_link(self):
		if self.options['death_link']:
			await self.send_death()

	def giveResources(self):
		isNormalMode = self.options['mode'] == 1
		return self.eosd.giveAllResources(isNormalMode)

	def updateStageList(self):
		shot_type = self.options['shot_type']
		difficulty_check = self.options['difficulty_check']

		self.eosd.updateStageList()
		self.eosd.updatePracticeScore(shot_type, difficulty_check)

	def checkVictory(self):
		goal = self.options['goal']
		endingRequired = self.options['ending_required']
		shot_type = self.options['shot_type']
		extra = self.options['extra_stage']
		victory = False

		if not shot_type and endingRequired == 2:
			endingRequired = 1

		if goal == 0 or extra == 0: # Remilia
			if endingRequired == 0: # One
				victory = self.eosd.endingRemilia[0] or self.eosd.endingRemilia[1]
			elif endingRequired == 1: # Both characters
				victory = self.eosd.endingRemilia[0] and self.eosd.endingRemilia[1]
			elif endingRequired == 2: # All Shot type
				victory = self.eosd.endingRemilia[0] >= 2 and self.eosd.endingRemilia[1] >= 2
		elif goal == 1: # Flandre
			if endingRequired == 0: # One
				victory = self.eosd.endingFlandre[0] or self.eosd.endingFlandre[1]
			elif endingRequired == 1: # Both characters
				victory = self.eosd.endingFlandre[0] and self.eosd.endingFlandre[1]
			elif endingRequired == 2: # All Shot type
				victory = self.eosd.endingFlandre[0] >= 2 and self.eosd.endingFlandre[1] >= 2
		elif goal == 2: # Both
			if endingRequired == 0: # One
				victory = (self.eosd.endingRemilia[0] or self.eosd.endingRemilia[1]) and (self.eosd.endingFlandre[0] or self.eosd.endingFlandre[1])
			elif endingRequired == 1: # Both characters
				victory = (self.eosd.endingRemilia[0] and self.eosd.endingRemilia[1]) and (self.eosd.endingFlandre[0] and self.eosd.endingFlandre[1])
			elif endingRequired == 2: # All Shot type
				victory = (self.eosd.endingRemilia[0] >= 2 and self.eosd.endingRemilia[1] >= 2) and (self.eosd.endingFlandre[0] >= 2 and self.eosd.endingFlandre[1] >= 2)

		return victory

	async def extra_unlock_loop(self):
		while True:
			if self.eosd.gameController.getGameMode() == 1:
				menu = self.eosd.gameController.getMenu()
				# We check where we are in the menu in order to determine how we lock/unlock the characters
				if menu in [0, 18]  or self.eosd.gameController.getDifficulty() == 4:
					self.ExtraMenu = True
				elif menu in [6] or self.eosd.gameController.getDifficulty() < 4:
					self.ExtraMenu = False

				self.eosd.updateExtraUnlock(not self.ExtraMenu)
			await asyncio.sleep(0.1)

	async def difficulty_cursor_loop(self):
		while True:
			if  self.eosd.gameController.getMenu() == 6:
				self.eosd.checkCursor()
				await asyncio.sleep(0.05)
			else:
				await asyncio.sleep(0.1)

	async def connect_to_eosd(self):
		self.eosd = None

		while not self.eosd:
			pid = await find_process()
			if pid:
				self.eosd = eosdState(pid)
			await asyncio.sleep(2)

	async def reconnect_to_eosd(self):
		self.eosd.gameController = None

		while not self.eosd.gameController:
			pid = await find_process()
			if pid:
				self.eosd.gameController = eosdController(pid)
			await asyncio.sleep(2)

async def touhou_6_watcher(ctx: T6Context):
	"""
	Client loop, watching the game process.
	Handles game hook attachments, checking locations, giving items, etc.

	:T6Context ctx: The client context instance.
	"""
	# Init
	bossPresent = False
	currentMode = 0
	currentLives = 0
	bossCounter = -1
	resourcesGiven = False
	disconnected = False
	currentMisses = 0
	onGoingDeathLink = False
	deathCounter = 0
	hasDied = False

	await ctx.wait_for_initial_connection_info()

	while not ctx.exit_event.is_set():
		if not ctx.server:
			# client disconnected from server
			await ctx.wait_for_initial_connection_info()
		# First connection
		if ctx.eosd is None and not disconnected:
			logger.info("Waiting for connection to Touhou 6...")
			asyncio.create_task(ctx.connect_to_eosd())
			while(ctx.eosd is None and not ctx.exit_event.is_set()):
				await asyncio.sleep(1)
		# Connection following an error
		if disconnected:
			logger.info("Connection lost. Waiting for connection to Touhou 6...")
			asyncio.create_task(ctx.reconnect_to_eosd())
			while(ctx.eosd.gameController is None and not ctx.exit_event.is_set()):
				await asyncio.sleep(1)
			disconnected = False
			ctx.updateStageList()
		try:
			if ctx.eosd:
				logger.info("Touhou 6 process found. Starting loop...")

			# We start the loop for the extra menu and the difficulty cursor in tasks since they need to be faster
			asyncio.create_task(ctx.extra_unlock_loop())
			asyncio.create_task(ctx.difficulty_cursor_loop())

			# Activating Death Link
			if ctx.options['death_link']:
				await ctx.update_death_link(True)

			# We set the lock for all the difficulty
			ctx.eosd.gameController.setLockToAllDifficulty()

			while not ctx.exit_event.is_set():
				await asyncio.sleep(0.5)
				gameMode = ctx.eosd.gameController.getGameMode()
				inDemo = ctx.eosd.gameController.getInDemo()

				# If we're in the demo, we reset the mode so that the variables in the menu can be reset correctly
				if inDemo == 1:
					currentMode = 0
					continue

				if(gameMode == 2):
					# Mode Check
					if(currentMode != 2): # A level has started
						currentMode = 2
						bossCounter = -1
						bossPresent = False
						currentMisses = ctx.eosd.gameController.getMisses()
						onGoingDeathLink = False
						ctx.pending_death_link = False

					if(not resourcesGiven):
						ctx.giveResources()
						resourcesGiven = True
						currentLives = ctx.eosd.gameController.getLives()

					# Boss Check
					if(not bossPresent):
						if(ctx.eosd.gameController.getIsBossPresent() == 1):
							# If a third boss is found, it's just that there is a problem and we ignore it
							if bossCounter < 2:
								bossPresent = True
								bossCounter += 1
								# print(f"{ctx.eosd.getBossName(bossCounter)} spawned")
					else:
						if bossPresent:
							if(ctx.eosd.gameController.getIsBossPresent() == 0):
								# print(f"{ctx.eosd.getBossName(bossCounter)} has been defeated")
								if(not ctx.eosd.isCurrentBossDefeated(bossCounter)):
									ctx.eosd.setbossBeaten(bossCounter, ctx.otherDifficulties)
									await ctx.update_locations_checked()
								bossPresent = False

					# Death Check
					# If a death link is sent, we set the flag
					if ctx.pending_death_link and not onGoingDeathLink:
						onGoingDeathLink = True

					# If a death has occured in game
					if currentMisses < ctx.eosd.gameController.getMisses():
						if not onGoingDeathLink: #Check if it's not by a death link in order to send a death link
							hasDied = True
							deathCounter = 3
						else: # If the player is killed by a death link, we tell the loop it's done
							onGoingDeathLink = False
							ctx.pending_death_link = False

						currentMisses += 1
					elif ctx.pending_death_link: #If no death has occured but a deahth link is pending, we try to kill the player
						ctx.eosd.gameController.setKill(True)
						await asyncio.sleep(0.1)
						ctx.eosd.gameController.setKill(False)

					if(currentLives != ctx.eosd.gameController.getLives()): # We update resources after the life has fully been lost
						if(currentLives > ctx.eosd.gameController.getLives()):
							# We give the bombs resources
							ctx.eosd.giveBombs()

						currentLives = ctx.eosd.gameController.getLives()

						if hasDied:
							await ctx.send_death_link()
							hasDied = False
					elif hasDied: # If the player has deathbomb
						if deathCounter > 0:
							deathCounter -= 1

						if deathCounter <= 0:
							hasDied = False

				elif(gameMode == 1):
					# Mode Check
					if(currentMode != 1): # We enter in the menu
						ctx.eosd.gameController.resetHpEnemies()
						ctx.eosd.gameController.resetBossPresent()
						currentMode = 1
						resourcesGiven = False
						if hasDied:
							await ctx.send_death_link()
						hasDied = False
						deathCounter = 0
						ctx.updateStageList()
				else: # If we're not in a level or a menu, we're probably in the Result Screen
					bossCounter = -1

		except Exception as err:  # Process closed?
			print(f"ERROR: {err}")
			disconnected = True
			ctx.eosd.gameController = None
			# attempt to reconnect at the top of the loop
			await asyncio.sleep(0.5)
			continue

def launch():
	"""
	Launch a client instance (wrapper / args parser)
	"""
	async def main(args):
		"""
		Launch a client instance (threaded)
		"""
		ctx = T6Context(args.connect, args.password)
		ctx.server_task = asyncio.create_task(server_loop(ctx), name="touhou 6 server loop")
		if gui_enabled:
			ctx.run_gui()
		ctx.run_cli()
		watcher = asyncio.create_task(
			touhou_6_watcher(ctx),
			name="Touhou6ProgressionWatcher"
		)
		await ctx.exit_event.wait()
		await watcher
		await ctx.shutdown()

	parser = get_base_parser(description="Touhou 6 Client")
	args, _ = parser.parse_known_args()

	colorama.init()
	asyncio.run(main(args))
	colorama.deinit()