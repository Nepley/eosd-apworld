from BaseClasses import MultiWorld, Region
from .Locations import TLocation, location_table
from .Variables import *

def get_regions(shot_type, difficulty_check, extra):
	regions = {}
	characters = CHARACTERS_LIST if not shot_type else SHOT_TYPE_LIST
	regions["Menu"] = {"locations": None, "exits": characters}
	if difficulty_check not in DIFFICULTY_CHECK:
		for character in characters:
			regions[character] = {"locations": None, "exits": [f"[{character}] Early", f"[{character}] Mid", f"[{character}] Late"]}
			regions[f"[{character}] Early"] = {"locations": None, "exits": [f"[{character}] Stage 1", f"[{character}] Stage 2"]}
			regions[f"[{character}] Mid"] = {"locations": None, "exits": [f"[{character}] Stage 3", f"[{character}] Stage 4"]}
			regions[f"[{character}] Late"] = {"locations": None, "exits": [f"[{character}] Stage 5", f"[{character}] Stage 6"]}

			level = 0
			for stage in STAGES_LIST:
				level += 1
				if level > 6:
					continue
				regions[f"[{character}] Stage {level}"] = {"locations": [f"[{character}] {stage[0]}", f"[{character}] {stage[1]}", f"[{character}] Stage {level} Clear"], "exits": None}

			if extra:
				regions[character]["exits"].append(f"[{character}] Extra")
				regions[f"[{character}] Extra"] = {"locations": [], "exits": [f"[{character}] Stage Extra"]}
				regions[f"[{character}] Stage Extra"] = {"locations": [f"[{character}] Stage Extra Clear"], "exits": None}

				for extra_check in EXTRA_CHECKS:
					regions[f"[{character}] Stage Extra"]["locations"].append(f"[{character}] {extra_check}")
	else:
		for character in characters:
			regions[character] = {"locations": None, "exits": [f"[{character}] Early", f"[{character}] Mid", f"[{character}] Late"]}
			regions[f"[{character}] Early"] = {"locations": None, "exits": [f"[{character}] Stage 1", f"[{character}] Stage 2"]}
			regions[f"[{character}] Mid"] = {"locations": None, "exits": [f"[{character}] Stage 3", f"[{character}] Stage 4"]}
			regions[f"[{character}] Late"] = {"locations": None, "exits": [f"[{character}] Stage 5", f"[{character}] Stage 6"]}

			level = 0
			for stage in STAGES_LIST:
				level += 1
				if level > 6:
					continue
				regions[f"[{character}] Stage {level}"] = {"locations": [f"[{character}] Stage {level} Clear"], "exits": None}

			if extra:
				regions[character]["exits"].append(f"[{character}] Extra")
				regions[f"[{character}] Extra"] = {"locations": None, "exits": [f"[{character}] Stage Extra"]}
				regions[f"[{character}] Stage Extra"] = {"locations": [f"[{character}] Stage Extra Clear"], "exits": None}
				for extra in EXTRA_CHECKS:
					regions[f"[{character}] Stage Extra"]["locations"].append(f"[{character}] {extra}")

		for difficulty in DIFFICULTY_LIST:
			for character in characters:
				regions[f"[{character}] Early"]["exits"].append(f"[{difficulty}][{character}] Stage 1")
				regions[f"[{character}] Early"]["exits"].append(f"[{difficulty}][{character}] Stage 2")
				regions[f"[{character}] Mid"]["exits"].append(f"[{difficulty}][{character}] Stage 3")
				regions[f"[{character}] Mid"]["exits"].append(f"[{difficulty}][{character}] Stage 4")
				regions[f"[{character}] Late"]["exits"].append(f"[{difficulty}][{character}] Stage 5")
				if difficulty != "Easy":
					regions[f"[{character}] Late"]["exits"].append(f"[{difficulty}][{character}] Stage 6")

				level = 0
				for stage in STAGES_LIST:
					level += 1
					if level > 6 or (level > 5 and difficulty == "Easy"):
						continue
					regions[f"[{difficulty}][{character}] Stage {level}"] = {"locations": [f"[{difficulty}][{character}] {stage[0]}", f"[{difficulty}][{character}] {stage[1]}"], "exits": None}

	return regions

def create_regions(multiworld: MultiWorld, player: int, options):
	shot_type = getattr(options, "shot_type")
	difficulty_check = getattr(options, "difficulty_check")
	extra = getattr(options, "extra_stage")

	regions = get_regions(shot_type, difficulty_check, extra)

	# Set up the regions correctly.
	for name, data in regions.items():
		multiworld.regions.append(create_region(multiworld, player, name, data["locations"]))

def create_region(multiworld: MultiWorld, player: int, name: str, locations: list):
	region = Region(name, player, multiworld)
	if locations:
		for location in locations:
			location = TLocation(player, location, location_table[location], region)
			region.locations.append(location)

	return region