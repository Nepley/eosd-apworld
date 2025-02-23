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

class ExtraStage(Choice):
    """
    Determine if the extra stage is included
    Linear: The extra stage is considered as the 7th stage
    Apart: The extra stage has it's own item fo it to be unlocked
    """
    display_name = "Determine if the extra stage is included"
    option_exclude = 0
    option_include_linear = 1
    option_include_apart = 2
    default = 0

class NumberLifeExtra(Range):
    """Number of life the randomizer expect you to have before facing Flandre"""
    display_name = "Number of life expected in order to face Flandre"
    range_start = 0
    range_end = 8
    default = 0

class NumberBombsExtra(Range):
    """Number of bombs the randomizer expect you to have before facing Flandre"""
    display_name = "Number of bombs expected in order to face Flandre"
    range_start = 0
    range_end = 8
    default = 0

class ShotTypeCheck(Toggle):
    """"If each shot type have their own check and are not just separated by character"""
    display_name = "Shot Type Check"

class DifficultyCheck(Toggle):
    """If checks are separated by difficulty. The check of the highest difficulty include the check of the lower difficulties that are unlocked"""
    display_name = "Difficulty Check"

class Goal(Choice):
    """If the Extra Stage is included, determine which boss is the goal."""
    display_name = "Goal"
    option_remilia = 0
    option_flandre = 1
    option_both = 2
    default = 0

class EndingRequired(Choice):
    """How many time do you need to beat the required boss"""
    display_name = "How many time do you need to beat the required boss"
    option_once = 0
    option_both_characters = 1
    option_all_shot_types = 2
    default = 0

class Traps(Range):
    """Percentage of fillers that are traps"""
    display_name = "Percentage of fillers that are traps"
    range_start = 0
    range_end = 100
    default = 0

class MaxRankTrap(Range):
    """
    Weight of the max rank trap.
    This trap max out the rank difficulty (32)
    """
    display_name = "Max rank trap"
    range_start = 0
    range_end = 100
    default = 30

class PowerPointTrap(Range):
    """
    Weight of the -50% power point trap.
    This trap reduce the power point by 50%
    """
    display_name = "-50% power point trap"
    range_start = 0
    range_end = 100
    default = 20

class BombTrap(Range):
    """
    Weight of the -1 bomb trap.
    This trap remove 1 bomb
    """
    display_name = "-1 bomb trap"
    range_start = 0
    range_end = 100
    default = 0

class LifeTrap(Range):
    """
    Weight of the -1 life trap.
    This trap remove 1 life
    """
    display_name = "-1 life trap"
    range_start = 0
    range_end = 100
    default = 0

class NoFocusTrap(Range):
    """
    Weight of the no focus trap.
    This trap remove the focus ability
    """
    display_name = "No focus trap"
    range_start = 0
    range_end = 100
    default = 20

class ReverseMovementTrap(Range):
    """
    Weight of the Reverse Movement trap.
    This trap reverse the movement of the player
    """
    display_name = "Reverse Movement trap"
    range_start = 0
    range_end = 100
    default = 20

class AyaSpeedTrap(Range):
    """
    Weight of the Aya speed trap.
    This trap make the speed of the player more extreme (faster normally, slower focus)
    """
    display_name = "Aya speed trap"
    range_start = 0
    range_end = 100
    default = 20

class FreezeTrap(Range):
    """
    Weight of the freeze trap.
    This trap freeze the player for a short amount of time
    """
    display_name = "Freeze trap"
    range_start = 0
    range_end = 100
    default = 5

class PowerPointDrainTrap(Range):
    """
    Weight of the power point drain trap.
    This trap drain the power point of the player (1 power point per second)
    """
    display_name = "Power point drain trap"
    range_start = 0
    range_end = 100
    default = 15

t6_options: Dict[str, type(Option)] = {
    "mode": Mode,
    "number_life_mid": NumberLifeMid,
    "number_bomb_mid": NumberBombsMid,
    "difficulty_mid": DifficultyMid,
    "number_life_end": NumberLifeEnd,
    "number_bomb_end": NumberBombsEnd,
    "difficulty_end": DifficultyEnd,
    "extra_stage": ExtraStage,
    "number_life_extra": NumberLifeExtra,
    "number_bomb_extra": NumberBombsExtra,
    "shot_type": ShotTypeCheck,
    "difficulty_check": DifficultyCheck,
    "goal": Goal,
    "ending_required": EndingRequired,
    "death_link": DeathLink,
    "traps": Traps,
    "max_rank_trap": MaxRankTrap,
    "power_point_trap": PowerPointTrap,
    "bomb_trap": BombTrap,
    "life_trap": LifeTrap,
    "no_focus_trap": NoFocusTrap,
    "reverse_movement_trap": ReverseMovementTrap,
    "aya_speed_trap": AyaSpeedTrap,
    "freeze_trap": FreezeTrap,
    "power_point_drain_trap": PowerPointDrainTrap,
}