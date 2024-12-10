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

		# We wait for the link to be etablished to the game before giving any items
		while self.eosd is None:
			await asyncio.sleep(0.5)

		for item in items:
			match item.item:
				case 60000:
					self.eosd.addLife()
				case 60001:
					self.eosd.addBomb()
				case 60002:
					self.difficulties += 1
					self.eosd.unlockDifficulty(self.difficulties, isNormalMode)
				case 60003:
					self.eosd.unlockCharacter(0)
				case 60004:
					self.eosd.unlockCharacter(1)
				case 60005:
					self.eosd.unlockCharacter(2)
				case 60006:
					self.eosd.unlockCharacter(3)
				case 60013:
					self.eosd.addStage()
				case 60014:
					self.eosd.addEnding()
					if self.eosd.getEndings() >= self.options['ending_required']:
						await self.send_msgs([{"cmd": 'StatusUpdate', "status": 30}])
				case 60015:
					self.eosd.add25Power()
				case 60016:
					self.eosd.addContinues()
				case 60030:
					self.eosd.add1Power()
				case _:
					print(f"[EOSD] Unknown Item: {item}")

	async def update_locations_checked(self):
		"""
		Check if any locations has been checked since last called, if a location has ben checked, we send a message and update ou list of checked locatio
		"""

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

async def touhou_6_watcher(ctx: T6Context):
	"""
	Client loop, watching the game process.
	Handles game hook attachments, checking locations, giving items, etc.

	:T6Context ctx: The client context instance.
	"""
	# Init
	noBoss = True
	bossHpId = -1
	currentMode = 0
	currentLives = 0
	bossCounter = -1
	resourcesGiven = False
	bossCurrentHp = 0
	disconnected = False
	currentMisses = 0
	onGoingDeathLink = False

	await ctx.wait_for_initial_connection_info()

	while not ctx.exit_event.is_set():
		if not ctx.server:
			# client disconnected from server
			await ctx.wait_for_initial_connection_info()
		# First connection
		if ctx.eosd is None:
			logger.info("Waiting for connection to Touhou 6...")
			ctx.eosd = connect_to_t6()
			while(ctx.eosd is None and not ctx.exit_event.is_set()):
				await asyncio.sleep(0.5)
				ctx.eosd = connect_to_t6()
		# Connection following an error
		if disconnected:
			logger.info("Connection lost. Waiting for connection to Touhou 6...")
			ctx.eosd.reconnect()
			while(ctx.eosd.gameController is None and not ctx.exit_event.is_set()):
				await asyncio.sleep(0.5)
				ctx.eosd.reconnect()
			disconnected = False
			ctx.eosd.updateStageList()
		try:
			logger.info("Touhou 6 process found. Starting loop...")

			# Activating Death Link
			if ctx.options['death_link']:
				await ctx.update_death_link(True)

			while not ctx.exit_event.is_set():
				await asyncio.sleep(0.5)
				if(ctx.eosd.gameController.getGameMode() == 2):
					# Mode Check
					if(currentMode != 2): # A level has started
						currentMode = 2
						bossCounter = -1
						currentMisses = ctx.eosd.gameController.getMisses()
						onGoingDeathLink = False
						ctx.pending_death_link = False

					if(not resourcesGiven):
						ctx.giveResources()
						resourcesGiven = True
						currentLives = ctx.eosd.gameController.getLives()

					# Boss Check
					if(noBoss):
						bossHpId = ctx.eosd.hasBossSpawn()
						if(bossHpId != -1):
							noBoss = False
							bossCounter += 1
							# print(f"{ctx.eosd.getBossName(bossCounter)} spawn ({bossHpId})")
							bossCurrentHp = ctx.eosd.gameController.getHpEnemies()[bossHpId]
					else:
						bossTmpHp = ctx.eosd.gameController.getHpEnemies()[bossHpId]
						# If the enemy has more hp than before and it's a huge amount, it mean that the boss has another life bar
						if (bossTmpHp > bossCurrentHp or bossTmpHp <= 0) and bossTmpHp < 3000:
							# print(f"{ctx.eosd.getBossName(bossCounter)} has been defeated")
							if(not ctx.eosd.isCurrentBossDefeated(bossCounter)):
								ctx.eosd.setbossBeaten(bossCounter)
								await ctx.update_locations_checked()
							noBoss = True
							bossHpId = -1
						bossCurrentHp = bossTmpHp

					# Death Check
					# If a death link is sent, we set the flag
					if ctx.pending_death_link and not onGoingDeathLink:
						onGoingDeathLink = True

					# If a death has occured in game
					if currentMisses < ctx.eosd.gameController.getMisses():
						if not onGoingDeathLink: #Check if it's not by a death link in order to send a death link
							await ctx.send_death_link()
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

				elif(ctx.eosd.gameController.getGameMode() == 1):
					# Mode Check
					if(currentMode != 1): # We enter in the menu
						ctx.eosd.gameController.resetHpEnemies()
						currentMode = 1
						bossHpId = -1
						noBoss = True
						resourcesGiven = False
					ctx.eosd.updateStageList()
				else: # If we're not in a level or a menu, we're probably in the Result Screen
					bossCounter = -1

		except Exception as err:  # Process closed?
			print(f"ERROR: {err}")
			disconnected = True
			# attempt to reconnect at the top of the loop
			await asyncio.sleep(0.5)
			continue

def connect_to_t6() -> eosdState:
	eosd = None

	try:
		eosd = eosdState()
	except Exception as err:
		eosd = None

	return eosd

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