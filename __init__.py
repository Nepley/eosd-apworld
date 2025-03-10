from typing import List
from .Variables import *

from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import TItem, get_items_by_category, item_table
from .Locations import location_table
from .Options import game_options
from .Regions import create_regions
from .Rules import set_rules
import random

def launch_client():
	"""Launch a client instance"""
	from worlds.th06.Client import launch
	launch_subprocess(launch, name="GameClient")

components.append(Component(
	SHORT_NAME+" Client",
	"GameClient",
	func=launch_client,
	component_type=Type.CLIENT
))

class TWorld(World):
	game = DISPLAY_NAME
	option_definitions = game_options
	topology_present = True
	data_version = 4
	required_client_version = (0, 3, 5)

	item_name_to_id = {name: data.code for name, data in item_table.items()}
	location_name_to_id = {name: data.code for name, data in location_table.items()}

	def fill_slot_data(self) -> dict:
		return {option_name: getattr(self.options, option_name).value for option_name in game_options}

	def create_items(self):
		item_pool: List[TItem] = []
		character_list = []
		total_locations = len(self.multiworld.get_unfilled_locations(self.player))
		number_placed_item = 0
		mode = getattr(self.options, "mode")
		extra = getattr(self.options, "extra_stage")
		goal = getattr(self.options, "goal")
		shot_type = getattr(self.options, "shot_type")
		traps = getattr(self.options, "traps")
		max_rank_trap = getattr(self.options, "max_rank_trap")
		power_point_trap = getattr(self.options, "power_point_trap")
		bomb_trap = getattr(self.options, "bomb_trap")
		life_trap = getattr(self.options, "life_trap")
		no_focus_trap = getattr(self.options, "no_focus_trap")
		reverse_movement_trap = getattr(self.options, "reverse_movement_trap")
		aya_speed_trap = getattr(self.options, "aya_speed_trap")
		freeze_trap = getattr(self.options, "freeze_trap")
		power_point_drain_trap = getattr(self.options, "power_point_drain_trap")

		for name, data in item_table.items():
			quantity = data.max_quantity

			# Categories to be ignored, they will be added in a later stage if necessary.
			if data.category == "Filler":
				continue

			# Will be added later
			if data.category == "Traps":
				continue

			# Will be added manually later
			if data.category == "Endings":
				continue

			# Ignored if it's not practice mode
			if data.category == "Stages" and mode != PRACTICE_MODE:
				continue

			# Ignored if it's not normal mode
			if data.category == "[Normal] Items" and mode == PRACTICE_MODE:
				continue

			# Will be added later
			if data.category == "Characters":
				character_list.append(name)
				continue

			# If the extra stage is not active or separated, we don't add the item
			if data.category == "Extra Stage" and extra != 2:
				continue

			# If there is no extra stage or it's separated, we remove one stage in practice mode
			if data.category == "Stages" and mode == PRACTICE_MODE and extra != 1:
				quantity -= 1

			item_pool += [self.create_item(name) for _ in range(0, quantity)]

		# Selecting starting character
		chosen = random.choice(character_list)
		self.multiworld.push_precollected(self.create_item(chosen))
		character_list.remove(chosen)
		for character in character_list:
			item_pool += [self.create_item(character) for _ in range(0, 1)]

		# Creating and placing Endings
		ending_normal_reimu = self.create_item("[Reimu] Ending - Remilia")
		ending_normal_marisa = self.create_item("[Marisa] Ending - Remilia")
		ending_extra_reimu = self.create_item("[Reimu] Ending - Flandre")
		ending_extra_marisa = self.create_item("[Marisa] Ending - Flandre")

		# If we have the extra stage and the extra boss is a potential goal
		if extra and goal != 0:
			if shot_type:
				self.multiworld.get_location("[Reimu A] Stage Extra Clear", self.player).place_locked_item(ending_extra_reimu)
				self.multiworld.get_location("[Reimu B] Stage Extra Clear", self.player).place_locked_item(ending_extra_reimu)
				self.multiworld.get_location("[Marisa A] Stage Extra Clear", self.player).place_locked_item(ending_extra_marisa)
				self.multiworld.get_location("[Marisa B] Stage Extra Clear", self.player).place_locked_item(ending_extra_marisa)
				number_placed_item += 4
			else:
				self.multiworld.get_location("[Reimu] Stage Extra Clear", self.player).place_locked_item(ending_extra_reimu)
				self.multiworld.get_location("[Marisa] Stage Extra Clear", self.player).place_locked_item(ending_extra_marisa)
				number_placed_item += 2

		# If the final boss is a potential goal
		if not extra or goal != 1:
			if shot_type:
				self.multiworld.get_location("[Reimu A] Stage 6 Clear", self.player).place_locked_item(ending_normal_reimu)
				self.multiworld.get_location("[Reimu B] Stage 6 Clear", self.player).place_locked_item(ending_normal_reimu)
				self.multiworld.get_location("[Marisa A] Stage 6 Clear", self.player).place_locked_item(ending_normal_marisa)
				self.multiworld.get_location("[Marisa B] Stage 6 Clear", self.player).place_locked_item(ending_normal_marisa)
				number_placed_item += 4
			else:
				self.multiworld.get_location("[Reimu] Stage 6 Clear", self.player).place_locked_item(ending_normal_reimu)
				self.multiworld.get_location("[Marisa] Stage 6 Clear", self.player).place_locked_item(ending_normal_marisa)
				number_placed_item += 2

		if traps > 0:
			remaining_locations = total_locations - (len(item_pool) + number_placed_item)

			# If we have traps, we count how many of them we need to add
			number_traps = int(remaining_locations * traps / 100)

			if number_traps > 0:
				trapList = random.choices(["Max Rank", "-50% Power Point", "-1 Bomb", "-1 Life", "No Focus", "Reverse Movement", "Aya Speed", "Freeze", "Power Point Drain"], weights=[max_rank_trap, power_point_trap, bomb_trap, life_trap, no_focus_trap, reverse_movement_trap, aya_speed_trap, freeze_trap, power_point_drain_trap], k=number_traps)
				for trap in trapList:
					item_pool.append(self.create_item(trap))

		# Fill any empty locations with filler items.
		while len(item_pool) + number_placed_item < total_locations:
			item_pool.append(self.create_item(self.get_filler_item_name()))

		self.multiworld.itempool += item_pool

	def get_filler_item_name(self) -> str:
		fillers = get_items_by_category("Filler")
		weights = [data.weight for data in fillers.values()]
		return self.multiworld.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

	def create_item(self, name: str) -> TItem:
		data = item_table[name]
		return TItem(name, data.classification, data.code, self.player)

	def set_rules(self):
		set_rules(self.multiworld, self.player)

	def create_regions(self):
		create_regions(self.multiworld, self.player, self.options)