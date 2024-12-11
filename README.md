# Touhou 6 ~ The Embodiment of Scarlet Devil Apworld

This is an implementation of touhou 6 for [Archipelago](https://github.com/ArchipelagoMW/Archipelago)<br />
Tracker: https://github.com/Nepley/eosd-poptracker

## Locations
* MidBoss Defeated
* Boss Defeated
* Stage Cleared

## Items
* Characters/Shot Types
* Next Stage (Practice Mode)
* Continues (Normal Mode)
* Pack of 25 Power Points
* Lives
* Bombs
* Lower Difficulty

**Filler**: 1 Power Point

## Options
You can choose if you want to play in practice mode or normal mode. With Practice mode, you play stage by stage individually and need to unlock the stages. In normal mode, you need to finish the game normally with the resources only given at the start.<br />
In practice mode, by default, the game except you to be able to finish the game once you unlock the final stage, you can set the resources needed for the stages 3/4 and stages 5/6.<br />
In normal mode, only the resources act as a gate. If you put everything at minimum, the logic consider you can finish at sphere 1.<br />
You can also choose if you must finish the game with just one character or both of them.

## How to use

1. Connect the client "Touhou 6" found in the archipelago launcher to the server.
2. Once the message "Waiting for connection to Touhou 6..." appeared, launch the game (you can launch it before)
3. If the message "Touhou 6 process found. Starting loop..." appeared, you're good to go

## Known Issues
* If you go to a character/shot type without any stage, you can still confirm and you will go to stage 1. The game is not supposed to have no stage in practice.
* When beating Daiyousei in stage 2, the check can be send a little later than normal if ennemies spawn just after defeating her.
* It's also possible that, sometime, the client will consider a boss beaten while the boss is still alive when the boss go to their next life bar.
* The demo play can activate the death link if it's active.