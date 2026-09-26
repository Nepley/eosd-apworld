GAMES = [
        {"name": "th06c", "process": "th06c.exe", "checksum": ""},
        {"name": "th06", "process": "東方紅魔郷", "checksum": "e61b4f4fea3802e926ef307f45166599c3e86555"}
    ]

DISPLAY_NAME = "Touhou Koumakyou ~ the Embodiment of Scarlet Devil"
SHORT_NAME = "Touhou EoSD"

REIMU = 0
MARISA = 1
CHARACTERS = [REIMU, MARISA]
CHARACTER_NAME_TO_ID = {"Reimu": REIMU, "Marisa": MARISA}

SHOT_A = 0
SHOT_B = 1
SHOTS = [SHOT_A, SHOT_B]
SHOT_NAME_TO_ID = {"Reimu A": SHOT_A, "Reimu B": SHOT_B, "Marisa A": SHOT_A, "Marisa B": SHOT_B}

EASY = 0
NORMAL = 1
HARD = 2
LUNATIC = 3
EXTRA = 4

NO_EXTRA = 0
EXTRA_LINEAR = 1
EXTRA_APART = 2
PRACTICE_MODE = 0
NORMAL_DYNAMIC_MODE = 1
NORMAL_STATIC_MODE = 2
NORMAL_MODE = [NORMAL_STATIC_MODE, NORMAL_DYNAMIC_MODE]
STAGE_GLOBAL = 0
STAGE_BY_CHARACTER = 1
STAGE_BY_SHOT_TYPE = 2

IN_MENU = 1
IN_GAME = 2
IN_RESULT_SCREEN = 7

MAIN_MENU = 0
DIFFICULTY_MENU = 6
CHARACTER_MENU = 7
SHOT_TYPE_MENU = 13
STAGE_SELECT_MENU = 19

ENDING_NORMAL = 0
ENDING_EXTRA = 1
ENDING_BOTH = 2
ENDINGS = [ENDING_NORMAL, ENDING_EXTRA]
ONE_ENDING = 0
ALL_CHARACTER_ENDING = 1
ALL_SHOT_TYPE_ENDING = 2

DEATH_LINK_LIFE = 0
DEATH_LINK_GAME_OVER = 1

WHITE_TEXT = 0
RED_TEXT = 1
FLASHING_TEXT = 2

"""
Generation Variables
"""

STARTING_ID = 60000
CHARACTERS_LIST = ["Reimu", "Marisa"]
SHOT_TYPE_LIST = ["Reimu A", "Reimu B", "Marisa A", "Marisa B"]
CHARACTER_SHOT_LINK = {"Reimu": ["Reimu A", "Reimu B"], "Marisa": ["Marisa A", "Marisa B"]}
ALL_CHARACTERS_LIST = CHARACTERS_LIST + SHOT_TYPE_LIST
CHARACTER_TO_ITEM = {
    "Reimu": ["Reimu A - Homing Amulet", "Reimu B - Persuasion Needle"],
    "Marisa": ["Marisa A - Magic Missile", "Marisa B - Illusion Laser"],
    "Reimu A": ["Reimu A - Homing Amulet"],
    "Reimu B": ["Reimu B - Persuasion Needle"],
    "Marisa A": ["Marisa A - Magic Missile"],
    "Marisa B": ["Marisa B - Illusion Laser"]
}
DIFFICULTY_LIST = ["Easy", "Normal", "Hard", "Lunatic"]
EXTRA_CHECKS = ["Patchouli - MidBoss",	"Flandre Defeated"]
STAGES_LIST = [
	["Rumia - MidBoss", "Rumia Defeated"],
	["Daiyousei Defeated", "Cirno Defeated"],
	["Meiling - MidBoss", "Meiling Defeated"],
	["Koakuma Defeated", "Patchouli Defeated"],
	["Sakuya - MidBoss 1", "Sakuya Defeated"],
	["Sakuya - MidBoss 2", "Remilia Defeated"],
	EXTRA_CHECKS
]
ENDING_NORMAL_ITEM = "Ending - Remilia"
ENDING_EXTRA_ITEM = "Ending - Flandre"