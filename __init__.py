from typing import List

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import T6Item, T6ItemData, event_item_table, get_items_by_category, item_table
from .Locations import T6Location, location_table
from .Options import t6_options
from .Regions import create_regions
from .Rules import set_rules
import random

def launch_client():
    """Launch a client instance"""
    from worlds.touhou6.Client import launch
    launch_subprocess(launch, name="Touhou6Client")

components.append(Component(
    "Touhou 6 Client",
    "Touhou6Client",
    func=launch_client,
    component_type=Type.CLIENT
))

class T6World(World):
    """
    Touhou 6
    """
    game = "Touhou 6"
    option_definitions = t6_options
    topology_present = True
    data_version = 4
    required_client_version = (0, 3, 5)

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player]

    def fill_slot_data(self) -> dict:
        return {option_name: self.get_setting(option_name).value for option_name in t6_options}

    def create_items(self):
        item_pool: List[T6Item] = []
        character_list = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        number_placed_item = 0
        mode = getattr(self.options, "mode")
        for name, data in item_table.items():
            quantity = data.max_quantity

            # Categories to be ignored, they will be added in a later stage.
            if data.category == "Filler":
                continue

            if data.category == "Endings":
                continue

            if data.category == "Stages" and mode != 0:
                continue

            if data.category == "[Normal] Items" and mode != 1:
                continue

            if data.category == "Characters":
                character_list.append(name)
                continue

            item_pool += [self.create_item(name) for _ in range(0, quantity)]

        # Selecting starting character
        chosen = random.choice(character_list)
        self.multiworld.push_precollected(self.create_item(chosen))
        character_list.remove(chosen)
        for character in character_list:
            item_pool += [self.create_item(character) for _ in range(0, 1)]

        # Creating and placing Endings
        ending = self.create_item("Ending")
        self.multiworld.get_location("[Reimu] Stage 6 Clear", self.player).place_locked_item(ending)
        self.multiworld.get_location("[Marisa] Stage 6 Clear", self.player).place_locked_item(ending)
        number_placed_item += 2

        # Fill any empty locations with filler items.
        while len(item_pool) + number_placed_item < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        fillers = get_items_by_category("Filler")
        weights = [data.weight for data in fillers.values()]
        return self.multiworld.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

    def create_item(self, name: str) -> T6Item:
        data = item_table[name]
        return T6Item(name, data.classification, data.code, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)