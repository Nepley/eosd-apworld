from typing import Dict, NamedTuple, Optional

from BaseClasses import Location

class T6Location(Location):
	game: str = "Touhou 6"

class T6LocationData(NamedTuple):
	category: str
	code: Optional[int] = None

def get_locations_by_category(category: str) -> Dict[str, T6LocationData]:
	location_dict: Dict[str, T6LocationData] = {}
	for name, data in location_table.items():
		if data.category == category:
			location_dict.setdefault(name, data)

	return location_dict

location_table: Dict[str, T6LocationData] = {
	# Reimu
	"[Reimu] Rumia - MidBoss":                  T6LocationData("Reimu",   91_000),
	"[Reimu] Rumia Defeated":                   T6LocationData("Reimu",   91_001),
	"[Reimu] Stage 1 Clear":                    T6LocationData("Reimu",   91_034),
	"[Reimu] Daiyousei Defeated":               T6LocationData("Reimu",   91_002),
	"[Reimu] Cirno Defeated":                   T6LocationData("Reimu",   91_004),
	"[Reimu] Stage 2 Clear":                    T6LocationData("Reimu",   91_003),
	"[Reimu] Meiling - MidBoss":                T6LocationData("Reimu",   91_006),
	"[Reimu] Meiling Defeated":                 T6LocationData("Reimu",   91_007),
	"[Reimu] Stage 3 Clear":                    T6LocationData("Reimu",   91_005),
	"[Reimu] Koakuma Defeated":                 T6LocationData("Reimu",   91_008),
	"[Reimu] Patchouli Defeated":               T6LocationData("Reimu",   91_010),
	"[Reimu] Stage 4 Clear":                    T6LocationData("Reimu",   91_009),
	"[Reimu] Sakuya - MidBoss 1":               T6LocationData("Reimu",   91_012),
	"[Reimu] Sakuya Defeated":                  T6LocationData("Reimu",   91_013),
	"[Reimu] Stage 5 Clear":                    T6LocationData("Reimu",   91_011),
	"[Reimu] Sakuya - MidBoss 2":               T6LocationData("Reimu",   91_015),
	"[Reimu] Remilia Defeated":                 T6LocationData("Reimu",   91_016),
	"[Reimu] Stage 6 Clear":                    T6LocationData("Reimu",   91_014),

	# Marisa
	"[Marisa] Rumia - MidBoss":                 T6LocationData("Marisa",   91_017),
	"[Marisa] Rumia Defeated":                  T6LocationData("Marisa",   91_018),
	"[Marisa] Stage 1 Clear":                   T6LocationData("Marisa",   91_035),
	"[Marisa] Daiyousei Defeated":              T6LocationData("Marisa",   91_019),
	"[Marisa] Cirno Defeated":                  T6LocationData("Marisa",   91_021),
	"[Marisa] Stage 2 Clear":                   T6LocationData("Marisa",   91_020),
	"[Marisa] Meiling - MidBoss":               T6LocationData("Marisa",   91_023),
	"[Marisa] Meiling Defeated":                T6LocationData("Marisa",   91_024),
	"[Marisa] Stage 3 Clear":                   T6LocationData("Marisa",   91_022),
	"[Marisa] Koakuma Defeated":                T6LocationData("Marisa",   91_025),
	"[Marisa] Patchouli Defeated":              T6LocationData("Marisa",   91_027),
	"[Marisa] Stage 4 Clear":                   T6LocationData("Marisa",   91_026),
	"[Marisa] Sakuya - MidBoss 1":              T6LocationData("Marisa",   91_029),
	"[Marisa] Sakuya Defeated":                 T6LocationData("Marisa",   91_030),
	"[Marisa] Stage 5 Clear":                   T6LocationData("Marisa",   91_028),
	"[Marisa] Sakuya - MidBoss 2":              T6LocationData("Marisa",   91_032),
	"[Marisa] Remilia Defeated":                T6LocationData("Marisa",   91_033),
	"[Marisa] Stage 6 Clear":                   T6LocationData("Marisa",   91_031),
}

event_location_table: Dict[str, T6LocationData] = {}