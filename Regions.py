from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import T6Location, location_table, get_locations_by_category
from .Options import t6_options

class T6RegionData(NamedTuple):
	locations: Optional[List[str]]
	region_exits: Optional[List[str]]

def create_regions(multiworld: MultiWorld, player: int, options):
	regionsNoShotType: Dict[str, T6RegionData] = {
		"Menu":            	T6RegionData(None, ["Reimu", "Marisa"]),
		"Reimu":            T6RegionData(None, ["Reimu - Early", "Reimu - Mid", "Reimu - End", "Reimu - Extra"]),
		"Marisa":           T6RegionData(None, ["Marisa - Early", "Marisa - Mid", "Marisa - End", "Marisa - Extra"]),
		"Reimu - Early":    T6RegionData(["[Reimu] Rumia - MidBoss",
										"[Reimu] Rumia Defeated",
										"[Reimu] Stage 1 Clear",
										"[Reimu] Daiyousei Defeated",
										"[Reimu] Cirno Defeated",
										"[Reimu] Stage 2 Clear"],   []),
		"Reimu - Mid":      T6RegionData(["[Reimu] Meiling - MidBoss",
										"[Reimu] Meiling Defeated",
										"[Reimu] Stage 3 Clear",
										"[Reimu] Koakuma Defeated",
										"[Reimu] Patchouli Defeated",
										"[Reimu] Stage 4 Clear"],   []),
		"Reimu - End":      T6RegionData(["[Reimu] Sakuya - MidBoss 1",
										"[Reimu] Sakuya Defeated",
										"[Reimu] Stage 5 Clear",
										"[Reimu] Sakuya - MidBoss 2",
										"[Reimu] Remilia Defeated",
										"[Reimu] Stage 6 Clear"],   []),
		"Reimu - Extra":    T6RegionData(["[Reimu] Patchouli - MidBoss",
										"[Reimu] Flandre Defeated",
										"[Reimu] Stage Extra Clear"],   []),
		"Marisa - Early":   T6RegionData(["[Marisa] Rumia - MidBoss",
										"[Marisa] Rumia Defeated",
										"[Marisa] Stage 1 Clear",
										"[Marisa] Daiyousei Defeated",
										"[Marisa] Cirno Defeated",
										"[Marisa] Stage 2 Clear"],   ["Marisa - Mid"]),
		"Marisa - Mid":     T6RegionData(["[Marisa] Meiling - MidBoss",
										"[Marisa] Meiling Defeated",
										"[Marisa] Stage 3 Clear",
										"[Marisa] Koakuma Defeated",
										"[Marisa] Patchouli Defeated",
										"[Marisa] Stage 4 Clear"],   ["Marisa - End"]),
		"Marisa - End":     T6RegionData(["[Marisa] Sakuya - MidBoss 1",
										"[Marisa] Sakuya Defeated",
										"[Marisa] Stage 5 Clear",
										"[Marisa] Sakuya - MidBoss 2",
										"[Marisa] Remilia Defeated",
										"[Marisa] Stage 6 Clear"],   []),
		"Marisa - Extra":   T6RegionData(["[Marisa] Patchouli - MidBoss",
										"[Marisa] Flandre Defeated",
										"[Marisa] Stage Extra Clear"],   []),
	}

	regionsShotType: Dict[str, T6RegionData] = {
		"Menu":            		T6RegionData(None, ["Reimu - A", "Marisa - A", "Reimu - B", "Marisa - B"]),
		"Reimu - A":            T6RegionData(None, ["Reimu - A - Early", "Reimu - A - Mid", "Reimu - A - End", "Reimu - A - Extra"]),
		"Reimu - B":            T6RegionData(None, ["Reimu - B - Early", "Reimu - B - Mid", "Reimu - B - End", "Reimu - B - Extra"]),
		"Marisa - A":           T6RegionData(None, ["Marisa - A - Early", "Marisa - A - Mid", "Marisa - A - End", "Marisa - A - Extra"]),
		"Marisa - B":           T6RegionData(None, ["Marisa - B - Early", "Marisa - B - Mid", "Marisa - B - End", "Marisa - B - Extra"]),

		"Reimu - A - Early":   T6RegionData(["[Reimu A] Rumia - MidBoss",
										"[Reimu A] Rumia Defeated",
										"[Reimu A] Stage 1 Clear",
										"[Reimu A] Daiyousei Defeated",
										"[Reimu A] Cirno Defeated",
										"[Reimu A] Stage 2 Clear"],   []),
		"Reimu - A - Mid":     T6RegionData(["[Reimu A] Meiling - MidBoss",
										"[Reimu A] Meiling Defeated",
										"[Reimu A] Stage 3 Clear",
										"[Reimu A] Koakuma Defeated",
										"[Reimu A] Patchouli Defeated",
										"[Reimu A] Stage 4 Clear"],   []),
		"Reimu - A - End":     T6RegionData(["[Reimu A] Sakuya - MidBoss 1",
										"[Reimu A] Sakuya Defeated",
										"[Reimu A] Stage 5 Clear",
										"[Reimu A] Sakuya - MidBoss 2",
										"[Reimu A] Remilia Defeated",
										"[Reimu A] Stage 6 Clear"],   []),
		"Reimu - A - Extra":   T6RegionData(["[Reimu A] Patchouli - MidBoss",
										"[Reimu A] Flandre Defeated",
										"[Reimu A] Stage Extra Clear"],   []),

		"Reimu - B - Early":   T6RegionData(["[Reimu B] Rumia - MidBoss",
										"[Reimu B] Rumia Defeated",
										"[Reimu B] Stage 1 Clear",
										"[Reimu B] Daiyousei Defeated",
										"[Reimu B] Cirno Defeated",
										"[Reimu B] Stage 2 Clear"],   []),
		"Reimu - B - Mid":     T6RegionData(["[Reimu B] Meiling - MidBoss",
										"[Reimu B] Meiling Defeated",
										"[Reimu B] Stage 3 Clear",
										"[Reimu B] Koakuma Defeated",
										"[Reimu B] Patchouli Defeated",
										"[Reimu B] Stage 4 Clear"],   []),
		"Reimu - B - End":     T6RegionData(["[Reimu B] Sakuya - MidBoss 1",
										"[Reimu B] Sakuya Defeated",
										"[Reimu B] Stage 5 Clear",
										"[Reimu B] Sakuya - MidBoss 2",
										"[Reimu B] Remilia Defeated",
										"[Reimu B] Stage 6 Clear"],   []),
		"Reimu - B - Extra":   T6RegionData(["[Reimu B] Patchouli - MidBoss",
										"[Reimu B] Flandre Defeated",
										"[Reimu B] Stage Extra Clear"],   []),

		"Marisa - A - Early":  T6RegionData(["[Marisa A] Rumia - MidBoss",
										"[Marisa A] Rumia Defeated",
										"[Marisa A] Stage 1 Clear",
										"[Marisa A] Daiyousei Defeated",
										"[Marisa A] Cirno Defeated",
										"[Marisa A] Stage 2 Clear"],   []),
		"Marisa - A - Mid":    T6RegionData(["[Marisa A] Meiling - MidBoss",
										"[Marisa A] Meiling Defeated",
										"[Marisa A] Stage 3 Clear",
										"[Marisa A] Koakuma Defeated",
										"[Marisa A] Patchouli Defeated",
										"[Marisa A] Stage 4 Clear"],   []),
		"Marisa - A - End":    T6RegionData(["[Marisa A] Sakuya - MidBoss 1",
										"[Marisa A] Sakuya Defeated",
										"[Marisa A] Stage 5 Clear",
										"[Marisa A] Sakuya - MidBoss 2",
										"[Marisa A] Remilia Defeated",
										"[Marisa A] Stage 6 Clear"],   []),
		"Marisa - A - Extra":  T6RegionData(["[Marisa A] Patchouli - MidBoss",
										"[Marisa A] Flandre Defeated",
										"[Marisa A] Stage Extra Clear"],   []),

		"Marisa - B - Early":  T6RegionData(["[Marisa B] Rumia - MidBoss",
										"[Marisa B] Rumia Defeated",
										"[Marisa B] Stage 1 Clear",
										"[Marisa B] Daiyousei Defeated",
										"[Marisa B] Cirno Defeated",
										"[Marisa B] Stage 2 Clear"],   []),
		"Marisa - B - Mid":    T6RegionData(["[Marisa B] Meiling - MidBoss",
										"[Marisa B] Meiling Defeated",
										"[Marisa B] Stage 3 Clear",
										"[Marisa B] Koakuma Defeated",
										"[Marisa B] Patchouli Defeated",
										"[Marisa B] Stage 4 Clear"],   []),
		"Marisa - B - End":    T6RegionData(["[Marisa B] Sakuya - MidBoss 1",
										"[Marisa B] Sakuya Defeated",
										"[Marisa B] Stage 5 Clear",
										"[Marisa B] Sakuya - MidBoss 2",
										"[Marisa B] Remilia Defeated",
										"[Marisa B] Stage 6 Clear"],   []),
		"Marisa - B - Extra":  T6RegionData(["[Marisa B] Patchouli - MidBoss",
										"[Marisa B] Flandre Defeated",
										"[Marisa B] Stage Extra Clear"],   []),
	}

	regionsNoShotTypeWdifficutly: Dict[str, T6RegionData] = {
		"Menu":            	T6RegionData(None, ["Reimu", "Marisa"]),
		"Reimu":            T6RegionData(None, ["Reimu - Early", "Reimu - Mid", "Reimu - End",
										  		"Easy - Reimu - Early", "Easy - Reimu - Mid", "Easy - Reimu - End",
										  		"Normal - Reimu - Early", "Normal - Reimu - Mid", "Normal - Reimu - End",
												"Hard - Reimu - Early", "Hard - Reimu - Mid", "Hard - Reimu - End",
												"Lunatic - Reimu - Early", "Lunatic - Reimu - Mid", "Lunatic - Reimu - End",
										  		"Reimu - Extra"]),
		"Marisa":           T6RegionData(None, ["Marisa - Early", "Marisa - Mid", "Marisa - End",
												"Easy - Marisa - Early", "Easy - Marisa - Mid", "Easy - Marisa - End",
												"Normal - Marisa - Early", "Normal - Marisa - Mid", "Normal - Marisa - End",
												"Hard - Marisa - Early", "Hard - Marisa - Mid", "Hard - Marisa - End",
												"Lunatic - Marisa - Early", "Lunatic - Marisa - Mid", "Lunatic - Marisa - End",
										  		"Marisa - Extra"]),
		"Reimu - Early":  T6RegionData(["[Reimu] Stage 1 Clear",
										"[Reimu] Stage 2 Clear"],   []),
		"Reimu - Mid":    T6RegionData(["[Reimu] Stage 3 Clear",
										"[Reimu] Stage 4 Clear"],   []),
		"Reimu - End":    T6RegionData(["[Reimu] Stage 5 Clear",
										"[Reimu] Stage 6 Clear"],   []),
		"Easy - Reimu - Early":    T6RegionData(["[Easy][Reimu] Rumia - MidBoss",
										"[Easy][Reimu] Rumia Defeated",
										"[Easy][Reimu] Daiyousei Defeated",
										"[Easy][Reimu] Cirno Defeated"],   []),
		"Easy - Reimu - Mid":      T6RegionData(["[Easy][Reimu] Meiling - MidBoss",
										"[Easy][Reimu] Meiling Defeated",
										"[Easy][Reimu] Koakuma Defeated",
										"[Easy][Reimu] Patchouli Defeated"],   []),
		"Easy - Reimu - End":      T6RegionData(["[Easy][Reimu] Sakuya - MidBoss 1",
										"[Easy][Reimu] Sakuya Defeated"],   []),
		"Normal - Reimu - Early":    T6RegionData(["[Normal][Reimu] Rumia - MidBoss",
										"[Normal][Reimu] Rumia Defeated",
										"[Normal][Reimu] Daiyousei Defeated",
										"[Normal][Reimu] Cirno Defeated"],   []),
		"Normal - Reimu - Mid":      T6RegionData(["[Normal][Reimu] Meiling - MidBoss",
										"[Normal][Reimu] Meiling Defeated",
										"[Normal][Reimu] Koakuma Defeated",
										"[Normal][Reimu] Patchouli Defeated"],   []),
		"Normal - Reimu - End":      T6RegionData(["[Normal][Reimu] Sakuya - MidBoss 1",
										"[Normal][Reimu] Sakuya Defeated",
										"[Normal][Reimu] Sakuya - MidBoss 2",
										"[Normal][Reimu] Remilia Defeated"],   []),
		"Hard - Reimu - Early":    T6RegionData(["[Hard][Reimu] Rumia - MidBoss",
										"[Hard][Reimu] Rumia Defeated",
										"[Hard][Reimu] Daiyousei Defeated",
										"[Hard][Reimu] Cirno Defeated"],   []),
		"Hard - Reimu - Mid":      T6RegionData(["[Hard][Reimu] Meiling - MidBoss",
										"[Hard][Reimu] Meiling Defeated",
										"[Hard][Reimu] Koakuma Defeated",
										"[Hard][Reimu] Patchouli Defeated"],   []),
		"Hard - Reimu - End":      T6RegionData(["[Hard][Reimu] Sakuya - MidBoss 1",
										"[Hard][Reimu] Sakuya Defeated",
										"[Hard][Reimu] Sakuya - MidBoss 2",
										"[Hard][Reimu] Remilia Defeated"],   []),
		"Lunatic - Reimu - Early":    T6RegionData(["[Lunatic][Reimu] Rumia - MidBoss",
										"[Lunatic][Reimu] Rumia Defeated",
										"[Lunatic][Reimu] Daiyousei Defeated",
										"[Lunatic][Reimu] Cirno Defeated"],   []),
		"Lunatic - Reimu - Mid":      T6RegionData(["[Lunatic][Reimu] Meiling - MidBoss",
										"[Lunatic][Reimu] Meiling Defeated",
										"[Lunatic][Reimu] Koakuma Defeated",
										"[Lunatic][Reimu] Patchouli Defeated"],   []),
		"Lunatic - Reimu - End":      T6RegionData(["[Lunatic][Reimu] Sakuya - MidBoss 1",
										"[Lunatic][Reimu] Sakuya Defeated",
										"[Lunatic][Reimu] Sakuya - MidBoss 2",
										"[Lunatic][Reimu] Remilia Defeated"],   []),
		"Reimu - Extra":    T6RegionData(["[Reimu] Patchouli - MidBoss",
										"[Reimu] Flandre Defeated",
										"[Reimu] Stage Extra Clear"],   []),

		"Marisa - Early":  T6RegionData(["[Marisa] Stage 1 Clear",
										"[Marisa] Stage 2 Clear"],   []),
		"Marisa - Mid":    T6RegionData(["[Marisa] Stage 3 Clear",
										"[Marisa] Stage 4 Clear"],   []),
		"Marisa - End":    T6RegionData(["[Marisa] Stage 5 Clear",
										"[Marisa] Stage 6 Clear"],   []),
		"Easy - Marisa - Early":   T6RegionData(["[Easy][Marisa] Rumia - MidBoss",
										"[Easy][Marisa] Rumia Defeated",
										"[Easy][Marisa] Daiyousei Defeated",
										"[Easy][Marisa] Cirno Defeated"],   ["Marisa - Mid"]),
		"Easy - Marisa - Mid":     T6RegionData(["[Easy][Marisa] Meiling - MidBoss",
										"[Easy][Marisa] Meiling Defeated",
										"[Easy][Marisa] Koakuma Defeated",
										"[Easy][Marisa] Patchouli Defeated"],   ["Marisa - End"]),
		"Easy - Marisa - End":     T6RegionData(["[Easy][Marisa] Sakuya - MidBoss 1",
										"[Easy][Marisa] Sakuya Defeated"],   []),
		"Normal - Marisa - Early":   T6RegionData(["[Normal][Marisa] Rumia - MidBoss",
										"[Normal][Marisa] Rumia Defeated",
										"[Normal][Marisa] Daiyousei Defeated",
										"[Normal][Marisa] Cirno Defeated"],   ["Marisa - Mid"]),
		"Normal - Marisa - Mid":     T6RegionData(["[Normal][Marisa] Meiling - MidBoss",
										"[Normal][Marisa] Meiling Defeated",
										"[Normal][Marisa] Koakuma Defeated",
										"[Normal][Marisa] Patchouli Defeated"],   ["Marisa - End"]),
		"Normal - Marisa - End":     T6RegionData(["[Normal][Marisa] Sakuya - MidBoss 1",
										"[Normal][Marisa] Sakuya Defeated",
										"[Normal][Marisa] Sakuya - MidBoss 2",
										"[Normal][Marisa] Remilia Defeated"],   []),
		"Hard - Marisa - Early":   T6RegionData(["[Hard][Marisa] Rumia - MidBoss",
										"[Hard][Marisa] Rumia Defeated",
										"[Hard][Marisa] Daiyousei Defeated",
										"[Hard][Marisa] Cirno Defeated"],   ["Marisa - Mid"]),
		"Hard - Marisa - Mid":     T6RegionData(["[Hard][Marisa] Meiling - MidBoss",
										"[Hard][Marisa] Meiling Defeated",
										"[Hard][Marisa] Koakuma Defeated",
										"[Hard][Marisa] Patchouli Defeated"],   ["Marisa - End"]),
		"Hard - Marisa - End":     T6RegionData(["[Hard][Marisa] Sakuya - MidBoss 1",
										"[Hard][Marisa] Sakuya Defeated",
										"[Hard][Marisa] Sakuya - MidBoss 2",
										"[Hard][Marisa] Remilia Defeated"],   []),
		"Lunatic - Marisa - Early":   T6RegionData(["[Lunatic][Marisa] Rumia - MidBoss",
										"[Lunatic][Marisa] Rumia Defeated",
										"[Lunatic][Marisa] Daiyousei Defeated",
										"[Lunatic][Marisa] Cirno Defeated"],   ["Marisa - Mid"]),
		"Lunatic - Marisa - Mid":     T6RegionData(["[Lunatic][Marisa] Meiling - MidBoss",
										"[Lunatic][Marisa] Meiling Defeated",
										"[Lunatic][Marisa] Koakuma Defeated",
										"[Lunatic][Marisa] Patchouli Defeated"],   ["Marisa - End"]),
		"Lunatic - Marisa - End":     T6RegionData(["[Lunatic][Marisa] Sakuya - MidBoss 1",
										"[Lunatic][Marisa] Sakuya Defeated",
										"[Lunatic][Marisa] Sakuya - MidBoss 2",
										"[Lunatic][Marisa] Remilia Defeated"],   []),
		"Marisa - Extra":   T6RegionData(["[Marisa] Patchouli - MidBoss",
										"[Marisa] Flandre Defeated",
										"[Marisa] Stage Extra Clear"],   []),
	}

	regionsShotTypeWdifficutly: Dict[str, T6RegionData] = {
		"Menu":            	T6RegionData(None, ["Reimu - A", "Marisa - A", "Reimu - B", "Marisa - B"]),
		"Reimu - A":            T6RegionData(None, ["Reimu - A - Early", "Reimu - A - Mid", "Reimu - A - End",
										  		"Easy - Reimu - A - Early", "Easy - Reimu - A - Mid", "Easy - Reimu - A - End",
										  		"Normal - Reimu - A - Early", "Normal - Reimu - A - Mid", "Normal - Reimu - A - End",
												"Hard - Reimu - A - Early", "Hard - Reimu - A - Mid", "Hard - Reimu - A - End",
												"Lunatic - Reimu - A - Early", "Lunatic - Reimu - A - Mid", "Lunatic - Reimu - A - End",
										  		"Reimu - A - Extra"]),
		"Reimu - B":            T6RegionData(None, ["Reimu - B - Early", "Reimu - B - Mid", "Reimu - B - End",
										  		"Easy - Reimu - B - Early", "Easy - Reimu - B - Mid", "Easy - Reimu - B - End",
										  		"Normal - Reimu - B - Early", "Normal - Reimu - B - Mid", "Normal - Reimu - B - End",
												"Hard - Reimu - B - Early", "Hard - Reimu - B - Mid", "Hard - Reimu - B - End",
												"Lunatic - Reimu - B - Early", "Lunatic - Reimu - B - Mid", "Lunatic - Reimu - B - End",
										  		"Reimu - B - Extra"]),
		"Marisa - A":           T6RegionData(None, ["Marisa - A - Early", "Marisa - A - Mid", "Marisa - A - End",
												"Easy - Marisa - A - Early", "Easy - Marisa - A - Mid", "Easy - Marisa - A - End",
												"Normal - Marisa - A - Early", "Normal - Marisa - A - Mid", "Normal - Marisa - A - End",
												"Hard - Marisa - A - Early", "Hard - Marisa - A - Mid", "Hard - Marisa - A - End",
												"Lunatic - Marisa - A - Early", "Lunatic - Marisa - A - Mid", "Lunatic - Marisa - A - End",
										  		"Marisa - A - Extra"]),
		"Marisa - B":           T6RegionData(None, ["Marisa - B - Early", "Marisa - B - Mid", "Marisa - B - End",
												"Easy - Marisa - B - Early", "Easy - Marisa - B - Mid", "Easy - Marisa - B - End",
												"Normal - Marisa - B - Early", "Normal - Marisa - B - Mid", "Normal - Marisa - B - End",
												"Hard - Marisa - B - Early", "Hard - Marisa - B - Mid", "Hard - Marisa - B - End",
												"Lunatic - Marisa - B - Early", "Lunatic - Marisa - B - Mid", "Lunatic - Marisa - B - End",
										  		"Marisa - B - Extra"]),

		"Reimu - A - Early":  T6RegionData(["[Reimu A] Stage 1 Clear",
										"[Reimu A] Stage 2 Clear"],   []),
		"Reimu - A - Mid":    T6RegionData(["[Reimu A] Stage 3 Clear",
										"[Reimu A] Stage 4 Clear"],   []),
		"Reimu - A - End":    T6RegionData(["[Reimu A] Stage 5 Clear",
										"[Reimu A] Stage 6 Clear"],   []),
		"Easy - Reimu - A - Early":    T6RegionData(["[Easy][Reimu A] Rumia - MidBoss",
										"[Easy][Reimu A] Rumia Defeated",
										"[Easy][Reimu A] Daiyousei Defeated",
										"[Easy][Reimu A] Cirno Defeated"],   []),
		"Easy - Reimu - A - Mid":      T6RegionData(["[Easy][Reimu A] Meiling - MidBoss",
										"[Easy][Reimu A] Meiling Defeated",
										"[Easy][Reimu A] Koakuma Defeated",
										"[Easy][Reimu A] Patchouli Defeated"],   []),
		"Easy - Reimu - A - End":      T6RegionData(["[Easy][Reimu A] Sakuya - MidBoss 1",
										"[Easy][Reimu A] Sakuya Defeated"],   []),
		"Normal - Reimu - A - Early":    T6RegionData(["[Normal][Reimu A] Rumia - MidBoss",
										"[Normal][Reimu A] Rumia Defeated",
										"[Normal][Reimu A] Daiyousei Defeated",
										"[Normal][Reimu A] Cirno Defeated"],   []),
		"Normal - Reimu - A - Mid":      T6RegionData(["[Normal][Reimu A] Meiling - MidBoss",
										"[Normal][Reimu A] Meiling Defeated",
										"[Normal][Reimu A] Koakuma Defeated",
										"[Normal][Reimu A] Patchouli Defeated"],   []),
		"Normal - Reimu - A - End":      T6RegionData(["[Normal][Reimu A] Sakuya - MidBoss 1",
										"[Normal][Reimu A] Sakuya Defeated",
										"[Normal][Reimu A] Sakuya - MidBoss 2",
										"[Normal][Reimu A] Remilia Defeated"],   []),
		"Hard - Reimu - A - Early":    T6RegionData(["[Hard][Reimu A] Rumia - MidBoss",
										"[Hard][Reimu A] Rumia Defeated",
										"[Hard][Reimu A] Daiyousei Defeated",
										"[Hard][Reimu A] Cirno Defeated"],   []),
		"Hard - Reimu - A - Mid":      T6RegionData(["[Hard][Reimu A] Meiling - MidBoss",
										"[Hard][Reimu A] Meiling Defeated",
										"[Hard][Reimu A] Koakuma Defeated",
										"[Hard][Reimu A] Patchouli Defeated"],   []),
		"Hard - Reimu - A - End":      T6RegionData(["[Hard][Reimu A] Sakuya - MidBoss 1",
										"[Hard][Reimu A] Sakuya Defeated",
										"[Hard][Reimu A] Sakuya - MidBoss 2",
										"[Hard][Reimu A] Remilia Defeated"],   []),
		"Lunatic - Reimu - A - Early":    T6RegionData(["[Lunatic][Reimu A] Rumia - MidBoss",
										"[Lunatic][Reimu A] Rumia Defeated",
										"[Lunatic][Reimu A] Daiyousei Defeated",
										"[Lunatic][Reimu A] Cirno Defeated"],   []),
		"Lunatic - Reimu - A - Mid":      T6RegionData(["[Lunatic][Reimu A] Meiling - MidBoss",
										"[Lunatic][Reimu A] Meiling Defeated",
										"[Lunatic][Reimu A] Koakuma Defeated",
										"[Lunatic][Reimu A] Patchouli Defeated"],   []),
		"Lunatic - Reimu - A - End":      T6RegionData(["[Lunatic][Reimu A] Sakuya - MidBoss 1",
										"[Lunatic][Reimu A] Sakuya Defeated",
										"[Lunatic][Reimu A] Sakuya - MidBoss 2",
										"[Lunatic][Reimu A] Remilia Defeated"],   []),
		"Reimu - A - Extra":    T6RegionData(["[Reimu A] Patchouli - MidBoss",
										"[Reimu A] Flandre Defeated",
										"[Reimu A] Stage Extra Clear"],   []),

		"Reimu - B - Early":  T6RegionData(["[Reimu B] Stage 1 Clear",
										"[Reimu B] Stage 2 Clear"],   []),
		"Reimu - B - Mid":    T6RegionData(["[Reimu B] Stage 3 Clear",
										"[Reimu B] Stage 4 Clear"],   []),
		"Reimu - B - End":    T6RegionData(["[Reimu B] Stage 5 Clear",
										"[Reimu B] Stage 6 Clear"],   []),
		"Easy - Reimu - B - Early":    T6RegionData(["[Easy][Reimu B] Rumia - MidBoss",
										"[Easy][Reimu B] Rumia Defeated",
										"[Easy][Reimu B] Daiyousei Defeated",
										"[Easy][Reimu B] Cirno Defeated"],   []),
		"Easy - Reimu - B - Mid":      T6RegionData(["[Easy][Reimu B] Meiling - MidBoss",
										"[Easy][Reimu B] Meiling Defeated",
										"[Easy][Reimu B] Koakuma Defeated",
										"[Easy][Reimu B] Patchouli Defeated"],   []),
		"Easy - Reimu - B - End":      T6RegionData(["[Easy][Reimu B] Sakuya - MidBoss 1",
										"[Easy][Reimu B] Sakuya Defeated"],   []),
		"Normal - Reimu - B - Early":    T6RegionData(["[Normal][Reimu B] Rumia - MidBoss",
										"[Normal][Reimu B] Rumia Defeated",
										"[Normal][Reimu B] Daiyousei Defeated",
										"[Normal][Reimu B] Cirno Defeated"],   []),
		"Normal - Reimu - B - Mid":      T6RegionData(["[Normal][Reimu B] Meiling - MidBoss",
										"[Normal][Reimu B] Meiling Defeated",
										"[Normal][Reimu B] Koakuma Defeated",
										"[Normal][Reimu B] Patchouli Defeated"],   []),
		"Normal - Reimu - B - End":      T6RegionData(["[Normal][Reimu B] Sakuya - MidBoss 1",
										"[Normal][Reimu B] Sakuya Defeated",
										"[Normal][Reimu B] Sakuya - MidBoss 2",
										"[Normal][Reimu B] Remilia Defeated"],   []),
		"Hard - Reimu - B - Early":    T6RegionData(["[Hard][Reimu B] Rumia - MidBoss",
										"[Hard][Reimu B] Rumia Defeated",
										"[Hard][Reimu B] Daiyousei Defeated",
										"[Hard][Reimu B] Cirno Defeated"],   []),
		"Hard - Reimu - B - Mid":      T6RegionData(["[Hard][Reimu B] Meiling - MidBoss",
										"[Hard][Reimu B] Meiling Defeated",
										"[Hard][Reimu B] Koakuma Defeated",
										"[Hard][Reimu B] Patchouli Defeated"],   []),
		"Hard - Reimu - B - End":      T6RegionData(["[Hard][Reimu B] Sakuya - MidBoss 1",
										"[Hard][Reimu B] Sakuya Defeated",
										"[Hard][Reimu B] Sakuya - MidBoss 2",
										"[Hard][Reimu B] Remilia Defeated"],   []),
		"Lunatic - Reimu - B - Early":    T6RegionData(["[Lunatic][Reimu B] Rumia - MidBoss",
										"[Lunatic][Reimu B] Rumia Defeated",
										"[Lunatic][Reimu B] Daiyousei Defeated",
										"[Lunatic][Reimu B] Cirno Defeated"],   []),
		"Lunatic - Reimu - B - Mid":      T6RegionData(["[Lunatic][Reimu B] Meiling - MidBoss",
										"[Lunatic][Reimu B] Meiling Defeated",
										"[Lunatic][Reimu B] Koakuma Defeated",
										"[Lunatic][Reimu B] Patchouli Defeated"],   []),
		"Lunatic - Reimu - B - End":      T6RegionData(["[Lunatic][Reimu B] Sakuya - MidBoss 1",
										"[Lunatic][Reimu B] Sakuya Defeated",
										"[Lunatic][Reimu B] Sakuya - MidBoss 2",
										"[Lunatic][Reimu B] Remilia Defeated"],   []),
		"Reimu - B - Extra":    T6RegionData(["[Reimu B] Patchouli - MidBoss",
										"[Reimu B] Flandre Defeated",
										"[Reimu B] Stage Extra Clear"],   []),

		"Marisa - A - Early":  T6RegionData(["[Marisa A] Stage 1 Clear",
										"[Marisa A] Stage 2 Clear"],   []),
		"Marisa - A - Mid":    T6RegionData(["[Marisa A] Stage 3 Clear",
										"[Marisa A] Stage 4 Clear"],   []),
		"Marisa - A - End":    T6RegionData(["[Marisa A] Stage 5 Clear",
										"[Marisa A] Stage 6 Clear"],   []),
		"Easy - Marisa - A - Early":    T6RegionData(["[Easy][Marisa A] Rumia - MidBoss",
										"[Easy][Marisa A] Rumia Defeated",
										"[Easy][Marisa A] Daiyousei Defeated",
										"[Easy][Marisa A] Cirno Defeated"],   []),
		"Easy - Marisa - A - Mid":      T6RegionData(["[Easy][Marisa A] Meiling - MidBoss",
										"[Easy][Marisa A] Meiling Defeated",
										"[Easy][Marisa A] Koakuma Defeated",
										"[Easy][Marisa A] Patchouli Defeated"],   []),
		"Easy - Marisa - A - End":      T6RegionData(["[Easy][Marisa A] Sakuya - MidBoss 1",
										"[Easy][Marisa A] Sakuya Defeated"],   []),
		"Normal - Marisa - A - Early":    T6RegionData(["[Normal][Marisa A] Rumia - MidBoss",
										"[Normal][Marisa A] Rumia Defeated",
										"[Normal][Marisa A] Daiyousei Defeated",
										"[Normal][Marisa A] Cirno Defeated"],   []),
		"Normal - Marisa - A - Mid":      T6RegionData(["[Normal][Marisa A] Meiling - MidBoss",
										"[Normal][Marisa A] Meiling Defeated",
										"[Normal][Marisa A] Koakuma Defeated",
										"[Normal][Marisa A] Patchouli Defeated"],   []),
		"Normal - Marisa - A - End":      T6RegionData(["[Normal][Marisa A] Sakuya - MidBoss 1",
										"[Normal][Marisa A] Sakuya Defeated",
										"[Normal][Marisa A] Sakuya - MidBoss 2",
										"[Normal][Marisa A] Remilia Defeated"],   []),
		"Hard - Marisa - A - Early":    T6RegionData(["[Hard][Marisa A] Rumia - MidBoss",
										"[Hard][Marisa A] Rumia Defeated",
										"[Hard][Marisa A] Daiyousei Defeated",
										"[Hard][Marisa A] Cirno Defeated"],   []),
		"Hard - Marisa - A - Mid":      T6RegionData(["[Hard][Marisa A] Meiling - MidBoss",
										"[Hard][Marisa A] Meiling Defeated",
										"[Hard][Marisa A] Koakuma Defeated",
										"[Hard][Marisa A] Patchouli Defeated"],   []),
		"Hard - Marisa - A - End":      T6RegionData(["[Hard][Marisa A] Sakuya - MidBoss 1",
										"[Hard][Marisa A] Sakuya Defeated",
										"[Hard][Marisa A] Sakuya - MidBoss 2",
										"[Hard][Marisa A] Remilia Defeated"],   []),
		"Lunatic - Marisa - A - Early":    T6RegionData(["[Lunatic][Marisa A] Rumia - MidBoss",
										"[Lunatic][Marisa A] Rumia Defeated",
										"[Lunatic][Marisa A] Daiyousei Defeated",
										"[Lunatic][Marisa A] Cirno Defeated"],   []),
		"Lunatic - Marisa - A - Mid":      T6RegionData(["[Lunatic][Marisa A] Meiling - MidBoss",
										"[Lunatic][Marisa A] Meiling Defeated",
										"[Lunatic][Marisa A] Koakuma Defeated",
										"[Lunatic][Marisa A] Patchouli Defeated"],   []),
		"Lunatic - Marisa - A - End":      T6RegionData(["[Lunatic][Marisa A] Sakuya - MidBoss 1",
										"[Lunatic][Marisa A] Sakuya Defeated",
										"[Lunatic][Marisa A] Sakuya - MidBoss 2",
										"[Lunatic][Marisa A] Remilia Defeated"],   []),
		"Marisa - A - Extra":    T6RegionData(["[Marisa A] Patchouli - MidBoss",
										"[Marisa A] Flandre Defeated",
										"[Marisa A] Stage Extra Clear"],   []),

		"Marisa - B - Early":  T6RegionData(["[Marisa B] Stage 1 Clear",
										"[Marisa B] Stage 2 Clear"],   []),
		"Marisa - B - Mid":    T6RegionData(["[Marisa B] Stage 3 Clear",
										"[Marisa B] Stage 4 Clear"],   []),
		"Marisa - B - End":    T6RegionData(["[Marisa B] Stage 5 Clear",
										"[Marisa B] Stage 6 Clear"],   []),
		"Easy - Marisa - B - Early":    T6RegionData(["[Easy][Marisa B] Rumia - MidBoss",
										"[Easy][Marisa B] Rumia Defeated",
										"[Easy][Marisa B] Daiyousei Defeated",
										"[Easy][Marisa B] Cirno Defeated"],   []),
		"Easy - Marisa - B - Mid":      T6RegionData(["[Easy][Marisa B] Meiling - MidBoss",
										"[Easy][Marisa B] Meiling Defeated",
										"[Easy][Marisa B] Koakuma Defeated",
										"[Easy][Marisa B] Patchouli Defeated"],   []),
		"Easy - Marisa - B - End":      T6RegionData(["[Easy][Marisa B] Sakuya - MidBoss 1",
										"[Easy][Marisa B] Sakuya Defeated"],   []),
		"Normal - Marisa - B - Early":    T6RegionData(["[Normal][Marisa B] Rumia - MidBoss",
										"[Normal][Marisa B] Rumia Defeated",
										"[Normal][Marisa B] Daiyousei Defeated",
										"[Normal][Marisa B] Cirno Defeated"],   []),
		"Normal - Marisa - B - Mid":      T6RegionData(["[Normal][Marisa B] Meiling - MidBoss",
										"[Normal][Marisa B] Meiling Defeated",
										"[Normal][Marisa B] Koakuma Defeated",
										"[Normal][Marisa B] Patchouli Defeated"],   []),
		"Normal - Marisa - B - End":      T6RegionData(["[Normal][Marisa B] Sakuya - MidBoss 1",
										"[Normal][Marisa B] Sakuya Defeated",
										"[Normal][Marisa B] Sakuya - MidBoss 2",
										"[Normal][Marisa B] Remilia Defeated"],   []),
		"Hard - Marisa - B - Early":    T6RegionData(["[Hard][Marisa B] Rumia - MidBoss",
										"[Hard][Marisa B] Rumia Defeated",
										"[Hard][Marisa B] Daiyousei Defeated",
										"[Hard][Marisa B] Cirno Defeated"],   []),
		"Hard - Marisa - B - Mid":      T6RegionData(["[Hard][Marisa B] Meiling - MidBoss",
										"[Hard][Marisa B] Meiling Defeated",
										"[Hard][Marisa B] Koakuma Defeated",
										"[Hard][Marisa B] Patchouli Defeated"],   []),
		"Hard - Marisa - B - End":      T6RegionData(["[Hard][Marisa B] Sakuya - MidBoss 1",
										"[Hard][Marisa B] Sakuya Defeated",
										"[Hard][Marisa B] Sakuya - MidBoss 2",
										"[Hard][Marisa B] Remilia Defeated"],   []),
		"Lunatic - Marisa - B - Early":    T6RegionData(["[Lunatic][Marisa B] Rumia - MidBoss",
										"[Lunatic][Marisa B] Rumia Defeated",
										"[Lunatic][Marisa B] Daiyousei Defeated",
										"[Lunatic][Marisa B] Cirno Defeated"],   []),
		"Lunatic - Marisa - B - Mid":      T6RegionData(["[Lunatic][Marisa B] Meiling - MidBoss",
										"[Lunatic][Marisa B] Meiling Defeated",
										"[Lunatic][Marisa B] Koakuma Defeated",
										"[Lunatic][Marisa B] Patchouli Defeated"],   []),
		"Lunatic - Marisa - B - End":      T6RegionData(["[Lunatic][Marisa B] Sakuya - MidBoss 1",
										"[Lunatic][Marisa B] Sakuya Defeated",
										"[Lunatic][Marisa B] Sakuya - MidBoss 2",
										"[Lunatic][Marisa B] Remilia Defeated"],   []),
		"Marisa - B - Extra":    T6RegionData(["[Marisa B] Patchouli - MidBoss",
										"[Marisa B] Flandre Defeated",
										"[Marisa B] Stage Extra Clear"],   []),
	}

	extra = getattr(options, "extra_stage")
	shot_type = getattr(options, "shot_type")
	difficulty_check = getattr(options, "difficulty_check")

	if difficulty_check:
		regions = regionsShotTypeWdifficutly if shot_type else regionsNoShotTypeWdifficutly
	else:
		regions = regionsShotType if shot_type else regionsNoShotType

	# Set up the regions correctly.
	for name, data in regions.items():
		if extra == 0 and "Extra" in name:
			continue

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