from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import T6Location, location_table, get_locations_by_category

class T6RegionData(NamedTuple):
	locations: Optional[List[str]]
	region_exits: Optional[List[str]]

def create_regions(multiworld: MultiWorld, player: int):
	regions: Dict[str, T6RegionData] = {
		"Menu":            T6RegionData(None, ["Reimu", "Marisa"]),
		"Reimu":            T6RegionData(None, ["Reimu - Early", "Reimu - Mid", "Reimu - End"]),
		"Marisa":            T6RegionData(None, ["Marisa - Early", "Marisa - Mid", "Marisa - End"]),
		"Reimu - Early":          T6RegionData(["[Reimu] Rumia - MidBoss",
										"[Reimu] Rumia Defeated",
										"[Reimu] Stage 1 Clear",
										"[Reimu] Daiyousei Defeated",
										"[Reimu] Cirno Defeated",
										"[Reimu] Stage 2 Clear"],   []),
		"Reimu - Mid":          T6RegionData(["[Reimu] Meiling - MidBoss",
										"[Reimu] Meiling Defeated",
										"[Reimu] Stage 3 Clear",
										"[Reimu] Koakuma Defeated",
										"[Reimu] Patchouli Defeated",
										"[Reimu] Stage 4 Clear"],   []),
		"Reimu - End":          T6RegionData(["[Reimu] Sakuya - MidBoss 1",
										"[Reimu] Sakuya Defeated",
										"[Reimu] Stage 5 Clear",
										"[Reimu] Sakuya - MidBoss 2",
										"[Reimu] Remilia Defeated",
										"[Reimu] Stage 6 Clear"],   []),
		"Marisa - Early":         T6RegionData(["[Marisa] Rumia - MidBoss",
										"[Marisa] Rumia Defeated",
										"[Marisa] Stage 1 Clear",
										"[Marisa] Daiyousei Defeated",
										"[Marisa] Cirno Defeated",
										"[Marisa] Stage 2 Clear"],   ["Marisa - Mid"]),
		"Marisa - Mid":         T6RegionData(["[Marisa] Meiling - MidBoss",
										"[Marisa] Meiling Defeated",
										"[Marisa] Stage 3 Clear",
										"[Marisa] Koakuma Defeated",
										"[Marisa] Patchouli Defeated",
										"[Marisa] Stage 4 Clear"],   ["Marisa - End"]),
		"Marisa - End":         T6RegionData(["[Marisa] Sakuya - MidBoss 1",
										"[Marisa] Sakuya Defeated",
										"[Marisa] Stage 5 Clear",
										"[Marisa] Sakuya - MidBoss 2",
										"[Marisa] Remilia Defeated",
										"[Marisa] Stage 6 Clear"],   []),
	}
	# Set up the regions correctly.
	for name, data in regions.items():
		multiworld.regions.append(create_region(multiworld, player, name, data))

def create_region(multiworld: MultiWorld, player: int, name: str, data: T6RegionData):
	region = Region(name, player, multiworld)
	if data.locations:
		for loc_name in data.locations:
			loc_data = location_table.get(loc_name)
			location = T6Location(player, loc_name, loc_data.code if loc_data else None, region)
			region.locations.append(location)

	return region

def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)
    sourceRegion.connect(targetRegion, rule=rule)