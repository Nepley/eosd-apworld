from typing import Optional
import asyncio
import colorama
import time
import random
import traceback
from .gameHandler import *
from .guardRail import *
from .Tools import *
from .Mapping import *

from CommonClient import (
	CommonContext,
	ClientCommandProcessor,
	get_base_parser,
	logger,
	server_loop,
	gui_enabled,
)

class TouhouClientProcessor(ClientCommandProcessor):
	def _cmd_multiple_difficulty_check(self, active = None):
		"""Toggle the possibility to check multiple difficulty check by doing the highest difficulty
        :param active: If "on" or "true", enable it. If "off" or "false", disable it."""
		changed = False
		if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
			if active is not None:
				if active.lower() in ["on", "true"]:
					self.ctx.check_multiple_difficulty = True
					changed = True
					logger.info("Multiple difficulty check enabled")
				elif active.lower() in ("off", "false"):
					self.ctx.check_multiple_difficulty = False
					changed = True
					logger.info("Multiple difficulty check disabled")
				else:
					logger.error("Invalid argument, use 'on' or 'off'")
			else:
				logger.info(f"Multiple difficulty check is {'enabled' if self.ctx.check_multiple_difficulty else 'disabled'}")
		else:
			logger.error("Multiple difficulty check cannot be changed before connecting to the game and server")

		return changed

	def _cmd_deathlink(self, active = None):
		"""Toggle DeathLink on or off
        :param active: If "on" or "true", enable DeathLink. If "off" or "false", disable DeathLink."""
		changed = False
		if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
			if active is not None:
				if active.lower() in ["on", "true"]:
					if "DeathLink" not in self.ctx.tags:
						self.ctx.tags.add("DeathLink")
						self.ctx.death_link_is_active = True
						changed = True
					logger.info("DeathLink enabled")
				elif active.lower() in ("off", "false"):
					if "DeathLink" in self.ctx.tags:
						self.ctx.tags.remove("DeathLink")
						self.ctx.death_link_is_active = False
						changed = True
					logger.info("DeathLink disabled")
				else:
					logger.error("Invalid argument, use 'on' or 'off'")

				if changed:
					asyncio.create_task(self.ctx.send_msgs([{"cmd": "ConnectUpdate", "tags": self.ctx.tags}]))
			else:
				logger.info(f"DeathLink is {'enabled' if self.ctx.death_link_is_active else 'disabled'}")
		else:
			logger.error("DeathLink cannot be changed before connecting to the game and server")

		return changed

	def _cmd_deathlink_trigger(self, value = None):
		"""Get or Set the trigger for the DeayhLink trigger
        :param value: Possibler values are "life" or "gameover"
		"""
		if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
			if value is not None:
				if value.lower() == "life":
					self.ctx.death_link_trigger = DEATH_LINK_LIFE
					logger.info("DeathLink trigger set to 'Life'")
					return True
				elif value.lower() == "gameover":
					self.ctx.death_link_trigger = DEATH_LINK_GAME_OVER
					logger.info("DeathLink trigger set to 'Game Over'")
					return True
				else:
					logger.error("Invalid argument, use 'life' or 'gameover'")
					return False
			else:
				trigger = "Life" if self.ctx.death_link_trigger == DEATH_LINK_LIFE else "Game Over"
				logger.info(f"Current DeathLink Trigger: {trigger}")
				return True
		else:
			logger.error("DeathLink amnesty cannot be accessed before connecting to the game and server")
			return False

	def _cmd_deathlink_amnesty(self, value = -1):
		"""Get or Set the number of death before sending a DeathLink
        :param value: Set the amnesty to this value, must be between 0 and 10."""
		if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
			if value == -1:
				logger.info(f"Current DeathLink amnesty: {self.ctx.death_link_amnesty}")
				return True
			else:
				try:
					value = int(value)
					if value < 0 or value > 10:
						raise ValueError
					self.ctx.death_link_amnesty = value
					logger.info(f"New DeathLink amnesty: {value}")
					return True
				except ValueError:
					logger.error("Invalid argument, amnesty must be between 0 and 10")
					return False
		else:
			logger.error("DeathLink amnesty cannot be accessed before connecting to the game and server")
			return False

	def _cmd_ringlink(self, active = None):
		"""Toggle RingLink on or off
        :param active: If "on" or "true", enable RingLink. If "off" or "false", disable RingLink."""
		changed = False
		if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
			if active is not None:
				if active.lower() in ("on", "true"):
					if "RingLink" not in self.ctx.tags:
						self.ctx.tags.add("RingLink")
						self.ctx.ring_link_is_active = True
						changed = True
					logger.info("RingLink enabled")
				elif active.lower() in ("off", "false"):
					if "RingLink" in self.ctx.tags:
						self.ctx.tags.remove("RingLink")
						changed = True
						self.ctx.ring_link_is_active = False
					logger.info("RingLink disabled")
				else:
					logger.error("Invalid argument, use 'on' or 'off'")

				if changed:
					asyncio.create_task(self.ctx.send_msgs([{"cmd": "ConnectUpdate", "tags": self.ctx.tags}]))
			else:
				logger.info(f"RingLink is {'enabled' if self.ctx.ring_link_is_active else 'disabled'}")
		else:
			logger.error("RingLink cannot be changed before connecting to the game and server")

		return changed

	def _cmd_limits(self, lives = -1, bombs = -1):
		"""Get or Set the max limits for lives and bombs
        :param lives: New max lives value, must be between 0 and 8.
        :param bombs: New max bombs value, must be between 0 and 8."""
		if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
			if lives == -1 and bombs == -1:
				logger.info(f"Current max lives: {self.ctx.handler.limitLives} / Current max bombs: {self.ctx.handler.limitBombs}")
				return True
			else:
				try:
					lives = int(lives)
					bombs = int(bombs)
					if lives < 0 or lives > 8 or bombs < 0 or bombs > 8:
						raise ValueError
					self.ctx.handler.setLivesLimit(lives)
					self.ctx.handler.setBombsLimit(bombs)
					logger.info(f"New max lives: {lives} / New max bombs: {bombs}")
					return True
				except ValueError:
					logger.error("Invalid argument, limits must be between 0 and 8")
					return False
		else:
			logger.error("Limits cannot be accessed before connecting to the game and server")
			return False

class TouhouContext(CommonContext):
	"""Touhou Game Context"""
	def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
		super().__init__(server_address, password)
		self.game = DISPLAY_NAME
		self.items_handling = 0b111  # Item from starting inventory, own world and other world
		self.command_processor = TouhouClientProcessor
		self.reset()

	def reset(self):
		self.pending_death_link = False

		self.current_power_point = -1
		self.ring_link_id = None
		self.last_power_point = -1

		self.handler = None # gameHandler
		self.inError = False
		self.msgQueue = []

		# List of items/locations
		self.all_location_ids = None
		self.location_name_to_ap_id = None
		self.location_ap_id_to_name = None
		self.item_name_to_ap_id = None
		self.item_ap_id_to_name = None
		self.previous_location_checked = None
		self.location_mapping = None
		self.final_stage_location_ids = None

		self.is_connected = False
		self.last_death_link = 0
		self.last_ring_link = 0
		self.death_link_is_active = False
		self.ring_link_is_active = False
		self.death_link_amnesty = 0
		self.death_link_trigger = DEATH_LINK_LIFE

		# Counter
		self.difficulties = 3
		self.traps = {"power_point_drain": 0, "max_rank": 0, "no_focus": 0, "reverse_control": 0, "aya_speed": 0, "freeze": 0, "bomb": 0, "life": 0, "power_point": 0}
		self.can_trap = True

		self.options = None
		self.check_multiple_difficulty = False
		self.ExtraMenu = False
		self.minimalCursor = 0

	def make_gui(self):
		ui = super().make_gui()
		ui.base_title = f"{DISPLAY_NAME} Client"
		return ui

	async def server_auth(self, password_requested: bool = False):
		if password_requested and not self.password:
			await super().server_auth(password_requested)
		await self.get_username()
		await self.send_connect()

	def on_package(self, cmd: str, args: dict):
		"""
		Manage the package received from the server
		"""
		if cmd == "Connected":
			self.previous_location_checked = args['checked_locations']
			self.all_location_ids = set(args["missing_locations"] + args["checked_locations"])
			self.options = args["slot_data"] # Yaml Options
			self.is_connected = True
			self.check_multiple_difficulty = self.options['check_multiple_difficulty']
			self.location_mapping, self.final_stage_location_ids = getLocationMapping(self.options['shot_type'], self.options['difficulty_check'])

			if self.handler is not None:
				self.handler.reset()

			asyncio.create_task(self.send_msgs([{"cmd": "GetDataPackage", "games": [DISPLAY_NAME]}]))

		if cmd == "ReceivedItems":
			asyncio.create_task(self.give_item(args["items"]))

		elif cmd == "DataPackage":
			if not self.all_location_ids:
				# Connected package not received yet, wait for datapackage request after connected package
				return
			self.location_name_to_ap_id = args["data"]["games"][DISPLAY_NAME]["location_name_to_id"]
			self.location_name_to_ap_id = {
				name: loc_id for name, loc_id in
				self.location_name_to_ap_id.items() if loc_id in self.all_location_ids
			}
			self.location_ap_id_to_name = {v: k for k, v in self.location_name_to_ap_id.items()}
			self.item_name_to_ap_id = args["data"]["games"][DISPLAY_NAME]["item_name_to_id"]
			self.item_ap_id_to_name = {v: k for k, v in self.item_name_to_ap_id.items()}
		elif cmd == "Bounced":
			tags = args.get("tags", [])
			# we can skip checking "DeathLink" in ctx.tags, as otherwise we wouldn't have been send this
			if "DeathLink" in tags and self.last_death_link != args["data"]["time"]:
				self.last_death_link = args["data"]["time"]
				self.on_deathlink(args["data"])
			elif "RingLink" in tags and self.ring_link_id != None:
				self.last_ring_link = args["data"]["time"]
				self.on_ringlink(args["data"])

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
		while not self.client_recieved_initial_server_data() and not self.exit_event.is_set():
			await asyncio.sleep(1)

	async def give_item(self, items):
		"""
		Give an item to the player. This method will always give the oldest
		item that the player has recieved from AP, but not in game yet.

		:NetworkItem item: The item to give to the player
		"""

		gotAnyItem = False

		# We wait for the link to be etablished to the game before giving any items
		while self.handler is None or self.handler.gameController is None:
			await asyncio.sleep(0.5)

		for item in items:
			item_id = item.item - STARTING_ID
			match item_id:
				case 0: # Life
					self.handler.addLife()
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 1: # Bomb
					self.handler.addBomb()
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 2: # Lower Difficulty
					updateDifficulty = self.options['mode'] == NORMAL_DYNAMIC_MODE and not self.options['difficulty_check']
					self.difficulties -= 1
					self.handler.unlockDifficulty(self.difficulties, updateDifficulty)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 3: # 1 Continue
					self.handler.addContinue()
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 100: # Reimu A
					self.handler.unlockCharacter(0, 0)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 101: # Reimu B
					self.handler.unlockCharacter(0, 1)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 102: # Marisa A
					self.handler.unlockCharacter(1, 0)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 103: # Marisa B
					self.handler.unlockCharacter(1, 1)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 200: # Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addStage(isExtraStageLinear)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 201: # [Reimu] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addStage(isExtraStageLinear, REIMU)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 202: # [Marisa] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addStage(isExtraStageLinear, MARISA)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 203: # [Reimu A] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addStage(isExtraStageLinear, REIMU, SHOT_A)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 204: # [Reimu B] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addStage(isExtraStageLinear, REIMU, SHOT_B)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 205: # [Marisa A] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addStage(isExtraStageLinear, MARISA, SHOT_A)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 206: # [Marisa B] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addStage(isExtraStageLinear, MARISA, SHOT_B)
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 207: # 25 Power Point
					self.handler.add25Power()
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 208: # Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart:
						self.handler.unlockExtraStage()
						gotAnyItem = True
						self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 209: # [Reimu] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart:
						self.handler.unlockExtraStage(REIMU)
						gotAnyItem = True
						self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 210: # [Marisa] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart:
						self.handler.unlockExtraStage(MARISA)
						gotAnyItem = True
						self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 211: # [Reimu A] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart:
						self.handler.unlockExtraStage(REIMU, SHOT_A)
						gotAnyItem = True
						self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 212: # [Reimu B] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart:
						self.handler.unlockExtraStage(REIMU, SHOT_B)
						gotAnyItem = True
						self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 213: # [Marisa A] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart:
						self.handler.unlockExtraStage(MARISA, SHOT_A)
						gotAnyItem = True
						self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 214: # [Marisa B] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart:
						self.handler.unlockExtraStage(MARISA, SHOT_B)
						gotAnyItem = True
						self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 300 | 301: # Ending Normal
					character = REIMU if item_id == 300 else MARISA
					self.handler.addEnding(character, ENDING_NORMAL)
					if self.checkVictory():
						await self.send_msgs([{"cmd": 'StatusUpdate', "status": 30}])
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 302 | 303: # Ending Extra
					character = REIMU if item_id == 302 else MARISA
					self.handler.addEnding(character, ENDING_EXTRA)
					if self.checkVictory():
						await self.send_msgs([{"cmd": 'StatusUpdate', "status": 30}])
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 400: # 1 Power Point
					self.handler.add1Power()
					gotAnyItem = True
					self.msgQueue.append({"msg": SHORT_ITEM_NAME[item_id], "color": FLASHING_TEXT})
				case 500: # Max Rank
					self.traps["max_rank"] = 1
				case 501: # -50% Power Point
					self.traps["power_point"] += 1
				case 502: # -1 Bomb
					self.traps["bomb"] += 1
				case 503: # -1 Life
					self.traps["life"] += 1
				case 504: # No Focus
					self.traps["no_focus"] = 1
				case 505: # Reverse Movement
					self.traps["reverse_control"] = 1
				case 506: # Aya Speed
					self.traps["aya_speed"] = 1
				case 507: # Freeze
					self.traps["freeze"] += 1
				case 508: # Power Point Drain
					self.traps["power_point_drain"] = 1
				case _:
					print(f"Unknown Item: {item}")

		if gotAnyItem:
			self.handler.playSound(0x19)

		# Update the stage list
		self.handler.updateStageList()

	async def update_locations_checked(self):
		"""
		Check if any locations has been checked since last called, if a location has ben checked, we send a message and update our list of checked location
		"""
		new_locations = []

		for id, map in self.location_mapping.items():
			# Check if the boss is beaten and the location is not already checked
			if self.handler.isBossBeaten(*map) and id not in self.previous_location_checked:
				# We add it to the list of checked locations
				new_locations.append(id)
				# If we are in normal mode, the extra stage is set to linear and the stage 6 has just been cleared. We unlock it if it's not already.
				if not self.handler.canExtra() and self.options['mode'] in NORMAL_MODE and self.options['extra_stage'] == EXTRA_LINEAR and id in self.final_stage_location_ids:
					self.handler.unlockExtraStage()

		# If we have new locations, we send them to the server and add them to the list of checked locations
		if new_locations:
			self.previous_location_checked = self.previous_location_checked + new_locations
			await self.send_msgs([{"cmd": 'LocationChecks', "locations": new_locations}])

	def on_deathlink(self, data):
		"""
		Method that is called when a death link is recieved.
		"""
		self.pending_death_link = True
		return super().on_deathlink(data)
	
	def on_ringlink(self, data):
		"""
		Method that is called when a ring link is recieved.
		"""
		# We check if we are in a state where we can receive a ring link
		if self.handler.gameController and self.handler.getGameMode() == IN_GAME and not self.inError:
			# We check if it was not sent by us
			if data["source"] != self.ring_link_id:
				self.handler.playSound(0x15) if data["amount"] < 5 else self.handler.playSound(0x1F)
				self.handler.giveCurrentPowerPoint(data["amount"])
				self.last_power_point = self.handler.getCurrentPowerPoint()

	async def send_death_link(self):
		"""
		Send a death link to the server if it's active.
		"""
		if self.death_link_is_active:
			await self.send_death()

	def giveResources(self):
		"""
		Give the resources to the player
		"""
		isNormalMode = self.options['mode'] == NORMAL_DYNAMIC_MODE or self.options['mode'] == NORMAL_STATIC_MODE
		autoDifficulty = not self.options['difficulty_check'] and self.options['mode'] == NORMAL_DYNAMIC_MODE
		return self.handler.initResources(isNormalMode, autoDifficulty)

	def updateStageList(self):
		"""
		Update the stage list in practice mode
		"""
		mode = self.options['mode']

		self.handler.updateStageList(mode == PRACTICE_MODE)
		self.handler.updatePracticeScore(self.location_mapping, self.previous_location_checked)

	def setRingLinkTag(self, active):
		if active:
			self.tags.add("RingLink")
			self.ring_link_is_active = True
		else:
			self.tags.remove("RingLink")
			self.ring_link_is_active = False
		asyncio.create_task(self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}]))

	def checkVictory(self):
		"""
		Check if the player has won the game.
		"""
		goal = self.options['goal']
		type = self.options['ending_required']
		shot_type = self.options['shot_type']
		extra = self.options['extra_stage']

		if not shot_type and type == ALL_SHOT_TYPE_ENDING:
			type = ALL_CHARACTER_ENDING

		normal_victory = True
		extra_victory = True

		if (goal == ENDING_NORMAL or goal == ENDING_BOTH) or extra == NO_EXTRA:
			if type == ONE_ENDING:
				normal_victory = False
				for character in CHARACTERS:
					normal_victory = normal_victory or self.handler.endings[character][ENDING_NORMAL]
			elif type == ALL_CHARACTER_ENDING:
				for character in CHARACTERS:
					normal_victory = normal_victory and self.handler.endings[character][ENDING_NORMAL]
			elif type == ALL_SHOT_TYPE_ENDING:
				for character in CHARACTERS:
					normal_victory = normal_victory and self.handler.endings[character][ENDING_NORMAL] >= len(SHOTS)

		if (goal == ENDING_EXTRA or goal == ENDING_BOTH) and extra != NO_EXTRA:
			if type == ONE_ENDING:
				extra_victory = False
				for character in CHARACTERS:
					extra_victory = extra_victory or self.handler.endings[character][ENDING_EXTRA]
			elif type == ALL_CHARACTER_ENDING:
				for character in CHARACTERS:
					extra_victory = extra_victory and self.handler.endings[character][ENDING_EXTRA]
			elif type == ALL_SHOT_TYPE_ENDING:
				for character in CHARACTERS:
					extra_victory = extra_victory and self.handler.endings[character][ENDING_EXTRA] >= len(SHOTS)

		return normal_victory and extra_victory

	async def main_loop(self):
		"""
		Main loop that handles giving resources and updating locations.
		"""
		try:
			bossPresent = False
			currentMode = 0
			bossCounter = -1
			resourcesGiven = False
			noCheck = True #We start by disabling the checks since we don't know where the player would be when connecting the client
			while not self.exit_event.is_set() and self.handler and not self.inError:
				await asyncio.sleep(0.5)
				gameMode = self.handler.getGameMode()
				inDemo = self.handler.isInDemo()

				# If we're in the demo, we reset the mode so that the variables in the menu can be reset correctly
				if inDemo:
					currentMode = 0
					continue

				# Mode Check
				if(gameMode == IN_GAME and not noCheck):
					# A level has started
					if(currentMode != IN_GAME):
						currentMode = IN_GAME
						bossCounter = -1
						bossPresent = False

						# If the current situation is technically not possible, we lock checks
						if(not self.handler.checkIfCurrentIsPossible((self.options['mode'] in NORMAL_MODE))):
							noCheck = False

					if(not resourcesGiven):
						self.giveResources()
						resourcesGiven = True

					# Boss Check
					if(not bossPresent):
						if(self.handler.isBossPresent()):
							bossPresent = True
							bossCounter += 1
					else:
						if bossPresent:
							# If the boss is defeated, we update the locations
							if(not self.handler.isBossPresent()):
								if(not self.handler.isCurrentBossDefeated(bossCounter%2)):
									#We disable the trap if the stage is ending
									if bossCounter%2 == 1:
										self.can_trap = False
									self.handler.setCurrentStageBossBeaten(bossCounter%2, self.check_multiple_difficulty)
									await self.update_locations_checked()
								bossPresent = False

					# If we're in practice mode and a third boss spawn, it's not normal and we stop sending checks
					if (self.options['mode'] == PRACTICE_MODE and bossCounter > 2):
						noCheck = True
				elif(gameMode == IN_MENU):
					# We enter in the menu
					if(currentMode != IN_MENU):
						self.handler.resetStageVariables()
						currentMode = IN_MENU
						resourcesGiven = False
						noCheck = False # We enable the checks once we're in the menu
		except Exception as e:
			logger.error(f"Main ERROR:")
			logger.error(traceback.format_exc())
			self.inError = True

	async def menu_loop(self):
		"""
		Loop that handles the characters lock and difficulty lock, depending on the menu.
		"""
		try:
			mode = self.options['mode']
			exclude_lunatic = self.options['exclude_lunatic']

			if exclude_lunatic:
				self.difficulties -= 1
				self.handler.unlockDifficulty(self.difficulties)

			while not self.exit_event.is_set() and self.handler and not self.inError:
				if self.handler.getGameMode() == IN_MENU:
					menu = self.handler.getMenu()
					# We check where we are in the menu in order to determine how we lock/unlock the characters
					if menu in [0, 18]  or self.handler.getDifficulty() == EXTRA:
						self.ExtraMenu = True
					elif menu in [6] or self.handler.getDifficulty() < EXTRA:
						self.ExtraMenu = False

					# If we're in the difficulty menu, we put the minimal value to the lowest difficulty
					if menu == 6:
						self.minimalCursor = -1
					# If we're in the main menu and we play in practice mode, we lock the access to normal mode
					elif menu == 0 and mode == PRACTICE_MODE:
						# 1 If we have access to the extra stage, 2 if we don't
						self.minimalCursor = 1 if self.handler.canExtra() else 2
					else:
						self.minimalCursor = 0

					self.handler.updateExtraUnlock(not self.ExtraMenu)
					self.handler.updateCursor(self.minimalCursor)
					self.updateStageList()
				await asyncio.sleep(0.1)
		except Exception as e:
			logger.error(f"Menu ERROR: {e}")
			logger.error(traceback.format_exc())
			self.inError = True

	async def trap_loop(self):
		"""
		Loop that handles traps.
		"""

		try:
			PowerPointDrain = False
			MaxRank = False
			NoFocus = False
			ReverseControls = False
			AyaSpeed = False
			Freeze = False
			InLevel = False
			TransitionTimer = 2
			counterTransition = 0
			freezeTimer = 2
			counterFreeze = 0
			while not self.exit_event.is_set() and self.handler and not self.inError:
				await asyncio.sleep(1)
				if self.handler.getGameMode() == IN_GAME and not self.handler.isInDemo():
					# If we enter a level and some time has passed, we activate the traps
					if not InLevel and counterTransition < TransitionTimer:
						counterTransition += 1
					elif not InLevel:
						InLevel = True
						counterTransition = 0

					if InLevel and self.can_trap:
						# Checks if we need to add a new trap
						if not PowerPointDrain and self.traps['power_point_drain'] > 0:
							PowerPointDrain = True
							self.traps['power_point_drain'] -= 1
							self.msgQueue.append({"msg": SHORT_TRAP_NAME['power_point_drain'], "color": RED_TEXT})
							self.handler.playSound(0x1F)
						elif not MaxRank and self.traps['max_rank'] > 0:
							MaxRank = True
							self.traps['max_rank'] -= 1
							self.msgQueue.append({"msg": SHORT_TRAP_NAME['max_rank'], "color": RED_TEXT})
							self.handler.playSound(0x10)
							self.handler.maxRank()
						elif not ReverseControls and self.traps['reverse_control'] > 0:
							ReverseControls = True
							self.traps['reverse_control'] -= 1
							self.msgQueue.append({"msg": SHORT_TRAP_NAME['reverse_control'], "color": RED_TEXT})
							self.handler.playSound(0x0D)
							self.handler.reverseControls()
						elif not AyaSpeed and self.traps['aya_speed'] > 0:
							AyaSpeed = True
							self.traps['aya_speed'] -= 1
							self.msgQueue.append({"msg": SHORT_TRAP_NAME['aya_speed'], "color": RED_TEXT})
							self.handler.playSound(0x0D)
							self.handler.ayaSpeed()
						elif not NoFocus and self.traps['no_focus'] > 0:
							NoFocus = True
							self.traps['no_focus'] -= 1
							self.msgQueue.append({"msg": SHORT_TRAP_NAME['no_focus'], "color": RED_TEXT})
							self.handler.playSound(0x0D)
							self.handler.noFocus()
						elif not Freeze and self.traps['freeze'] > 0:
							Freeze = True
							self.traps['freeze'] -= 1
							self.msgQueue.append({"msg": SHORT_TRAP_NAME['freeze'], "color": RED_TEXT})
							self.handler.playSound(0x0D)
							self.handler.freeze()
						elif self.traps['bomb'] > 0:
							self.traps['bomb'] -= 1
							self.msgQueue.append({"msg": SHORT_TRAP_NAME['bomb'], "color": RED_TEXT})
							self.handler.playSound(0x0E)
							self.handler.loseBomb()
						elif self.traps['life'] > 0:
							self.traps['life'] -= 1
							self.msgQueue.append({"msg": SHORT_TRAP_NAME['life'], "color": RED_TEXT})
							self.handler.playSound(0x04)
							self.handler.loseLife()
						elif self.traps['power_point'] > 0:
							self.traps['power_point'] -= 1
							self.msgQueue.append({"msg": SHORT_TRAP_NAME['power_point'], "color": RED_TEXT})
							self.handler.playSound(0x1F)
							self.handler.halfPowerPoint()

						# Power Point Drain apply each loop until the player dies or the level is exited
						if PowerPointDrain:
							self.handler.powerPointDrain()

						# Freeze apply each loop until the timer is done
						if Freeze:
							if counterFreeze < freezeTimer:
								counterFreeze += 1
							else:
								Freeze = False
								counterFreeze = 0
								self.handler.resetSpeed()
				else:
					InLevel = False
					PowerPointDrain = False
					MaxRank = False
					NoFocus = False
					ReverseControls = False
					AyaSpeed = False
					Freeze = False
					counterTransition = 0
					counterFreeze = 0
					self.can_trap = True
		except Exception as e:
			logger.error(f"Trap ERROR: {e}")
			logger.error(traceback.format_exc())
			self.inError = True

	async def death_link_loop(self):
		"""
		Loop that handles death link.
		"""
		try:
			self.pending_death_link = False
			onGoingDeathLink = False
			inLevel = False
			currentMisses = 0
			currentLives = 0
			hasDied = False
			nb_death = 0

			while not self.exit_event.is_set() and self.handler and not self.inError:
				if(self.death_link_is_active):
					await asyncio.sleep(0.5)
				else:
					await asyncio.sleep(2)
					inLevel = False
					continue
				if self.handler.getGameMode() == IN_GAME:
					# If we enter a level, we set the variables
					if not inLevel:
						inLevel = True
						currentMisses = self.handler.getMisses()
						currentLives = self.handler.getCurrentLives()
						onGoingDeathLink = False
						self.pending_death_link = False
						deathCounter = 0
						hasDied = False

					# If a death link is sent, we set the flag
					if self.pending_death_link and not onGoingDeathLink:
						onGoingDeathLink = True

					# If a misses has been added, that mean the player has been killed and we check if it was because of the death link
					# (Receiving a death link is checked by misses as it's more reliable and the player could have deathbomb the death link)
					if currentMisses < self.handler.getMisses():
						# If the player is killed by a death link, we tell the loop it's done
						if onGoingDeathLink:
							onGoingDeathLink = False
							self.pending_death_link = False
						else:
							hasDied = True
							deathCounter = 3

						currentMisses += 1
					# If no death has occured but a death link is pending, we try to kill the player
					elif self.pending_death_link:
						await self.handler.killPlayer()

					# If the number of lives has changed
					# (Sending a death link is done by checking lives in order to not send one when deathbombing)
					if self.handler.getCurrentLives() != currentLives:
						# If it's lower and there is no death link on going, then a death has occured and we send a death link
						if self.handler.getCurrentLives() < currentLives and hasDied:
							if self.death_link_trigger == DEATH_LINK_LIFE or (self.death_link_trigger == DEATH_LINK_GAME_OVER and self.handler.getCurrentLives() == 0):
								nb_death += 1
								if nb_death >= self.death_link_amnesty:
									await self.send_death_link()
									nb_death = 0
								else:
									logger.info(f"DeathLink: {nb_death}/{self.death_link_amnesty}")
							hasDied = False

						currentLives = self.handler.getCurrentLives()
					elif hasDied: # If the player has deathbomb
						if deathCounter > 0:
							deathCounter -= 1

						if deathCounter <= 0:
							hasDied = False
				else:
					inLevel = False
					if hasDied:
						nb_death += 1
						if nb_death >= self.death_link_amnesty:
							await self.send_death_link()
							nb_death = 0
						else:
							logger.info(f"DeathLink: {nb_death}/{self.death_link_amnesty}")
						hasDied = False
		except Exception as e:
			logger.error(f"DeathLink ERROR: {e}")
			logger.error(traceback.format_exc())
			self.inError = True

	async def message_loop(self):
		"""
		Loop that handles displaying message
		"""
		try:
			while not self.exit_event.is_set() and self.handler and not self.inError:
				if self.msgQueue != []:
					msg = self.msgQueue[0]
					self.msgQueue.pop(0)
					task = asyncio.create_task(self.handler.displayMessage(msg['msg'], msg['color']))
					await asyncio.wait([task])
				else:
					await asyncio.sleep(0.1)
		except Exception as e:
			logger.error(f"Message ERROR: {e}")
			logger.error(traceback.format_exc())
			self.inError = True

	async def ring_link_loop(self):
		"""
		Loop that handles Ring Link
		"""
		try:
			self.last_power_point = -1
			self.ring_link_id = random.randint(0, 999999)
			self.timer = 0.5

			while not self.exit_event.is_set() and self.handler and not self.inError:
				if(self.ring_link_is_active):
					await asyncio.sleep(self.timer)
				else:
					await asyncio.sleep(2)
					self.last_power_point = -1
					continue
				if self.handler.getGameMode() == IN_GAME:
					# We wait a little before sending ring link
					self.timer = 0.1
					curent_power = self.handler.getCurrentPowerPoint()

					# If last_power_point is -1, that mean it's the first loop, so we just wait a little and then set it
					if self.last_power_point == -1:
						await asyncio.sleep(1)
						self.last_power_point = curent_power
						continue

					# If the power point has changed, we send a ring link
					if self.last_power_point != curent_power:
						diff_power = curent_power-self.last_power_point
						self.last_power_point = curent_power
						asyncio.create_task(self.send_msgs([{"cmd": "Bounce", "tags": ["RingLink"], "data": {"amount": diff_power, "source": self.ring_link_id, "time": time.time()}}]))
				else:
					self.last_power_point = -1
					self.timer = 0.5
		except Exception as e:
			logger.error(f"RingLink ERROR: {e}")
			logger.error(traceback.format_exc())
			self.inError = True

	async def guard_rail_loop(self):
		"""
		Loop that handles the guard rail
		"""
		in_menu = False
		guard_rail = GuardRail(self.handler.gameController, self.handler, self.options)
		while not self.exit_event.is_set() and self.handler and not self.inError:
			try:
				await asyncio.sleep(5)
				result = guard_rail.check_memory_addresses()
				if result["error"]:
					logger.error(f"Memory ERROR: {result['message']}")

				if self.handler.getGameMode() != IN_GAME:
					if not in_menu:
						await asyncio.sleep(2)  # Give some time for the menu to fully load
						in_menu = True

					result = guard_rail.check_cursor_state()
					if result["error"]:
						logger.error(f"Cursor State ERROR: {result['message']}")

					result = guard_rail.check_menu_lock()
					if result["error"]:
						logger.error(f"Menu Lock ERROR: {result['message']}")
				else:
					in_menu = False
			except Exception as e:
				logger.error(f"GuardRail ERROR: {e}")
				logger.error(traceback.format_exc())
				self.inError = True

	async def connect_to_game(self):
		"""
		Connect the client to the game process
		"""
		self.handler = None

		while not self.handler:
			pid = await find_process()
			if pid:
				self.handler = gameHandler(pid)
			await asyncio.sleep(2)

	async def reconnect_to_game(self):
		"""
		Reconnect to client to the game process without resetting everything
		"""

		while not self.handler.gameController:
			pid = await find_process()
			if pid:
				self.handler.reconnect(pid)
			await asyncio.sleep(2)

async def game_watcher(ctx: TouhouContext):
	"""
	Client loop, watching the game process.
	Start the different loops once connected that will handle the game.
	It will also attempt to reconnect if the connection to the game is lost.

	:TouhouContext ctx: The client context instance.
	"""

	await ctx.wait_for_initial_connection_info()

	while not ctx.exit_event.is_set():
		if not ctx.server:
			# client disconnected from server
			ctx.reset()
			await ctx.wait_for_initial_connection_info()

		# First connection
		if ctx.handler is None and not ctx.inError:
			logger.info(f"Waiting for connection to {SHORT_NAME}...")
			asyncio.create_task(ctx.connect_to_game())
			while(ctx.handler is None and not ctx.exit_event.is_set()):
				await asyncio.sleep(1)

		# Connection following an error
		if ctx.inError:
			logger.info(f"Connection lost. Waiting for connection to {SHORT_NAME}...")
			ctx.handler.gameController = None
			asyncio.create_task(ctx.reconnect_to_game())
			await asyncio.sleep(1)
			while(ctx.handler.gameController is None and not ctx.exit_event.is_set()):
				await asyncio.sleep(1)

		if ctx.handler and ctx.handler.gameController:
			ctx.inError = False
			logger.info(f"{SHORT_NAME} process found. Starting loop...")

			# We start all the diffrent loops
			loops = []
			loops.append(asyncio.create_task(ctx.main_loop()))
			loops.append(asyncio.create_task(ctx.menu_loop()))
			loops.append(asyncio.create_task(ctx.trap_loop()))
			loops.append(asyncio.create_task(ctx.message_loop()))
			loops.append(asyncio.create_task(ctx.guard_rail_loop()))
			loops.append(asyncio.create_task(ctx.death_link_loop()))
			loops.append(asyncio.create_task(ctx.ring_link_loop()))

			# We update the locations checked if there was any location that was already checked before the connection
			await ctx.update_locations_checked()
			ctx.updateStageList()

			# Activating Death Link / Ring Link if needed
			if ctx.options['death_link']:
				await ctx.update_death_link(True)
				ctx.death_link_is_active = True

			if ctx.options['death_link_amnesty']:
				ctx.death_link_amnesty = ctx.options['death_link_amnesty']

			if ctx.options['death_link_trigger']:
				ctx.death_link_trigger = ctx.options['death_link_trigger']

			if ctx.options['ring_link']:
				ctx.setRingLinkTag(True)

			# We set the limits for lives and bombs
			ctx.handler.setLivesLimit(ctx.options['limit_lives'])
			ctx.handler.setBombsLimit(ctx.options['limit_bombs'])

			# Infinite loop while there is no error. If there is an error, we exit this loop in order to restart the connection
			while not ctx.exit_event.is_set() and ctx.server and not ctx.inError:
				await asyncio.sleep(1)

			# If we're here, we stop all the loops
			for loop in loops:
				try:
					loop.cancel()
				except:
					pass

def launch():
	"""
	Launch a client instance (wrapper / args parser)
	"""
	async def main(args):
		"""
		Launch a client instance (threaded)
		"""
		ctx = TouhouContext(args.connect, args.password)
		ctx.server_task = asyncio.create_task(server_loop(ctx))
		if gui_enabled:
			ctx.run_gui()
		ctx.run_cli()
		watcher = asyncio.create_task(
			game_watcher(ctx),
			name="GameProgressionWatcher"
		)
		await ctx.exit_event.wait()
		await watcher
		await ctx.shutdown()

	parser = get_base_parser(description=SHORT_NAME+" Client")
	args, _ = parser.parse_known_args()

	colorama.init()
	asyncio.run(main(args))
	colorama.deinit()