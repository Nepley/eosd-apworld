import pymem
from .Variables import *

class gameController:
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

	# Starting Resources
	addrPracticeStartingLives = None
	addrNormalStartingLives = None
	addrPracticeStartingLives = None
	addrNormalStartingBombs = None
	addrRespawnBombs = None

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

	# FPS
	addrFpsText = None
	addrFpsUpdate = None

	# Other
	addrControllerHandle = None
	addrInput = None
	addrGameMode = None
	addrMenu = None
	addrMenuCursor = None
	addrInDemo = None
	addrIsBossPresent = None
	addrKillCondition = None
	addrCharacterLock = None
	addrForceExtra = None

	# Sound
	addrCustomSoundId = None
	addrSoundHack1 = None
	addrSoundHack2 = None

	# Difficulty
	addrDifficultyDown = None
	addrDifficultyUp = None
	addrDifficutlyCondition = None

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

		self.addrPracticeStartingLives = self.pm.base_address+ADDR_PRACTICE_STARTING_LIVES
		self.addrNormalStartingLives = self.pm.base_address+ADDR_NORMAL_STARTING_LIVES
		self.addrPracticeStartingBombs = self.pm.base_address+ADDR_PRACTICE_STARTING_BOMBS
		self.addrNormalStartingBombs = self.pm.base_address+ADDR_NORMAL_STARTING_BOMBS
		self.addrRespawnBombs = self.pm.base_address+ADDR_RESPAWN_BOMBS

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

		self.addrFpsText = self.pm.base_address+ADDR_FPS_TEXT
		self.addrFpsUpdate = self.pm.base_address+ADDR_FPS_UPDATE

		self.addrDifficultyDown = self.pm.base_address+ADDR_DIFFICULTY_DOWN
		self.addrDifficultyUp = self.pm.base_address+ADDR_DIFFICULTY_UP
		self.addrDifficutlyCondition = self.pm.base_address+ADDR_DIFFICULTY_CONDITION

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

	def getDifficultyDown(self):
		return int.from_bytes(self.pm.read_bytes(self.addrDifficultyDown, 1))

	def getDifficultyUp(self):
		return int.from_bytes(self.pm.read_bytes(self.addrDifficultyUp, 1))

	def getFpsText(self):
		return self.pm.read_bytes(self.addrFpsText, 8)

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

	def setPracticeStartingLives(self, newPracticeStartingLives):
		self.pm.write_bytes(self.addrPracticeStartingLives, bytes([newPracticeStartingLives]), 1)

	def setNormalStartingLives(self, newNormalStartingLives):
		self.pm.write_bytes(self.addrNormalStartingLives, bytes([newNormalStartingLives]), 1)

	def setPracticeStartingBombs(self, newPracticeStartingBombs):
		self.pm.write_bytes(self.addrPracticeStartingBombs, bytes([newPracticeStartingBombs]), 1)

	def setNormalStartingBombs(self, newNormalStartingBombs):
		self.pm.write_bytes(self.addrNormalStartingBombs, bytes([newNormalStartingBombs]), 1)

	def setRespawnBombs(self, newRespawnBombs):
		self.pm.write_bytes(self.addrRespawnBombs, bytes([newRespawnBombs]), 1)

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

	def setFpsText(self, newFpsText):
		# If we have less than 8 character, we pad space character
		if len(newFpsText) < 8:
			for char in range(0, (8-len(newFpsText))):
				newFpsText.insert(0, 0xD6)
		self.pm.write_bytes(self.addrFpsText, bytes(newFpsText), 8)

	def setCharacterDifficulty(self, character, shot, difficulty, newValue):
		if character == REIMU:
			if shot == SHOT_A:
				if difficulty == EASY:
					self.setReimuAEasy(newValue)
				elif difficulty == NORMAL:
					self.setReimuANormal(newValue)
				elif difficulty == HARD:
					self.setReimuAHard(newValue)
				elif difficulty == LUNATIC:
					self.setReimuALunatic(newValue)
				elif difficulty == EXTRA:
					self.setReimuAExtra(newValue)
			else:
				if difficulty == EASY:
					self.setReimuBEasy(newValue)
				elif difficulty == NORMAL:
					self.setReimuBNormal(newValue)
				elif difficulty == HARD:
					self.setReimuBHard(newValue)
				elif difficulty == LUNATIC:
					self.setReimuBLunatic(newValue)
				elif difficulty == EXTRA:
					self.setReimuBExtra(newValue)
		else:
			if shot == SHOT_A:
				if difficulty == EASY:
					self.setMarisaAEasy(newValue)
				elif difficulty == NORMAL:
					self.setMarisaANormal(newValue)
				elif difficulty == HARD:
					self.setMarisaAHard(newValue)
				elif difficulty == LUNATIC:
					self.setMarisaALunatic(newValue)
				elif difficulty == EXTRA:
					self.setMarisaAExtra(newValue)
			else:
				if difficulty == EASY:
					self.setMarisaBEasy(newValue)
				elif difficulty == NORMAL:
					self.setMarisaBNormal(newValue)
				elif difficulty == HARD:
					self.setMarisaBHard(newValue)
				elif difficulty == LUNATIC:
					self.setMarisaBLunatic(newValue)
				elif difficulty == EXTRA:
					self.setMarisaBExtra(newValue)

	def setInput(self, newInput):
		self.pm.write_bytes(self.addrInput, bytes([newInput]), 1)

	def setDifficultyDown(self, difficultyDown):
		self.pm.write_bytes(self.addrDifficultyDown, bytes([difficultyDown]), 1)

	def setDifficultyUp(self, difficultyUp):
		self.pm.write_bytes(self.addrDifficultyUp, bytes([difficultyUp]), 1)

	def setNormalSpeed(self, newNormalSpeed):
		self.pm.write_bytes(self.addrNormalSpeed, newNormalSpeed.to_bytes(2), 2)

	def setFocusSpeed(self, newFocusSpeed):
		self.pm.write_bytes(self.addrFocusSpeed, newFocusSpeed.to_bytes(2), 2)

	def setNormalSpeedD(self, newNormalSpeedD):
		self.pm.write_bytes(self.addrNormalSpeedD, newNormalSpeedD.to_bytes(2), 2)

	def setFocusSpeedD(self, newFocusSpeedD):
		self.pm.write_bytes(self.addrFocusSpeedD, newFocusSpeedD.to_bytes(2), 2)

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

	def initDifficultyHack(self):
		self.pm.write_bytes(self.addrDifficutlyCondition, bytes([0xC6, 0x80]), 2)

	def setFpsUpdate(self, active):
		if active:
			self.pm.write_bytes(self.addrFpsUpdate, bytes([0xE8, 0x88, 0x83, 0x03, 0x00]), 5)
		else:
			self.pm.write_bytes(self.addrFpsUpdate, bytes([0x90, 0x90, 0x90, 0x90, 0x90]), 5)