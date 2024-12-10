import pymem

REIMU = 0
MARISA = 1
SHOT_A = 0
SHOT_B = 1
EASY = 0
NORMAL = 1
HARD = 2
LUNATIC = 3

ADDR_GAME_MODE = 0x002C6EA4 # 7 = Result Screen / 2 = In Game / 1 = In Menu
ADDR_STAGE = 0x0029D6D4
ADDR_DIFFICULTY = 0x0029bcb0
ADDR_CHARACTER = 0x0029d4bd
ADDR_SHOT_TYPE = 0x0029d4be

ADDR_HP_ENEMY = [0x000B957C, 0x000BA444, 0x000BB30C, 0x000BC1D4, 0x000BD09C, 0x000BDF64, 0x000BEE2C, 0x000BFCF4, 0x000C0BBC, 0x000C1A84, 0x000C294C, 0x000C3814, 0x000C55A4, 0x000C7334]

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

# Others
ADDR_KILL_CONDITION = 0x00026DC6

class eosdController:
	"""Class accessing the game memory"""
	gameName = "東方紅魔郷"
	pm = None

	# Player
	addrStage = None
	addrDifficulty = None
	addrCharacter = None
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

	# Practice stage score
	addrPracticeScore = None

	# Other
	addrGameMode = None
	addrHpEnemies = None
	addrKillCondition = None

	def __init__(self):
		self.pm = pymem.Pymem(self.gameName)

		self.addrStage = self.pm.base_address+ADDR_STAGE
		self.addrDifficulty = self.pm.base_address+ADDR_DIFFICULTY
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

		self.addrGameMode = self.pm.base_address+ADDR_GAME_MODE
		self.addrHpEnemies = []
		for addr in ADDR_HP_ENEMY:
			self.addrHpEnemies.append(self.pm.base_address+addr)

		self.addrKillCondition = self.pm.base_address+ADDR_KILL_CONDITION

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

	def getReimuBEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBEasy, 1))

	def getReimuBNormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBNormal, 1))

	def getReimuBHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBHard, 1))

	def getReimuBLunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrReimuBLunatic, 1))

	def getMarisaAEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaAEasy, 1))

	def getMarisaANormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaANormal, 1))

	def getMarisaAHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaAHard, 1))

	def getMarisaALunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaALunatic, 1))

	def getMarisaBEasy(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBEasy, 1))

	def getMarisaBNormal(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBNormal, 1))

	def getMarisaBHard(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBHard, 1))

	def getMarisaBLunatic(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMarisaBLunatic, 1))

	def getGameMode(self):
		return int.from_bytes(self.pm.read_bytes(self.addrGameMode, 1))

	def getHpEnemies(self):
		result = []
		for addr in self.addrHpEnemies:
			result.append(self.pm.read_int(addr))
		return result
	
	def getPracticeStageScore(self, characterId, shotId, difficultyId, stageId):
		return int.from_bytes(self.pm.read_bytes(self.addrPracticeScore[characterId][shotId][difficultyId][stageId], 4))

	def setStage(self, newStage):
		self.pm.write_short(self.addrStage, newStage)

	def setDifficulty(self, newDifficulty):
		self.pm.write_short(self.addrDifficulty, newDifficulty)

	def setCharacter(self, newCharacter):
		self.pm.write_short(self.addrCharacter, newCharacter)

	def setShotType(self, newShotType):
		self.pm.write_short(self.addrShotType, newShotType)

	def setLives(self, newLives):
		self.pm.write_short(self.addrLives, newLives)

	def setBombs(self, newBombs):
		self.pm.write_short(self.addrBombs, newBombs)

	def setPower(self, newPower):
		self.pm.write_short(self.addrPower, newPower)
	
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

	def setReimuBEasy(self, newReimuBEasy):
		self.pm.write_int(self.addrReimuBEasy, newReimuBEasy)

	def setReimuBNormal(self, newReimuBNormal):
		self.pm.write_int(self.addrReimuBNormal, newReimuBNormal)

	def setReimuBHard(self, newReimuBHard):
		self.pm.write_int(self.addrReimuBHard, newReimuBHard)

	def setReimuBLunatic(self, newReimuBLunatic):
		self.pm.write_int(self.addrReimuBLunatic, newReimuBLunatic)

	def setMarisaAEasy(self, newMarisaAEasy):
		self.pm.write_int(self.addrMarisaAEasy, newMarisaAEasy)

	def setMarisaANormal(self, newMarisaANormal):
		self.pm.write_int(self.addrMarisaANormal, newMarisaANormal)

	def setMarisaAHard(self, newMarisaAHard):
		self.pm.write_int(self.addrMarisaAHard, newMarisaAHard)

	def setMarisaALunatic(self, newMarisaALunatic):
		self.pm.write_int(self.addrMarisaALunatic, newMarisaALunatic)

	def setMarisaBEasy(self, newMarisaBEasy):
		self.pm.write_int(self.addrMarisaBEasy, newMarisaBEasy)

	def setMarisaBNormal(self, newMarisaBNormal):
		self.pm.write_int(self.addrMarisaBNormal, newMarisaBNormal)

	def setMarisaBHard(self, newMarisaBHard):
		self.pm.write_int(self.addrMarisaBHard, newMarisaBHard)

	def setMarisaBLunatic(self, newMarisaBLunatic):
		self.pm.write_int(self.addrMarisaBLunatic, newMarisaBLunatic)

	def resetHpEnemies(self):
		for addr in self.addrHpEnemies:
			self.pm.write_int(addr, 0)

	def setPracticeStageScore(self, characterId, shotId, difficultyId, stageId, newScore):
		return self.pm.write_int(self.addrPracticeScore[characterId][shotId][difficultyId][stageId], newScore)

	def setKill(self, active):
		if active:
			self.pm.write_bytes(self.addrKillCondition, bytes([0x90, 0x90]), 2)
		else:
			self.pm.write_bytes(self.addrKillCondition, bytes([0xEB, 0x22]), 2)

class eosdState:
	"""Class keeping track of what's unlock for the game"""
	lives = None
	bombs = None
	power = None
	endings = None
	stages = None
	continues = None

	hasLunatic = None
	hasHard = None
	hasNormal = None
	hasEasy = None

	hasReimuA = None
	hasReimuB = None
	hasMarisaA = None
	hasMarisaB = None

	gameController = None

	bossBeaten = []

	def __init__(self):
		# Default Value
		self.lives = 0
		self.bombs = 0
		self.power = 0
		self.endings = 0
		self.stages = 1
		self.continues = 0

		self.hasLunatic = True
		self.hasHard = False
		self.hasNormal = False
		self.hasEasy = False

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

		self.gameController = eosdController()

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

	def giveAllResources(self, normalMode = False):
		self.giveLives()
		self.giveBombs()
		self.givePower()

		if normalMode:
			self.giveContinues()
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

		self.updatePracticeScore()

	def updatePracticeScore(self, levelOfSeparation = 0):
		"""
		0: By character
		1: By shot type
		2: By Difficulty
		"""

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

	#
	# Boss
	#

	def isCurrentBossDefeated(self, counter):
		return self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][self.gameController.getDifficulty()][self.gameController.getStage()-1][counter]

	def setbossBeaten(self, counter):
		self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][self.gameController.getDifficulty()][self.gameController.getStage()-1][counter] = True

	def getBossName(self, counter):
		bossName = [
			["Rumia - MidBoss", "Rumia - Boss"],
			["Dayousei", "Cirno"],
			["Meiling - MidBoss", "Meiling - Boss"],
			["Koakuma", "Patchouli"],
			["Sakuya - MidBoss 1", "Sakuya - Boss"],
			["Sakuya - MidBoss 2", "Remilia"]
		]

		return bossName[self.gameController.getStage()-1][counter]

	def isBossBeaten(self, character, stage, counter, shot_type = -1, difficutly = -1):
		if difficutly >= 0 and difficutly < 5:
			flags = [
				self.bossBeaten[character][0][difficutly][stage][counter],
				self.bossBeaten[character][1][difficutly][stage][counter],
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

		if shot_type == 0 or shot_type == 1:
			if shot_type == 0:
				if difficutly >= 0 and difficutly < 5:
					flags = [flags[0]]
				else:
					flags = flags[:3]
			else:
				if difficutly >= 0 and difficutly < 5:
					flags = [flags[1]]
				else:
					flags = flags[-4:]

		isBeaten = False

		for flag in flags:
			if flag:
				isBeaten = True
				break

		return isBeaten

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

		if addInLevel and self.gameController.getGameMode() == 2:
			self.gameController.setLives(self.gameController.getLives() + 1)

	def addBomb(self, addInLevel = True):
		if(self.bombs < 8):
			self.bombs += 1

		if addInLevel and self.gameController.getGameMode() == 2:
			self.gameController.setBombs(self.gameController.getBombs() + 1)

	def add1Power(self, addInLevel = True):
		if(self.power < 128):
			self.power += 1

		if addInLevel and self.gameController.getGameMode() == 2 and self.gameController.getPower() < 128:
			self.gameController.setPower(self.gameController.getPower() + 1)

	def add25Power(self, addInLevel = True):
		if(self.power < 103):
			self.power += 25
		else:
			self.power = 128

		if addInLevel and self.gameController.getGameMode() == 2:
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

	def addEnding(self):
		self.endings += 1

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

	def unlockCharacter(self, character):
		if(character == 0):
			self.hasReimuA = True
		elif(character == 1):
			self.hasReimuB = True
		elif(character == 2):
			self.hasMarisaA = True
		elif(character == 3):
			self.hasMarisaB = True
			
	def reconnect(self):
		try:
			self.gameController = eosdController()
		except Exception as err:
			self.gameController = None