from typing import Dict, NamedTuple, Optional
from .Variables import *

from BaseClasses import Item, ItemClassification

class TItem(Item):
	game: str = DISPLAY_NAME

class TItemData(NamedTuple):
	category: str
	code: Optional[int] = None
	classification: ItemClassification = ItemClassification.filler
	max_quantity: int = 1
	weight: int = 1

def get_items_by_category(category: str) -> Dict[str, TItemData]:
	item_dict: Dict[str, TItemData] = {}
	for name, data in item_table.items():
		if data.category == category:
			item_dict.setdefault(name, data)

	return item_dict

item_table: Dict[str, TItemData] = {
	# Items
	"+1 Life":				TItemData("Items", STARTING_ID + 0, ItemClassification.progression, 8),
	"+1 Bomb":				TItemData("Items", STARTING_ID + 1, ItemClassification.progression, 8),
	"Lower Difficulty":		TItemData("Items", STARTING_ID + 2, ItemClassification.progression, 3),
	"+1 Continue":			TItemData("[Normal] Items", STARTING_ID + 3, ItemClassification.useful, 3),

	# Characters
	"Reimu A - Homing Amulet":		TItemData("Characters", STARTING_ID + 100, ItemClassification.progression),
	"Reimu B - Persuasion Needle":	TItemData("Characters", STARTING_ID + 101, ItemClassification.progression),
	"Marisa A - Magic Missile":		TItemData("Characters", STARTING_ID + 102, ItemClassification.progression),
	"Marisa B - Illusion Laser":	TItemData("Characters", STARTING_ID + 103, ItemClassification.progression),

	# Others
	"Next Stage":					TItemData("[Global] Stages", STARTING_ID + 200, ItemClassification.progression, 6),
	"[Reimu] Next Stage":			TItemData("[Character] Stages", STARTING_ID + 201, ItemClassification.progression, 6),
	"[Marisa] Next Stage":			TItemData("[Character] Stages", STARTING_ID + 202, ItemClassification.progression, 6),
	"[Reimu A] Next Stage":			TItemData("[Shot Type] Stages", STARTING_ID + 203, ItemClassification.progression, 6),
	"[Reimu B] Next Stage":			TItemData("[Shot Type] Stages", STARTING_ID + 204, ItemClassification.progression, 6),
	"[Marisa A] Next Stage":		TItemData("[Shot Type] Stages", STARTING_ID + 205, ItemClassification.progression, 6),
	"[Marisa B] Next Stage":		TItemData("[Shot Type] Stages", STARTING_ID + 206, ItemClassification.progression, 6),
	"+25 Power Point":				TItemData("Power Point", STARTING_ID + 207, ItemClassification.useful, 5),
	"Extra Stage":					TItemData("[Global] Extra Stage", STARTING_ID + 208, ItemClassification.progression),
	"[Reimu] Extra Stage":			TItemData("[Character] Extra Stage", STARTING_ID + 209, ItemClassification.progression),
	"[Marisa] Extra Stage":			TItemData("[Character] Extra Stage", STARTING_ID + 210, ItemClassification.progression),
	"[Reimu A] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 211, ItemClassification.progression),
	"[Reimu B] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 212, ItemClassification.progression),
	"[Marisa A] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 213, ItemClassification.progression),
	"[Marisa B] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 214, ItemClassification.progression),

	# Endings
	"[Reimu] Ending - Remilia":		TItemData("Endings", STARTING_ID + 300, ItemClassification.progression, 2),
	"[Marisa] Ending - Remilia":	TItemData("Endings", STARTING_ID + 301, ItemClassification.progression, 2),
	"[Reimu] Ending - Flandre":		TItemData("Endings", STARTING_ID + 302, ItemClassification.progression, 2),
	"[Marisa] Ending - Flandre":	TItemData("Endings", STARTING_ID + 303, ItemClassification.progression, 2),

	# Junk
	"+1 Power Point":	TItemData("Filler", STARTING_ID + 400),

	# Trap
	"Max Rank":				TItemData("Traps", STARTING_ID + 500, ItemClassification.trap),
	"-50% Power Point":		TItemData("Traps", STARTING_ID + 501, ItemClassification.trap),
	"-1 Bomb":				TItemData("Traps", STARTING_ID + 502, ItemClassification.trap),
	"-1 Life":				TItemData("Traps", STARTING_ID + 503, ItemClassification.trap),
	"No Focus":				TItemData("Traps", STARTING_ID + 504, ItemClassification.trap),
	"Reverse Movement":		TItemData("Traps", STARTING_ID + 505, ItemClassification.trap),
	"Aya Speed":			TItemData("Traps", STARTING_ID + 506, ItemClassification.trap),
	"Freeze":				TItemData("Traps", STARTING_ID + 507, ItemClassification.trap),
	"Power Point Drain":	TItemData("Traps", STARTING_ID + 508, ItemClassification.trap),
}

item_groups: Dict[str, str] = {
	"Reimu A": ["Reimu A - Homing Amulet"],
	"Reimu B": ["Reimu B - Persuasion Needle"],
	"Marisa A": ["Marisa A - Magic Missile"],
	"Marisa B": ["Marisa B - Illusion Laser"],
}