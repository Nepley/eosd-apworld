from typing import Dict

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet

class Mode(Choice):
    """
    Practice Mode: You need to unlock the stage in order to progress.
    Normal Mode: The resources are only given at Stage 1. Add 3 Continues to the Item Pools. Restriction in life, bomb or difficulty for stages 3/4 and 5/6 and character are the only gate. The difficulty is dynamic, meaning that choosing at the start doesn't change the difficulty that you will get
    """
    display_name = "Mode played"
    option_practice = 0
    option_normal = 1
    default = 0

class NumberLifeMid(Range):
    """Number of life the randomizer expect you to have before facing Meiling and Patchouli"""
    display_name = "Number of life expected in order to face Meiling and Patchouli"
    range_start = 0
    range_end = 8
    default = 0

class NumberBombsMid(Range):
    """Number of bombs the randomizer expect you to have before facing Meiling and Patchouli"""
    display_name = "Number of bombs expected in order to face Meiling and Patchouli"
    range_start = 0
    range_end = 8
    default = 0

class DifficultyMid(Choice):
    """The difficulty expected in order to face Meiling and Patchouli (Starting from Lunatic and got to Easy)"""
    display_name = "Difficulty in order to face Meiling and Patchouli"
    option_lunatic = 0
    option_hard = 1
    option_normal = 2
    option_easy = 3
    default = 0

class NumberLifeEnd(Range):
    """Number of life the randomizer expect you to have before facing Remilia and Sakuya"""
    display_name = "Number of life expected in order to face Remilia and Sakuya"
    range_start = 0
    range_end = 8
    default = 0

class NumberBombsEnd(Range):
    """Number of bombs the randomizer expect you to have before facing Remilia and Sakuya"""
    display_name = "Number of bombs expected in order to face Remilia and Sakuya"
    range_start = 0
    range_end = 8
    default = 0

class DifficultyEnd(Choice):
    """The difficulty expected in order to face Remilia and Sakuya (Starting from Lunatic and got to Easy)"""
    display_name = "Difficulty in order to face Remilia and Sakuya"
    option_lunatic = 0
    option_hard = 1
    option_normal = 2
    option_easy = 3
    default = 0

class EndingRequired(Range):
    """How many ending is required to finish the game"""
    display_name = "How many ending is required to finish the game"
    range_start = 1
    range_end = 2
    default = 1

t6_options: Dict[str, type(Option)] = {
    "mode": Mode,
    "number_life_mid": NumberLifeMid,
    "number_bomb_mid": NumberBombsMid,
    "difficulty_mid": DifficultyMid,
    "number_life_end": NumberLifeEnd,
    "number_bomb_end": NumberBombsEnd,
    "difficulty_end": DifficultyEnd,
    "ending_required": EndingRequired,
    "death_link": DeathLink,
}