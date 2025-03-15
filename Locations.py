from .Variables import *
from BaseClasses import Location

class TLocation(Location):
	game: str = SHORT_NAME

location_id_offset = 0
location_table = {}

for character in ALL_CHARACTERS_LIST:
	level = 0
	for stage in STAGES_LIST:
		level += 1
		for check in stage:
			location_table[f"[{character}] {check}"] = STARTING_ID + location_id_offset
			location_id_offset += 1
		level_name = "Extra" if level == 7 else level
		location_table[f"[{character}] Stage {level_name} Clear"] = STARTING_ID + location_id_offset
		location_id_offset += 1

for difficulty in DIFFICULTY_LIST:
	for character in ALL_CHARACTERS_LIST:
		level = 0
		for stage in STAGES_LIST:
			level += 1
			if level > 6 or (level > 5 and difficulty == "Easy"):
				continue
			for check in stage:
				location_table[f"[{difficulty}][{character}] {check}"] = STARTING_ID + location_id_offset
				location_id_offset += 1