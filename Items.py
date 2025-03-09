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
	"+1 Life":				TItemData("Items", 60000, ItemClassification.progression_skip_balancing, 8),
	"+1 Bomb":				TItemData("Items", 60001, ItemClassification.progression_skip_balancing, 8),
	"Lower Difficulty":		TItemData("Items", 60002, ItemClassification.progression_skip_balancing, 3),
	"+1 Continue":			TItemData("[Normal] Items", 60016, ItemClassification.useful, 3),

	# Characters
	"Reimu A - Homing Amulet":		TItemData("Characters", 60003, ItemClassification.progression),
	"Reimu B - Persuasion Needle":	TItemData("Characters", 60004, ItemClassification.progression),
	"Marisa A - Magic Missile":		TItemData("Characters", 60005, ItemClassification.progression),
	"Marisa B - Illusion Laser":	TItemData("Characters", 60006, ItemClassification.progression),

	# Others
	"Next Stage":					TItemData("Stages", 60013, ItemClassification.progression_skip_balancing, 6),
	"+25 Power Point":				TItemData("Power Point", 60015, ItemClassification.useful, 5),
	"Extra Stage":					TItemData("Extra Stage", 60017, ItemClassification.progression_skip_balancing),

	# Endings
	"[Reimu] Ending - Remilia":		TItemData("Endings", 60014, ItemClassification.progression, 2),
	"[Marisa] Ending - Remilia":	TItemData("Endings", 60018, ItemClassification.progression, 2),
	"[Reimu] Ending - Flandre":		TItemData("Endings", 60019, ItemClassification.progression, 2),
	"[Marisa] Ending - Flandre":	TItemData("Endings", 60020, ItemClassification.progression, 2),

	# Junk
	"+1 Power Point":	TItemData("Filler", 60030),

	# Trap
	"Max Rank":				TItemData("Traps", 60040, ItemClassification.trap),
	"-50% Power Point":		TItemData("Traps", 60041, ItemClassification.trap),
	"-1 Bomb":				TItemData("Traps", 60042, ItemClassification.trap),
	"-1 Life":				TItemData("Traps", 60043, ItemClassification.trap),
	"No Focus":				TItemData("Traps", 60044, ItemClassification.trap),
	"Reverse Movement":		TItemData("Traps", 60045, ItemClassification.trap),
	"Aya Speed":			TItemData("Traps", 60046, ItemClassification.trap),
	"Freeze":				TItemData("Traps", 60047, ItemClassification.trap),
	"Power Point Drain":	TItemData("Traps", 60048, ItemClassification.trap),
}