# Touhou 6 ~ The Embodiment of Scarlet Devil Apworld

This is an implementation of touhou 6 for [Archipelago](https://github.com/ArchipelagoMW/Archipelago)<br />
Tracker: https://github.com/Nepley/eosd-poptracker

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
By default, the game except you to be able to finish the game once you unlock the final stage, you can set the resources needed for the stages 3/4 and stages 5/6.<br />
You can also choose if you must finish the game with just one character or both of them.

## How to use

1. Connect the client "Touhou 6" found in the archipelago launcher to the server.
2. Once the message "Waiting for connection to Touhou 6..." appeared, launch the game (you can launch it before)
3. If the message "Touhou 6 process found. Starting loop..." appeared, you're good to go

**You need to have your system locale set to Japanese**

Here the step for Windows 11:
1. Go to 'Control Panel' -> 'Time & language' -> 'Region' ->  'Language & Region'
2. In the Related settings, select 'Administrative Language settings'
3. Go to the Administrative tab and click on 'Change system locale'
4. Choose Japanese (Japan) and reboot Windows

## Known Issues
* If you go to a character/shot type without any stage, you can still confirm and you will go to stage 1. The game is not supposed to have no stage in practice.
* When beating Daiyousei in stage 2, the check can be send a little later than normal if ennemies spawn just after defeating her.
* It's also possible that, sometime, the client will consider a boss beaten while the boss is still alive when the boss go to their next life bar.