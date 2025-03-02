import pymem
from .Tools import *

REIMU = 0
MARISA = 1
SHOT_A = 0
SHOT_B = 1
EASY = 0
NORMAL = 1
HARD = 2
LUNATIC = 3

ADDR_GAME_MODE = 0x002C6EA4 # 7 = Result Screen / 2 = In Game / 1 = In Menu
ADDR_IN_DEMO = 0x0029D4C4 # 0 = No / 1 = Yes
ADDR_MENU = 0x002D496A # 0 = Main Menu / 6 = Difficulty / 7 = Character / 13 = Shot / 19 = Stage Select / 18 = Extra Difficulty
ADDR_MENU_CURSOR = 0x002DC860
ADDR_INPUT = 0x0029D904
ADDR_STAGE = 0x0029D6D4
ADDR_DIFFICULTY = 0x0029BCB0
ADDR_RANK = 0x0029D710
ADDR_CHARACTER = 0x0029D4BD
ADDR_SHOT_TYPE = 0x0029D4BE
ADDR_CUSTOM_SOUND_ID = 0x0029D4FB

ADDR_HP_ENEMY = [0x000B957C, 0x000BA444, 0x000BB30C, 0x000BC1D4, 0x000BD09C, 0x000BDF64, 0x000BEE2C, 0x000BFCF4, 0x000C0BBC, 0x000C1A84, 0x000C294C, 0x000C3814, 0x000C55A4, 0x000C7334]
ADDR_IS_BOSS_PRESENT = 0x0029BC50 # 0 = No boss / 1 = Boss present

ADDR_LIVES = 0x0029D4BA
ADDR_BOMBS = 0x0029D4BB
ADDR_POWER = 0x0029D4B0
ADDR_CONTINUE = 0x0029D4B8

# Stats
ADDR_MISSES = 0x0029BCC0

# Practice stage access
ADDR_REIMU_A_EASY = 0x0029CCE1
ADDR_REIMU_A_NORMAL = 0x0029CCE2
ADDR_REIMU_A_HARD = 0x0029CCE3
ADDR_REIMU_A_LUNATIC = 0x0029CCE4

ADDR_REIMU_B_EASY = 0x0029CCF9
ADDR_REIMU_B_NORMAL = 0x0029CCFA
ADDR_REIMU_B_HARD = 0x0029CCFB
ADDR_REIMU_B_LUNATIC = 0x0029CCFC

ADDR_MARISA_A_EASY = 0x0029CD11
ADDR_MARISA_A_NORMAL = 0x0029CD12
ADDR_MARISA_A_HARD = 0x0029CD13
ADDR_MARISA_A_LUNATIC = 0x0029CD14

ADDR_MARISA_B_EASY = 0x0029CD29
ADDR_MARISA_B_NORMAL = 0x0029CD2A
ADDR_MARISA_B_HARD = 0x0029CD2B
ADDR_MARISA_B_LUNATIC = 0x0029CD2C

# Extra stage access
ADDR_REIMU_A_EXTRA = 0x0029CCDE
ADDR_REIMU_B_EXTRA = 0x0029CCF6
ADDR_MARISA_A_EXTRA = 0x0029CD0E
ADDR_MARISA_B_EXTRA = 0x0029CD26

# Practice stage score
ADDR_REIMU_A_EASY_SCORE_1 = 0x0029CD3C
ADDR_REIMU_A_EASY_SCORE_2 = 0x0029CD8C
ADDR_REIMU_A_EASY_SCORE_3 = 0x0029CDDC
ADDR_REIMU_A_EASY_SCORE_4 = 0x0029CE2C
ADDR_REIMU_A_EASY_SCORE_5 = 0x0029CE7C

ADDR_REIMU_A_NORMAL_SCORE_1 = 0x0029CD50
ADDR_REIMU_A_NORMAL_SCORE_2 = 0x0029CDA0
ADDR_REIMU_A_NORMAL_SCORE_3 = 0x0029CDF0
ADDR_REIMU_A_NORMAL_SCORE_4 = 0x0029CE40
ADDR_REIMU_A_NORMAL_SCORE_5 = 0x0029CE90
ADDR_REIMU_A_NORMAL_SCORE_6 = 0x0029CEE0

ADDR_REIMU_A_HARD_SCORE_1 = 0x0029CD64
ADDR_REIMU_A_HARD_SCORE_2 = 0x0029CDB4
ADDR_REIMU_A_HARD_SCORE_3 = 0x0029CE04
ADDR_REIMU_A_HARD_SCORE_4 = 0x0029CE54
ADDR_REIMU_A_HARD_SCORE_5 = 0x0029CEA4
ADDR_REIMU_A_HARD_SCORE_6 = 0x0029CEF4

ADDR_REIMU_A_LUNATIC_SCORE_1 = 0x0029CD78
ADDR_REIMU_A_LUNATIC_SCORE_2 = 0x0029CDC8
ADDR_REIMU_A_LUNATIC_SCORE_3 = 0x0029CE18
ADDR_REIMU_A_LUNATIC_SCORE_4 = 0x0029CE68
ADDR_REIMU_A_LUNATIC_SCORE_5 = 0x0029CEB8
ADDR_REIMU_A_LUNATIC_SCORE_6 = 0x0029CF08

ADDR_REIMU_B_EASY_SCORE_1 = 0x0029CF1C
ADDR_REIMU_B_EASY_SCORE_2 = 0x0029CF6C
ADDR_REIMU_B_EASY_SCORE_3 = 0x0029CFBC
ADDR_REIMU_B_EASY_SCORE_4 = 0x0029D00C
ADDR_REIMU_B_EASY_SCORE_5 = 0x0029D05C

ADDR_REIMU_B_NORMAL_SCORE_1 = 0x0029CF30
ADDR_REIMU_B_NORMAL_SCORE_2 = 0x0029CF80
ADDR_REIMU_B_NORMAL_SCORE_3 = 0x0029CFD0
ADDR_REIMU_B_NORMAL_SCORE_4 = 0x0029D020
ADDR_REIMU_B_NORMAL_SCORE_5 = 0x0029D070
ADDR_REIMU_B_NORMAL_SCORE_6 = 0x0029D0C0

ADDR_REIMU_B_HARD_SCORE_1 = 0x0029CF44
ADDR_REIMU_B_HARD_SCORE_2 = 0x0029CF94
ADDR_REIMU_B_HARD_SCORE_3 = 0x0029CFE4
ADDR_REIMU_B_HARD_SCORE_4 = 0x0029D034
ADDR_REIMU_B_HARD_SCORE_5 = 0x0029D084
ADDR_REIMU_B_HARD_SCORE_6 = 0x0029D0D4

ADDR_REIMU_B_LUNATIC_SCORE_1 = 0x0029CF58
ADDR_REIMU_B_LUNATIC_SCORE_2 = 0x0029CFA8
ADDR_REIMU_B_LUNATIC_SCORE_3 = 0x0029CFF8
ADDR_REIMU_B_LUNATIC_SCORE_4 = 0x0029D048
ADDR_REIMU_B_LUNATIC_SCORE_5 = 0x0029D098
ADDR_REIMU_B_LUNATIC_SCORE_6 = 0x0029D0E8

ADDR_MARISA_A_EASY_SCORE_1 = 0x0029D0FC
ADDR_MARISA_A_EASY_SCORE_2 = 0x0029D14C
ADDR_MARISA_A_EASY_SCORE_3 = 0x0029D19C
ADDR_MARISA_A_EASY_SCORE_4 = 0x0029D1EC
ADDR_MARISA_A_EASY_SCORE_5 = 0x0029D23C

ADDR_MARISA_A_NORMAL_SCORE_1 = 0x0029D110
ADDR_MARISA_A_NORMAL_SCORE_2 = 0x0029D160
ADDR_MARISA_A_NORMAL_SCORE_3 = 0x0029D1B0
ADDR_MARISA_A_NORMAL_SCORE_4 = 0x0029D200
ADDR_MARISA_A_NORMAL_SCORE_5 = 0x0029D250
ADDR_MARISA_A_NORMAL_SCORE_6 = 0x0029D2A0

ADDR_MARISA_A_HARD_SCORE_1 = 0x0029D124
ADDR_MARISA_A_HARD_SCORE_2 = 0x0029D174
ADDR_MARISA_A_HARD_SCORE_3 = 0x0029D1C4
ADDR_MARISA_A_HARD_SCORE_4 = 0x0029D214
ADDR_MARISA_A_HARD_SCORE_5 = 0x0029D264
ADDR_MARISA_A_HARD_SCORE_6 = 0x0029D2B4

ADDR_MARISA_A_LUNATIC_SCORE_1 = 0x0029D138
ADDR_MARISA_A_LUNATIC_SCORE_2 = 0x0029D188
ADDR_MARISA_A_LUNATIC_SCORE_3 = 0x0029D1D8
ADDR_MARISA_A_LUNATIC_SCORE_4 = 0x0029D228
ADDR_MARISA_A_LUNATIC_SCORE_5 = 0x0029D278
ADDR_MARISA_A_LUNATIC_SCORE_6 = 0x0029D2C8

ADDR_MARISA_B_EASY_SCORE_1 = 0x0029D2DC
ADDR_MARISA_B_EASY_SCORE_2 = 0x0029D32C
ADDR_MARISA_B_EASY_SCORE_3 = 0x0029D37C
ADDR_MARISA_B_EASY_SCORE_4 = 0x0029D3CC
ADDR_MARISA_B_EASY_SCORE_5 = 0x0029D41C

ADDR_MARISA_B_NORMAL_SCORE_1 = 0x0029D2F0
ADDR_MARISA_B_NORMAL_SCORE_2 = 0x0029D340
ADDR_MARISA_B_NORMAL_SCORE_3 = 0x0029D390
ADDR_MARISA_B_NORMAL_SCORE_4 = 0x0029D3E0
ADDR_MARISA_B_NORMAL_SCORE_5 = 0x0029D430
ADDR_MARISA_B_NORMAL_SCORE_6 = 0x0029D480

ADDR_MARISA_B_HARD_SCORE_1 = 0x0029D304
ADDR_MARISA_B_HARD_SCORE_2 = 0x0029D354
ADDR_MARISA_B_HARD_SCORE_3 = 0x0029D3A4
ADDR_MARISA_B_HARD_SCORE_4 = 0x0029D3F4
ADDR_MARISA_B_HARD_SCORE_5 = 0x0029D444
ADDR_MARISA_B_HARD_SCORE_6 = 0x0029D494

ADDR_MARISA_B_LUNATIC_SCORE_1 = 0x0029D318
ADDR_MARISA_B_LUNATIC_SCORE_2 = 0x0029D368
ADDR_MARISA_B_LUNATIC_SCORE_3 = 0x0029D3B8
ADDR_MARISA_B_LUNATIC_SCORE_4 = 0x0029D408
ADDR_MARISA_B_LUNATIC_SCORE_5 = 0x0029D458
ADDR_MARISA_B_LUNATIC_SCORE_6 = 0x0029D4A8

# Character Speed
ADDR_NORMAL_SPEED = 0x002CB01E
ADDR_FOCUS_SPEED = 0x002CB022
ADDR_NORMAL_SPEED_D = 0x002CB026
ADDR_FOCUS_SPEED_D = 0x002CB02A

# Others
ADDR_KILL_CONDITION = 0x00026DC6
ADDR_CONTROLLER_HANDLER = 0x00023366

ADDR_LOCK_1 = 0x000366F7
ADDR_LOCK_2 = 0x00036572
ADDR_LOCK_3 = 0x00036A10
ADDR_LOCK_4 = 0x00036A8F
ADDR_LOCK_JMP = 0x00036403
ADDR_LOCK_FORCE_EXTRA = 0x0003641C # 10 addresses to nop

ADDR_SOUND_HACK_1 = 0x0001CB6C
ADDR_SOUND_HACK_2 = 0x00021AC1

class eosdController:
	"""Class accessing the game memory"""
	pm = None

	# Player
	addrStage = None
	addrDifficulty = None
	addrCharacter = None
	addrRank = None
	addrShotType = None

	# Resources
	addrLives = None
	addrBombs = None
	addrPower = None
	addrContinues = None

	# Stats
	addrMisses = None

	# Practice stage access
	addrReimuAEasy = None
	addrReimuANormal = None
	addrReimuAHard = None
	addrReimuALunatic = None

	addrReimuBEasy = None
	addrReimuBNormal = None
	addrReimuBHard = None
	addrReimuBLunatic = None

	addrMarisaAEasy = None
	addrMarisaANormal = None
	addrMarisaAHard = None
	addrMarisaALunatic = None

	addrMarisaBEasy = None
	addrMarisaBNormal = None
	addrMarisaBHard = None
	addrMarisaBLunatic = None

	# Extra stage access
	addrReimuAExtra = None
	addrReimuBExtra = None
	addrMarisaAExtra = None
	addrMarisaBExtra = None

	# Practice stage score
	addrPracticeScore = None

	# Character speed
	addrNormalSpeed = None
	addrFocusSpeed = None
	addrNormalSpeedD = None
	addrFocusSpeedD = None

	# Other
	addrControllerHandle = None
	addrInput = None
	addrGameMode = None
	addrMenu = None
	addrMenuCursor = None
	addrInDemo = None
	addrHpEnemies = None
	addrIsBossPresent = None
	addrKillCondition = None
	addrCharacterLock = None
	addrForceExtra = None
	addrCustomSoundId = None
	addrSoundHack1 = None
	addrSoundHack2 = None

	def __init__(self, pid):
		self.pm = pymem.Pymem(pid)

		self.addrStage = self.pm.base_address+ADDR_STAGE
		self.addrDifficulty = self.pm.base_address+ADDR_DIFFICULTY
		self.addrRank = self.pm.base_address+ADDR_RANK
		self.addrCharacter = self.pm.base_address+ADDR_CHARACTER
		self.addrShotType = self.pm.base_address+ADDR_SHOT_TYPE

		self.addrLives = self.pm.base_address+ADDR_LIVES
		self.addrBombs = self.pm.base_address+ADDR_BOMBS
		self.addrPower = self.pm.base_address+ADDR_POWER
		self.addrContinues = self.pm.base_address+ADDR_CONTINUE

		self.addrMisses = self.pm.base_address+ADDR_MISSES

		self.addrReimuAEasy = self.pm.base_address+ADDR_REIMU_A_EASY
		self.addrReimuANormal = self.pm.base_address+ADDR_REIMU_A_NORMAL
		self.addrReimuAHard = self.pm.base_address+ADDR_REIMU_A_HARD
		self.addrReimuALunatic = self.pm.base_address+ADDR_REIMU_A_LUNATIC

		self.addrReimuBEasy = self.pm.base_address+ADDR_REIMU_B_EASY
		self.addrReimuBNormal = self.pm.base_address+ADDR_REIMU_B_NORMAL
		self.addrReimuBHard = self.pm.base_address+ADDR_REIMU_B_HARD
		self.addrReimuBLunatic = self.pm.base_address+ADDR_REIMU_B_LUNATIC

		self.addrMarisaAEasy = self.pm.base_address+ADDR_MARISA_A_EASY
		self.addrMarisaANormal = self.pm.base_address+ADDR_MARISA_A_NORMAL
		self.addrMarisaAHard = self.pm.base_address+ADDR_MARISA_A_HARD
		self.addrMarisaALunatic = self.pm.base_address+ADDR_MARISA_A_LUNATIC

		self.addrMarisaBEasy = self.pm.base_address+ADDR_MARISA_B_EASY
		self.addrMarisaBNormal = self.pm.base_address+ADDR_MARISA_B_NORMAL
		self.addrMarisaBHard = self.pm.base_address+ADDR_MARISA_B_HARD
		self.addrMarisaBLunatic = self.pm.base_address+ADDR_MARISA_B_LUNATIC

		self.addrReimuAExtra = self.pm.base_address+ADDR_REIMU_A_EXTRA
		self.addrReimuBExtra = self.pm.base_address+ADDR_REIMU_B_EXTRA
		self.addrMarisaAExtra = self.pm.base_address+ADDR_MARISA_A_EXTRA
		self.addrMarisaBExtra = self.pm.base_address+ADDR_MARISA_B_EXTRA

		self.addrControllerHandle = self.pm.base_address+ADDR_CONTROLLER_HANDLER
		self.addrInput = self.pm.base_address+ADDR_INPUT
		self.addrGameMode = self.pm.base_address+ADDR_GAME_MODE
		self.addrMenu = self.pm.base_address+ADDR_MENU
		self.addrMenuCursor = self.pm.base_address+ADDR_MENU_CURSOR
		self.addrInDemo = self.pm.base_address+ADDR_IN_DEMO
		self.addrIsBossPresent = self.pm.base_address+ADDR_IS_BOSS_PRESENT
		self.addrHpEnemies = []
		for addr in ADDR_HP_ENEMY:
			self.addrHpEnemies.append(self.pm.base_address+addr)

		self.addrKillCondition = self.pm.base_address+ADDR_KILL_CONDITION

		self.addrCharacterLock = [self.pm.base_address+ADDR_LOCK_1, self.pm.base_address+ADDR_LOCK_2, self.pm.base_address+ADDR_LOCK_3, self.pm.base_address+ADDR_LOCK_4, self.pm.base_address+ADDR_LOCK_JMP]
		self.addrForceExtra = self.pm.base_address+ADDR_LOCK_FORCE_EXTRA

		self.addrNormalSpeed = self.pm.base_address+ADDR_NORMAL_SPEED
		self.addrFocusSpeed = self.pm.base_address+ADDR_FOCUS_SPEED
		self.addrNormalSpeedD = self.pm.base_address+ADDR_NORMAL_SPEED_D
		self.addrFocusSpeedD = self.pm.base_address+ADDR_FOCUS_SPEED_D

		self.addrCustomSoundId = self.pm.base_address+ADDR_CUSTOM_SOUND_ID
		self.addrSoundHack1 = self.pm.base_address+ADDR_SOUND_HACK_1
		self.addrSoundHack2 = self.pm.base_address+ADDR_SOUND_HACK_2

		self.addrPracticeScore = {
			REIMU:
				{
					SHOT_A:
					{
						EASY:
						[
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_1,
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_2,
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_3,
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_4,
							self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_5,
						],
						NORMAL:
						[
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_1,
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_2,
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_3,
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_4,
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_5,
							self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_6,
						],
						HARD:
						[
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_1,
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_2,
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_3,
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_4,
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_5,
							self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_6,
						],
						LUNATIC:
						[
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_1,
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_2,
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_3,
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_4,
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_5,
							self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_6,
						],
					},
					SHOT_B:
					{
						EASY:
						[
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_1,
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_2,
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_3,
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_4,
							self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_5,
						],
						NORMAL:
						[
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_1,
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_2,
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_3,
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_4,
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_5,
							self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_6,
						],
						HARD:
						[
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_1,
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_2,
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_3,
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_4,
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_5,
							self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_6,
						],
						LUNATIC:
						[
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_1,
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_2,
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_3,
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_4,
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_5,
							self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_6,
						],
					}

				},
			MARISA:
				{
					SHOT_A:
					{
						EASY:
						[
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_1,
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_2,
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_3,
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_4,
							self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_5,
						],
						NORMAL:
						[
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_1,
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_2,
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_3,
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_4,
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_5,
							self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_6,
						],
						HARD:
						[
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_1,
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_2,
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_3,
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_4,
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_5,
							self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_6,
						],
						LUNATIC:
						[
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_1,
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_2,
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_3,
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_4,
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_5,
							self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_6,
						],
					},
					SHOT_B:
					{
						EASY:
						[
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_1,
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_2,
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_3,
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_4,
							self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_5,
						],
						NORMAL:
						[
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_1,
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_2,
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_3,
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_4,
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_5,
							self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_6,
						],
						HARD:
						[
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_1,
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_2,
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_3,
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_4,
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_5,
							self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_6,
						],
						LUNATIC:
						[
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_1,
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_2,
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_3,
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_4,
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_5,
							self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_6,
						],
					}
				}
		}

	def getStage(self):
		return int.from_bytes(self.pm.read_bytes(self.addrStage, 1))

	def getDifficulty(self):
		return int.from_bytes(self.pm.read_bytes(self.addrDifficulty, 1))

	def getRank(self):
		return int.from_bytes(self.pm.read_bytes(self.addrRank, 1))

	def getCharacter(self):
		return int.from_bytes(self.pm.read_bytes(self.addrCharacter, 1))

	def getShotType(self):
		return int.from_bytes(self.pm.read_bytes(self.addrShotType, 1))

	def getLives(self):
		return int.from_bytes(self.pm.read_bytes(self.addrLives, 1))

	def getBombs(self):
		return int.from_bytes(self.pm.read_bytes(self.addrBombs, 1))

	def getPower(self):
		return int.from_bytes(self.pm.read_bytes(self.addrPower, 1))

	def getMisses(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMisses, 1))

	def getContinues(self):
		return int.from_bytes(self.pm.read_bytes(self.addrContinues, 1))

	def getReimuAEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuAEasy, 1))

	def getReimuANormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuANormal, 1))

	def getReimuAHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuAHard, 1))

	def getReimuALunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuALunatic, 1))

	def getReimuAExtra(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuAExtra, 1))

	def getReimuBEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBEasy, 1))

	def getReimuBNormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBNormal, 1))

	def getReimuBHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBHard, 1))

	def getReimuBLunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBLunatic, 1))

	def getReimuBExtra(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBExtra, 1))

	def getMarisaAEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaAEasy, 1))

	def getMarisaANormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaANormal, 1))

	def getMarisaAHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaAHard, 1))

	def getMarisaALunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaALunatic, 1))

	def getMarisaAExtra(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaAExtra, 1))

	def getMarisaBEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBEasy, 1))

	def getMarisaBNormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBNormal, 1))

	def getMarisaBHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBHard, 1))

	def getMarisaBLunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBLunatic, 1))

	def getMarisaBExtra(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBExtra, 1))

	def getInput(self):
		return int.from_bytes(self.pm.read_bytes(self.addrInput, 1))

	def getGameMode(self):
		return int.from_bytes(self.pm.read_bytes(self.addrGameMode, 1))

	def getInDemo(self):
		return int.from_bytes(self.pm.read_bytes(self.addrInDemo, 1))

	def getMenu(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMenu, 1))

	def getMenuCursor(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMenuCursor, 1))

	def getNormalSpeed(self):
		return int.from_bytes(self.pm.read_bytes(self.addrNormalSpeed, 2))

	def getFocusSpeed(self):
		return int.from_bytes(self.pm.read_bytes(self.addrFocusSpeed, 2))

	def getNormalSpeedD(self):
		return int.from_bytes(self.pm.read_bytes(self.addrNormalSpeedD, 2))

	def getFocusSpeedD(self):
		return int.from_bytes(self.pm.read_bytes(self.addrFocusSpeedD, 2))

	def getCustomSoundId(self):
		return int.from_bytes(self.pm.read_bytes(self.addrCustomSoundId, 1))

	def getHpEnemies(self):
		result = []
		for addr in self.addrHpEnemies:
			result.append(self.pm.read_int(addr))
		return result

	def getIsBossPresent(self):
		return int.from_bytes(self.pm.read_bytes(self.addrIsBossPresent, 1))

	def getPracticeStageScore(self, characterId, shotId, difficultyId, stageId):
		return int.from_bytes(self.pm.read_bytes(self.addrPracticeScore[characterId][shotId][difficultyId][stageId], 4))

	def setMenuCursor(self, newCursor):
		self.pm.write_bytes(self.addrMenuCursor, bytes([newCursor]), 1)

	def setStage(self, newStage):
		self.pm.write_short(self.addrStage, newStage)

	def setDifficulty(self, newDifficulty):
		self.pm.write_short(self.addrDifficulty, newDifficulty)

	def setRank(self, newRank):
		self.pm.write_bytes(self.addrRank, bytes([newRank]), 1)

	def setCharacter(self, newCharacter):
		self.pm.write_short(self.addrCharacter, newCharacter)

	def setShotType(self, newShotType):
		self.pm.write_short(self.addrShotType, newShotType)

	def setLives(self, newLives):
		self.pm.write_bytes(self.addrLives, bytes([newLives]), 1)

	def setBombs(self, newBombs):
		self.pm.write_bytes(self.addrBombs, bytes([newBombs]), 1)

	def setPower(self, newPower):
		self.pm.write_bytes(self.addrPower, bytes([newPower]), 1)

	def setContinues(self, newContinue):
		self.pm.write_short(self.addrContinues, newContinue)

	def setMisses(self, newMisses):
		self.pm.write_short(self.addrMisses, newMisses)

	def setReimuAEasy(self, newReimuAEasy):
		self.pm.write_int(self.addrReimuAEasy, newReimuAEasy)

	def setReimuANormal(self, newReimuANormal):
		self.pm.write_int(self.addrReimuANormal, newReimuANormal)

	def setReimuAHard(self, newReimuAHard):
		self.pm.write_int(self.addrReimuAHard, newReimuAHard)

	def setReimuALunatic(self, newReimuALunatic):
		self.pm.write_int(self.addrReimuALunatic, newReimuALunatic)

	def setReimuAExtra(self, newReimuAExtra):
		self.pm.write_bytes(self.addrReimuAExtra, bytes([newReimuAExtra]), 1)

	def setReimuBEasy(self, newReimuBEasy):
		self.pm.write_int(self.addrReimuBEasy, newReimuBEasy)

	def setReimuBNormal(self, newReimuBNormal):
		self.pm.write_int(self.addrReimuBNormal, newReimuBNormal)

	def setReimuBHard(self, newReimuBHard):
		self.pm.write_int(self.addrReimuBHard, newReimuBHard)

	def setReimuBLunatic(self, newReimuBLunatic):
		self.pm.write_int(self.addrReimuBLunatic, newReimuBLunatic)

	def setReimuBExtra(self, newReimuBExtra):
		self.pm.write_bytes(self.addrReimuBExtra, bytes([newReimuBExtra]), 1)

	def setMarisaAEasy(self, newMarisaAEasy):
		self.pm.write_int(self.addrMarisaAEasy, newMarisaAEasy)

	def setMarisaANormal(self, newMarisaANormal):
		self.pm.write_int(self.addrMarisaANormal, newMarisaANormal)

	def setMarisaAHard(self, newMarisaAHard):
		self.pm.write_int(self.addrMarisaAHard, newMarisaAHard)

	def setMarisaALunatic(self, newMarisaALunatic):
		self.pm.write_int(self.addrMarisaALunatic, newMarisaALunatic)

	def setMarisaAExtra(self, newMarisaAExtra):
		self.pm.write_bytes(self.addrMarisaAExtra, bytes([newMarisaAExtra]), 1)

	def setMarisaBEasy(self, newMarisaBEasy):
		self.pm.write_int(self.addrMarisaBEasy, newMarisaBEasy)

	def setMarisaBNormal(self, newMarisaBNormal):
		self.pm.write_int(self.addrMarisaBNormal, newMarisaBNormal)

	def setMarisaBHard(self, newMarisaBHard):
		self.pm.write_int(self.addrMarisaBHard, newMarisaBHard)

	def setMarisaBLunatic(self, newMarisaBLunatic):
		self.pm.write_int(self.addrMarisaBLunatic, newMarisaBLunatic)

	def setMarisaBExtra(self, newMarisaBExtra):
		self.pm.write_bytes(self.addrMarisaBExtra, bytes([newMarisaBExtra]), 1)

	def setInput(self, newInput):
		self.pm.write_bytes(self.addrInput, bytes([newInput]), 1)

	def setNormalSpeed(self, newNormalSpeed):
		self.pm.write_bytes(self.addrNormalSpeed, newNormalSpeed.to_bytes(2), 2)

	def setFocusSpeed(self, newFocusSpeed):
		self.pm.write_bytes(self.addrFocusSpeed, newFocusSpeed.to_bytes(2), 2)

	def setNormalSpeedD(self, newNormalSpeedD):
		self.pm.write_bytes(self.addrNormalSpeedD, newNormalSpeedD.to_bytes(2), 2)

	def setFocusSpeedD(self, newFocusSpeedD):
		self.pm.write_bytes(self.addrFocusSpeedD, newFocusSpeedD.to_bytes(2), 2)

	def resetHpEnemies(self):
		for addr in self.addrHpEnemies:
			self.pm.write_int(addr, 0)

	def resetBossPresent(self):
		self.pm.write_bytes(self.addrIsBossPresent, bytes([0]), 1)

	def setPracticeStageScore(self, characterId, shotId, difficultyId, stageId, newScore):
		return self.pm.write_int(self.addrPracticeScore[characterId][shotId][difficultyId][stageId], newScore)

	def setKill(self, active):
		if active:
			self.pm.write_bytes(self.addrKillCondition, bytes([0x90, 0x90]), 2)
		else:
			self.pm.write_bytes(self.addrKillCondition, bytes([0xEB, 0x22]), 2)

	def setLockToAllDifficulty(self):
		for lock in self.addrCharacterLock:
			self.pm.write_bytes(lock, bytes([0x90, 0x90]), 2)

		self.pm.write_bytes(self.addrForceExtra, bytes([0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90]), 10)

	def setControllerHandler(self, activate):
		if activate:
			self.pm.write_bytes(self.addrControllerHandle, bytes([0x66, 0xA3, 0x04, 0xD9, 0x69, 0x00]), 6)
		else:
			self.pm.write_bytes(self.addrControllerHandle, bytes([0x90, 0x90, 0x90, 0x90, 0x90, 0x90]), 6)

	def initSoundHack(self):
		soundIdHex = hex(self.addrCustomSoundId)[2:]
		soundId = [int(soundIdHex[i:i+2], 16) for i in range(0, len(soundIdHex), 2)]
		self.pm.write_bytes(self.addrSoundHack2, bytes([0xC7, 0x05, soundId[2], soundId[1], soundId[0], 0x00, 0x20, 0x00, 0x00, 0x00,
														0xE9, 0xBD, 0xB0, 0xFF, 0xFF]), 15)

		self.pm.write_bytes(self.addrSoundHack1, bytes([0x6A, 0x00,
														0xEB, 0x08,
														0x41,
														0x00, 0x53, 0xCB,
														0x41,
														0x00, 0x41, 0xCB,
														0xFF, 0x35, soundId[2], soundId[1], soundId[0], 0x00,
														0xB9, 0x50, 0x3F, 0x6D, 0x00,
														0xE8, 0x58, 0x46, 0x01, 0x00,
														0xE9, 0x34, 0x4F, 0x00, 0x00,
														0x5D,
														0xC3]), 35)

	def setCustomSoundId(self, soundId = 0x0D):
		self.pm.write_bytes(self.addrCustomSoundId, bytes([soundId]), 1)

class eosdState:
	"""Class keeping track of what's unlock for the game"""
	lives = None
	bombs = None
	power = None
	endingRemilia = None
	endingFlandre = None
	stages = None
	continues = None

	hasLunatic = None
	hasHard = None
	hasNormal = None
	hasEasy = None
	hasExtra = None

	hasReimuA = None
	hasReimuB = None
	hasMarisaA = None
	hasMarisaB = None

	gameController = None
	lastSpeeds = []

	bossBeaten = []
	extraBeaten = []

	def __init__(self, pid):
		# Default Value
		self.lives = 0
		self.bombs = 0
		self.power = 0
		self.endingRemilia = [0, 0]
		self.endingFlandre = [0, 0]
		self.stages = 1
		self.continues = 0

		self.hasLunatic = True
		self.hasHard = False
		self.hasNormal = False
		self.hasEasy = False
		self.hasExtra = [[False, False], [False, False,]]

		self.hasReimuA = False
		self.hasReimuB = False
		self.hasMarisaA = False
		self.hasMarisaB = False

		self.bossBeaten = [
			[
				[
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					]
				],
				[
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					]
				]
			],
			[
				[
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					]
				],
				[
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					],
					[
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False],
						[False, False]
					]
				]
			]
		]

		self.extraBeaten = [
				[
					[False, False],
					[False, False]
				],
				[
					[False, False],
					[False, False]
				]
			]
		self.gameController = eosdController(pid)
		self.gameController.initSoundHack()
		self.lastSpeeds = [0, 0, 0, 0]

	def hasBossSpawn(self):
		"""Check if a MidBoss or a Boss has spawn"""
		hasSpawn = -1
		enemies = self.gameController.getHpEnemies()

		for i in range(0, len(enemies)):
			if(enemies[i] >= 5000):
				hasSpawn = i
				break

		return hasSpawn

	#
	# Init Resources
	#

	def giveLives(self):
		self.gameController.setLives(self.lives)

	def giveBombs(self):
		self.gameController.setBombs(self.bombs)

	def givePower(self):
		self.gameController.setPower(self.power)

	def giveContinues(self):
		self.gameController.setContinues(3 - self.continues)

	def setDifficulty(self, excludeEasy = False):
		self.gameController.setDifficulty(self.getHighestDifficulty(excludeEasy))

	def giveAllResources(self, normalMode = False, autoDifficulty = False):
		self.giveLives()
		self.giveBombs()
		self.givePower()

		if normalMode:
			self.giveContinues()

			if autoDifficulty:
				self.setDifficulty(True)

	def updateStageList(self):
		if(self.hasReimuA):
			if(self.hasEasy):
				self.gameController.setReimuAEasy(self.stages)
			else:
				self.gameController.setReimuAEasy(0)

			if(self.hasNormal):
				self.gameController.setReimuANormal(self.stages)
			else:
				self.gameController.setReimuANormal(0)

			if(self.hasHard):
				self.gameController.setReimuAHard(self.stages)
			else:
				self.gameController.setReimuAHard(0)

			if(self.hasLunatic):
				self.gameController.setReimuALunatic(self.stages)
			else:
				self.gameController.setReimuALunatic(0)
		else:
			self.gameController.setReimuAEasy(0)
			self.gameController.setReimuANormal(0)
			self.gameController.setReimuAHard(0)
			self.gameController.setReimuALunatic(0)

		if(self.hasReimuB):
			if(self.hasEasy):
				self.gameController.setReimuBEasy(self.stages)
			else:
				self.gameController.setReimuBEasy(0)

			if(self.hasNormal):
				self.gameController.setReimuBNormal(self.stages)
			else:
				self.gameController.setReimuBNormal(0)

			if(self.hasHard):
				self.gameController.setReimuBHard(self.stages)
			else:
				self.gameController.setReimuBHard(0)

			if(self.hasLunatic):
				self.gameController.setReimuBLunatic(self.stages)
			else:
				self.gameController.setReimuBLunatic(0)
		else:
			self.gameController.setReimuBEasy(0)
			self.gameController.setReimuBNormal(0)
			self.gameController.setReimuBHard(0)
			self.gameController.setReimuBLunatic(0)

		if(self.hasMarisaA):
			if(self.hasEasy):
				self.gameController.setMarisaAEasy(self.stages)
			else:
				self.gameController.setMarisaAEasy(0)

			if(self.hasNormal):
				self.gameController.setMarisaANormal(self.stages)
			else:
				self.gameController.setMarisaANormal(0)

			if(self.hasHard):
				self.gameController.setMarisaAHard(self.stages)
			else:
				self.gameController.setMarisaAHard(0)

			if(self.hasLunatic):
				self.gameController.setMarisaALunatic(self.stages)
			else:
				self.gameController.setMarisaALunatic(0)
		else:
			self.gameController.setMarisaAEasy(0)
			self.gameController.setMarisaANormal(0)
			self.gameController.setMarisaAHard(0)
			self.gameController.setMarisaALunatic(0)

		if(self.hasMarisaB):
			if(self.hasEasy):
				self.gameController.setMarisaBEasy(self.stages)
			else:
				self.gameController.setMarisaBEasy(0)

			if(self.hasNormal):
				self.gameController.setMarisaBNormal(self.stages)
			else:
				self.gameController.setMarisaBNormal(0)

			if(self.hasHard):
				self.gameController.setMarisaBHard(self.stages)
			else:
				self.gameController.setMarisaBHard(0)

			if(self.hasLunatic):
				self.gameController.setMarisaBLunatic(self.stages)
			else:
				self.gameController.setMarisaBLunatic(0)
		else:
			self.gameController.setMarisaBEasy(0)
			self.gameController.setMarisaBNormal(0)
			self.gameController.setMarisaBHard(0)
			self.gameController.setMarisaBLunatic(0)

	def updatePracticeScore(self, shot_type = False, difficulty = False):
		if difficulty:
			if shot_type:
				for difficulty in range(4):
					for character in range(2):
						for shot in range(2):
							for stage in range(6):
								score = 0
								if self.isBossBeaten(character, stage, 1, shot, difficulty):
									score = 999999999
								elif self.isBossBeaten(character, stage, 0, shot, difficulty):
									score = 555555555

								# Easy mode has no stage 6
								if stage < 5 or difficulty != 0:
									self.gameController.setPracticeStageScore(character, shot, difficulty, stage, score)
			else:
				for difficulty in range(4):
					for character in range(2):
						for stage in range(6):
							score = 0
							if self.isBossBeaten(character, stage, 1, -1, difficulty):
								score = 999999999
							elif self.isBossBeaten(character, stage, 0, -1, difficulty):
								score = 555555555

							# Easy mode has no stage 6
							if stage < 5 or difficulty != 0:
								self.gameController.setPracticeStageScore(character, SHOT_A, difficulty, stage, score)
								self.gameController.setPracticeStageScore(character, SHOT_B, difficulty, stage, score)
		else:
			if shot_type:
				for character in range(2):
					for shot in range(2):
						for stage in range(6):
							score = 0
							if self.isBossBeaten(character, stage, 1, shot):
								score = 999999999
							elif self.isBossBeaten(character, stage, 0, shot):
								score = 555555555

							# Easy mode has no stage 6
							if stage < 5:
								self.gameController.setPracticeStageScore(character, shot, EASY, stage, score)

							self.gameController.setPracticeStageScore(character, shot, NORMAL, stage, score)
							self.gameController.setPracticeStageScore(character, shot, HARD, stage, score)
							self.gameController.setPracticeStageScore(character, shot, LUNATIC, stage, score)
			else:
				for character in range(2):
					for stage in range(6):
						score = 0
						if self.isBossBeaten(character, stage, 1):
							score = 999999999
						elif self.isBossBeaten(character, stage, 0):
							score = 555555555

						# Easy mode has no stage 6
						if stage < 5:
							self.gameController.setPracticeStageScore(character, SHOT_A, EASY, stage, score)
							self.gameController.setPracticeStageScore(character, SHOT_B, EASY, stage, score)

						self.gameController.setPracticeStageScore(character, SHOT_A, NORMAL, stage, score)
						self.gameController.setPracticeStageScore(character, SHOT_A, HARD, stage, score)
						self.gameController.setPracticeStageScore(character, SHOT_A, LUNATIC, stage, score)

						self.gameController.setPracticeStageScore(character, SHOT_B, NORMAL, stage, score)
						self.gameController.setPracticeStageScore(character, SHOT_B, HARD, stage, score)
						self.gameController.setPracticeStageScore(character, SHOT_B, LUNATIC, stage, score)

	def updateExtraUnlock(self, otherMode = False):
		if self.hasReimuA and (self.hasExtra[REIMU][SHOT_A] or otherMode):
			self.gameController.setReimuAExtra(99)
		else:
			self.gameController.setReimuAExtra(0)

		if self.hasReimuB and (self.hasExtra[REIMU][SHOT_B] or otherMode):
			self.gameController.setReimuBExtra(99)
		else:
			self.gameController.setReimuBExtra(0)

		if self.hasMarisaA and (self.hasExtra[MARISA][SHOT_A] or otherMode):
			self.gameController.setMarisaAExtra(99)
		else:
			self.gameController.setMarisaAExtra(0)

		if self.hasMarisaB and (self.hasExtra[MARISA][SHOT_B] or otherMode):
			self.gameController.setMarisaBExtra(99)
		else:
			self.gameController.setMarisaBExtra(0)

	#
	# Boss
	#

	def isCurrentBossDefeated(self, counter):
		isDefeated = False
		if self.gameController.getStage() == 7:
			isDefeated = self.extraBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][counter]
		else:
			isDefeated = self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][self.gameController.getDifficulty()][self.gameController.getStage()-1][counter]

		return isDefeated

	def setbossBeaten(self, counter, otherDifficulties = False):
		if self.gameController.getStage() == 7:
			self.extraBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][counter] = True
		else:
			self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][self.gameController.getDifficulty()][self.gameController.getStage()-1][counter] = True
			if otherDifficulties:
				if self.hasEasy:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][0][self.gameController.getStage()-1][counter] = True
				if self.hasNormal and self.gameController.getDifficulty() >= 1:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][1][self.gameController.getStage()-1][counter] = True
				if self.hasHard and self.gameController.getDifficulty() >= 2:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][2][self.gameController.getStage()-1][counter] = True
				if self.hasLunatic and self.gameController.getDifficulty() >= 3:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][3][self.gameController.getStage()-1][counter] = True

	def getBossName(self, counter):
		bossName = [
			["Rumia - MidBoss", "Rumia - Boss"],
			["Dayousei", "Cirno"],
			["Meiling - MidBoss", "Meiling - Boss"],
			["Koakuma", "Patchouli"],
			["Sakuya - MidBoss 1", "Sakuya - Boss"],
			["Sakuya - MidBoss 2", "Remilia"],
			["Patchouli - MidBoss", "Flandre"]
		]

		return bossName[self.gameController.getStage()-1][counter]

	def isBossBeaten(self, character, stage, counter, shot_type = -1, difficulty = -1):
		if difficulty >= 0 and difficulty < 4:
			flags = [
					self.bossBeaten[character][0][difficulty][stage][counter],
					self.bossBeaten[character][1][difficulty][stage][counter],
				]
		elif stage == 6: # Extra Stage
			if shot_type == 0 or shot_type == 1:
				if shot_type == 0:
					flags = [
						self.extraBeaten[character][0][counter],
					]
				else:
					flags = [
						self.extraBeaten[character][1][counter],
					]
			else:
				flags = [
					self.extraBeaten[character][0][counter],
					self.extraBeaten[character][1][counter],
				]
		else:
			flags = [
				self.bossBeaten[character][0][0][stage][counter],
				self.bossBeaten[character][0][1][stage][counter],
				self.bossBeaten[character][0][2][stage][counter],
				self.bossBeaten[character][0][3][stage][counter],
				self.bossBeaten[character][1][0][stage][counter],
				self.bossBeaten[character][1][1][stage][counter],
				self.bossBeaten[character][1][2][stage][counter],
				self.bossBeaten[character][1][3][stage][counter],
			]

		if stage < 6:
			if shot_type == 0 or shot_type == 1:
				if shot_type == 0:
					if difficulty >= 0 and difficulty < 5:
						flags = [flags[0]]
					else:
						flags = flags[:4]
				else:
					if difficulty >= 0 and difficulty < 5:
						flags = [flags[1]]
					else:
						flags = flags[-4:]

		return True if True in flags else False

	#
	# Get Items Functions
	#

	def getLives(self):
		return self.lives

	def getBombs(self):
		return self.bombs

	def getPower(self):
		return self.power

	def getEndings(self):
		return self.endings

	def getHighestDifficulty(self, excludeEasy = False):
		difficulty = 3
		if(self.hasEasy and not excludeEasy):
			difficulty = 0
		elif(self.hasNormal or (self.hasEasy and excludeEasy)):
			difficulty = 1
		elif(self.hasHard):
			difficulty = 2

		return difficulty

	#
	# Set Items Functions
	#
	def addLife(self, addInLevel = True):
		if(self.lives < 8):
			self.lives += 1

		if addInLevel and self.gameController.getGameMode() == 2 and self.gameController.getInDemo() != 1:
			self.gameController.setLives(self.gameController.getLives() + 1)

	def addBomb(self, addInLevel = True):
		if(self.bombs < 8):
			self.bombs += 1

		if addInLevel and self.gameController.getGameMode() == 2 and self.gameController.getInDemo() != 1:
			self.gameController.setBombs(self.gameController.getBombs() + 1)

	def add1Power(self, addInLevel = True):
		if(self.power < 128):
			self.power += 1

		if addInLevel and self.gameController.getGameMode() == 2 and self.gameController.getPower() < 128 and self.gameController.getInDemo() != 1:
			self.gameController.setPower(self.gameController.getPower() + 1)

	def add25Power(self, addInLevel = True):
		if(self.power < 103):
			self.power += 25
		else:
			self.power = 128

		if addInLevel and self.gameController.getGameMode() == 2 and self.gameController.getInDemo() != 1:
			if self.gameController.getPower() < 103:
				self.gameController.setPower(self.gameController.getPower() + 25)
			else:
				self.gameController.setPower(128)

	def addStage(self):
		if(self.stages < 6):
			self.stages += 1

	def addContinue(self):
		if(self.continues < 3):
			self.continues += 1

	def addEndingRemilia(self, character):
		self.endingRemilia[character] += 1

	def addEndingFlandre(self, character):
		self.endingFlandre[character] += 1

	def unlockDifficulty(self, difficulty, update = False):
		if(difficulty == 0):
			self.hasLunatic = True
		elif(difficulty == 1):
			self.hasHard = True
		elif(difficulty == 2):
			self.hasNormal = True
		elif(difficulty == 3):
			self.hasEasy = True

		if update:
			self.setDifficulty(True)

	def unlockExtraStage(self, character =-1, shot_type = -1):
		# Unlock for one character/shot type
		if character > -1 and shot_type > -1:
			self.hasExtra[character][shot_type] = True
		# Unlock for one character
		elif character > -1:
			self.hasExtra[character][SHOT_A] = True
			self.hasExtra[character][SHOT_B] = True
		# Unlock for all characters
		else:
			self.hasExtra = [[True, True], [True, True]]

	def unlockCharacter(self, character):
		if(character == 0):
			self.hasReimuA = True
		elif(character == 1):
			self.hasReimuB = True
		elif(character == 2):
			self.hasMarisaA = True
		elif(character == 3):
			self.hasMarisaB = True

	#
	# Traps
	#

	def halfPowerPoint(self):
		if(self.gameController.getPower() > 0):
			self.gameController.setPower(self.gameController.getPower() // 2)

	def loseBomb(self):
		if(self.gameController.getBombs() > 0):
			self.gameController.setBombs(self.gameController.getBombs() - 1)

	def loseLife(self):
		if(self.gameController.getLives() > 0):
			self.gameController.setLives(self.gameController.getLives() - 1)

	def powerPointDrain(self):
		if(self.gameController.getPower() > 0):
			self.gameController.setPower(self.gameController.getPower() - 1)

	def maxRank(self):
		self.gameController.setRank(32)

	def noFocus(self):
		self.gameController.setFocusSpeed(self.gameController.getNormalSpeed())
		self.gameController.setFocusSpeedD(self.gameController.getNormalSpeedD())

	def reverseControls(self):
		self.gameController.setNormalSpeed(self.gameController.getNormalSpeed()+0x0080)
		self.gameController.setFocusSpeed(self.gameController.getFocusSpeed()+0x0080)
		self.gameController.setNormalSpeedD(self.gameController.getNormalSpeedD()+0x0080)
		self.gameController.setFocusSpeedD(self.gameController.getFocusSpeedD()+0x0080)

	def ayaSpeed(self):
		self.gameController.setNormalSpeed(self.gameController.getNormalSpeed()+0x0001)
		self.gameController.setFocusSpeed(self.gameController.getFocusSpeed()-0x0001)
		self.gameController.setNormalSpeedD(self.gameController.getNormalSpeedD()+0x0001)
		self.gameController.setFocusSpeedD(self.gameController.getFocusSpeedD()-0x0001)

	def freeze(self):
		self.lastSpeeds = [self.gameController.getNormalSpeed(), self.gameController.getFocusSpeed(), self.gameController.getNormalSpeedD(), self.gameController.getFocusSpeedD()]
		self.gameController.setNormalSpeed(0x0000)
		self.gameController.setFocusSpeed(0x0000)
		self.gameController.setNormalSpeedD(0x0000)
		self.gameController.setFocusSpeedD(0x0000)

	def resetSpeed(self):
		self.gameController.setNormalSpeed(self.lastSpeeds[0])
		self.gameController.setFocusSpeed(self.lastSpeeds[1])
		self.gameController.setNormalSpeedD(self.lastSpeeds[2])
		self.gameController.setFocusSpeedD(self.lastSpeeds[3])

	#
	# Other
	#

	def reset(self):
		# Default Value
		self.lives = 0
		self.bombs = 0
		self.power = 0
		self.endingRemilia = [0, 0]
		self.endingFlandre = [0, 0]
		self.stages = 1
		self.continues = 0

		self.hasLunatic = True
		self.hasHard = False
		self.hasNormal = False
		self.hasEasy = False
		self.hasExtra = [[False, False], [False, False,]]

		self.hasReimuA = False
		self.hasReimuB = False
		self.hasMarisaA = False
		self.hasMarisaB = False

	def checkCursor(self):
		cursor = self.gameController.getMenuCursor()
		if self.gameController.getMenu() == 6:
			move = 0
			if cursor == 0 and not self.hasEasy:
				move += 1
			if cursor+move == 1 and not self.hasNormal:
				move += 1
			if cursor+move == 2 and not self.hasHard:
				move += 1

			self.gameController.setMenuCursor(self.gameController.getMenuCursor()+move)

	def playSound(self, soundId):
		self.gameController.setCustomSoundId(soundId)