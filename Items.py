from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification

class T6Item(Item):
	game: str = "Touhou 6"

class T6ItemData(NamedTuple):
	category: str
	code: Optional[int] = None
	classification: ItemClassification = ItemClassification.filler
	max_quantity: int = 1
	weight: int = 1

def get_items_by_category(category: str) -> Dict[str, T6ItemData]:
	item_dict: Dict[str, T6ItemData] = {}
	for name, data in item_table.items():
		if data.category == category:
			item_dict.setdefault(name, data)

	return item_dict

item_table: Dict[str, T6ItemData] = {
	# Items
	"Life":             T6ItemData("Items", 60_000, ItemClassification.progression_skip_balancing, 8),
	"Bomb":             T6ItemData("Items", 60_001, ItemClassification.progression_skip_balancing, 8),
	"Lower Difficulty": T6ItemData("Items", 60_002, ItemClassification.progression_skip_balancing, 3),
	"1 Continue":      T6ItemData("[Normal] Items", 60_016, ItemClassification.useful, 3),

	# Characters
	"Reimu A - Homing Amulet":     T6ItemData("Characters", 60_003, ItemClassification.progression),
	"Reimu B - Persuasion Needle": T6ItemData("Characters", 60_004, ItemClassification.progression),
	"Marisa A - Magic Missile":    T6ItemData("Characters", 60_005, ItemClassification.progression),
	"Marisa B - Illusion Laser":   T6ItemData("Characters", 60_006, ItemClassification.progression),

	# Others
	"Next Stage":     T6ItemData("Stages", 60_013, ItemClassification.progression_skip_balancing, 5),
	"Ending":         T6ItemData("Endings", 60_014, ItemClassification.progression, 2),
	"25 Power Point": T6ItemData("Power Point", 60_015, ItemClassification.useful, 5),

	# Junk
	"1 Power Point": T6ItemData("Filler", 60_030),
}

event_item_table: Dict[str, T6ItemData] = {}