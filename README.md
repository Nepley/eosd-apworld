# Touhou 6 ~ The Embodiment of Scarlet Devil Apworld

This is an implementation of touhou 6 for [Archipelago](https://github.com/ArchipelagoMW/Archipelago)<br />
Tracker: https://github.com/Nepley/eosd-poptracker

## How does this randomizer work ?
At the start, you start with only one character and one shot type, with zero resources and with only the Lunatic difficulty.<br />
Each item will make it easier and easier to clear the differents stages.

## Locations
* MidBoss Defeated
* Boss Defeated
* Stage Cleared

## Items
* Characters/Shot Types
* Next Stage (Practice Mode)
* Extra Stage (If enabled)
* Continues (Normal Mode)
* Pack of 25 Power Points
* Lives
* Bombs
* Lower Difficulty

**Filler**: 1 Power Point

## Options
**Mode:** Practice or Normal mode.
With Practice mode, you play stage by stage individually and need to unlock the stages progressively. You can also choose how the stage unlock are grouped (Globally, By character or By Shot Type)<br />
In normal mode, you need to finish the game normally with the resources only given at the start. Futhermore, only the resources act as a gate. If you put everything at minimum in the yaml, the logic consider you can finish at sphere 1.<br />
Normal Mode can be played with a dynamic difficulty or a static one.
* Dynamic: The difficulty will always be the lowest unlocked and will be able to change during a run. Easy difficulty is disabled as it lock access to the final stage.
* Static: The difficulty stay to the one you have selected

**Resources:** You can set the resources needed for the stages 3/4 and stages 5/6.

**Extra Stage:** You can enable the extra stage and choose if it act as the 7th stage or if it is unlocked separately. In normal mode, it is unlocked after clearing the stage 6 if it's not it's own unlock.

**Goal:** If the extra stage is enabled, you can choose which goal you want between Remilia, Flandre or both.

**Endings Required:** If you must clear your goal with just one character, both of them or with all shot type if they are enabled as separate check.

**Shot Type:** If checks are separated by shot type

**Difficulty:** If checks are separated by difficulty. In normal mode, it force the difficulty to be static.

**Traps:** You can choose to have traps replacing a percentages of filler items. You can set the weight of each individual trap

## How to use

**Backup your score.dat if you care about your scores, practice stage access and Extra unlock**

1. Launch the game
2. Connect the client "Touhou EoSD" found in the archipelago launcher to the server.
3. If the message "Touhou EoSD process found. Starting loop..." appeared, you're good to go
