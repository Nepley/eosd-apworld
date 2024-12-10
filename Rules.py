from BaseClasses import CollectionState, MultiWorld
from .Regions import connect_regions

def set_rules(multiworld: MultiWorld, player: int):
    lifeMid = getattr(multiworld.worlds[player].options, "number_life_mid")
    bombsMid = getattr(multiworld.worlds[player].options, "number_bomb_mid")
    difficutlyMid = getattr(multiworld.worlds[player].options, "difficulty_mid")
    lifeEnd = getattr(multiworld.worlds[player].options, "number_life_end")
    bombsEnd = getattr(multiworld.worlds[player].options, "number_bomb_end")
    difficutlyEnd = getattr(multiworld.worlds[player].options, "difficulty_end")
    endingRequired = getattr(multiworld.worlds[player].options, "ending_required")
    mode = getattr(multiworld.worlds[player].options, "mode")

    # Stage Access
    # Stage 2
    multiworld.get_location("[Reimu] Daiyousei Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
    multiworld.get_location("[Reimu] Cirno Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
    multiworld.get_location("[Reimu] Stage 2 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
    multiworld.get_location("[Marisa] Daiyousei Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
    multiworld.get_location("[Marisa] Cirno Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
    multiworld.get_location("[Marisa] Stage 2 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1

    # Stage 3
    multiworld.get_location("[Reimu] Meiling - MidBoss", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
    multiworld.get_location("[Reimu] Meiling Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
    multiworld.get_location("[Reimu] Stage 3 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
    multiworld.get_location("[Marisa] Meiling - MidBoss", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
    multiworld.get_location("[Marisa] Meiling Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
    multiworld.get_location("[Marisa] Stage 3 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1

    # Stage 4
    multiworld.get_location("[Reimu] Koakuma Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
    multiworld.get_location("[Reimu] Patchouli Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
    multiworld.get_location("[Reimu] Stage 4 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
    multiworld.get_location("[Marisa] Koakuma Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
    multiworld.get_location("[Marisa] Patchouli Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
    multiworld.get_location("[Marisa] Stage 4 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1

    # Stage 5
    multiworld.get_location("[Reimu] Sakuya - MidBoss 1", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
    multiworld.get_location("[Reimu] Sakuya Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
    multiworld.get_location("[Reimu] Stage 5 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
    multiworld.get_location("[Marisa] Sakuya - MidBoss 1", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
    multiworld.get_location("[Marisa] Sakuya Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
    multiworld.get_location("[Marisa] Stage 5 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1

    # Stage 6
    multiworld.get_location("[Reimu] Sakuya - MidBoss 2", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
    multiworld.get_location("[Reimu] Remilia Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
    multiworld.get_location("[Reimu] Stage 6 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
    multiworld.get_location("[Marisa] Sakuya - MidBoss 2", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
    multiworld.get_location("[Marisa] Remilia Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
    multiworld.get_location("[Marisa] Stage 6 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1

    connect_regions(multiworld, player, "Menu", "Reimu", lambda state: state.has("Reimu A - Homing Amulet", player) or state.has("Reimu B - Persuasion Needle", player, 1))
    connect_regions(multiworld, player, "Menu", "Marisa", lambda state: state.has("Marisa A - Magic Missile", player) or state.has("Marisa B - Illusion Laser", player, 1))
    connect_regions(multiworld, player, "Reimu", "Reimu - Early", None)
    connect_regions(multiworld, player, "Marisa", "Marisa - Early", None)
    connect_regions(multiworld, player, "Reimu - Early", "Reimu - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
    connect_regions(multiworld, player, "Marisa - Early", "Marisa - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
    connect_regions(multiworld, player, "Reimu - Mid", "Reimu - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
    connect_regions(multiworld, player, "Marisa - Mid", "Marisa - End", lambda state: state.count("Life", player) >= lifeEnd and state.count("Bomb", player) >= bombsEnd and state.count("Lower Difficulty", player) >= difficutlyEnd)

    # Win condition.
    multiworld.completion_condition[player] = lambda state: state.count("Ending", player) >= endingRequired