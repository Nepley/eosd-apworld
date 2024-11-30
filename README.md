# Touhou 6 ~ The Embodiment of Scarlet Devil Apworld

This is an implementation of touhou 6 for [Archipelago](https://github.com/ArchipelagoMW/Archipelago)

## Locations
* MidBoss Defeated
* Boss Defeated
* Stage Cleared

## Items
* Characters/Shot Types
* Next Stage
* Pack of 25 Power Points
* Lives
* Bombs
* Lower Difficulty

**Filler**: 1 Power Point

## Options
By default, the game except you to be able to finish the game once you unlock the final stage, you can set the resources needed for the stages 3/4 and stages 5/6.
You can also choose if you must finish the game with just one character or both of them.

## How to use

Launch the client from Archipelago and launch the game. The client should connect to the process of touhou 6 automatically.
Then you can go to the practice mode and start playing. You start with a random character/shot type.

## Known Issues
* If you go to a character/shot type without any stage, you can still confirm and you will go to stage 1. The game is not supposed to have no stage in practice.
* When beating Daiyousei in stage 2, the check can be send a little later than normal if ennemies spawn just after defeating her.
* It's also possible that, sometime, the client will consider a boss beaten while the boss is still alive when the boss go to their next life bar.