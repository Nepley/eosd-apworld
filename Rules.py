from BaseClasses import CollectionState, MultiWorld
from .Regions import connect_regions

def set_rules(multiworld: MultiWorld, player: int):
    lifeMid = getattr(multiworld.worlds[player].options, "number_life_mid")
    bombsMid = getattr(multiworld.worlds[player].options, "number_bomb_mid")
    difficutlyMid = getattr(multiworld.worlds[player].options, "difficulty_mid")
    lifeEnd = getattr(multiworld.worlds[player].options, "number_life_end")
    bombsEnd = getattr(multiworld.worlds[player].options, "number_bomb_end")
    difficutlyEnd = getattr(multiworld.worlds[player].options, "difficulty_end")
    lifeExtra = getattr(multiworld.worlds[player].options, "number_life_extra")
    bombsExtra = getattr(multiworld.worlds[player].options, "number_bomb_extra")
    endingRequired = getattr(multiworld.worlds[player].options, "ending_required")
    mode = getattr(multiworld.worlds[player].options, "mode")
    shot_type = getattr(multiworld.worlds[player].options, "shot_type")
    difficulty_check = getattr(multiworld.worlds[player].options, "difficulty_check")
    goal = getattr(multiworld.worlds[player].options, "goal")
    extra = getattr(multiworld.worlds[player].options, "extra_stage")

    # Stage Access
    # Stage 1
    if difficulty_check:
        if shot_type:
            multiworld.get_location("[Easy][Reimu A] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu A] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa A] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa A] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu A] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu A] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu A] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu A] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Easy][Reimu B] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu B] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa B] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa B] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu B] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu B] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu B] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu B] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1
        else:
            multiworld.get_location("[Easy][Reimu] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Rumia - MidBoss", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Rumia Defeated", player).access_rule = lambda state: state.count("Lower Difficulty", player) >= 1

    # Stage 2
    if difficulty_check:
        if shot_type:
            multiworld.get_location("[Easy][Reimu A] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu A] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa A] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa A] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu A] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu A] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu A] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu A] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu A] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu A] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa A] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa A] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0

            multiworld.get_location("[Easy][Reimu B] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu B] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa B] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa B] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu B] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu B] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu B] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu B] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu B] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu B] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa B] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa B] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
        else:
            multiworld.get_location("[Easy][Reimu] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa] Daiyousei Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa] Cirno Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 1 or mode == 1) and state.count("Lower Difficulty", player) >= 0
    else:
        if shot_type:
            multiworld.get_location("[Reimu A] Daiyousei Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
            multiworld.get_location("[Reimu A] Cirno Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
            multiworld.get_location("[Reimu B] Daiyousei Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
            multiworld.get_location("[Reimu B] Cirno Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
            multiworld.get_location("[Marisa A] Daiyousei Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
            multiworld.get_location("[Marisa A] Cirno Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
            multiworld.get_location("[Marisa B] Daiyousei Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
            multiworld.get_location("[Marisa B] Cirno Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
        else:
            multiworld.get_location("[Reimu] Daiyousei Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
            multiworld.get_location("[Reimu] Cirno Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
            multiworld.get_location("[Marisa] Daiyousei Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
            multiworld.get_location("[Marisa] Cirno Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1

    # Stage 3
    if difficulty_check:
        if shot_type:
            multiworld.get_location("[Easy][Reimu A] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu A] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu B] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu B] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa A] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa A] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa B] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa B] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu A] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu A] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu B] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu B] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu A] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu A] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu B] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu B] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu A] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu A] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu B] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu B] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa A] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa A] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa B] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa B] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
        else:
            multiworld.get_location("[Easy][Reimu] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa] Meiling - MidBoss", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa] Meiling Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 2 or mode == 1) and state.count("Lower Difficulty", player) >= 0
    else:
        if shot_type:
            multiworld.get_location("[Reimu A] Meiling - MidBoss", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
            multiworld.get_location("[Reimu A] Meiling Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
            multiworld.get_location("[Reimu B] Meiling - MidBoss", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
            multiworld.get_location("[Reimu B] Meiling Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
            multiworld.get_location("[Marisa A] Meiling - MidBoss", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
            multiworld.get_location("[Marisa A] Meiling Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
            multiworld.get_location("[Marisa B] Meiling - MidBoss", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
            multiworld.get_location("[Marisa B] Meiling Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
        else:
            multiworld.get_location("[Reimu] Meiling - MidBoss", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
            multiworld.get_location("[Reimu] Meiling Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
            multiworld.get_location("[Marisa] Meiling - MidBoss", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
            multiworld.get_location("[Marisa] Meiling Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1

    # Stage 4
    if difficulty_check:
        if shot_type:
            multiworld.get_location("[Easy][Reimu A] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu A] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu B] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu B] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa A] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa A] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa B] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa B] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu A] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu A] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu B] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu B] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu A] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu A] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu B] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu B] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu A] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu A] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu B] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu B] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa A] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa A] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa B] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa B] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
        else:
            multiworld.get_location("[Easy][Reimu] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa] Koakuma Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa] Patchouli Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 3 or mode == 1) and state.count("Lower Difficulty", player) >= 0
    else:
        if shot_type:
            multiworld.get_location("[Reimu A] Koakuma Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
            multiworld.get_location("[Reimu A] Patchouli Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
            multiworld.get_location("[Reimu B] Koakuma Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
            multiworld.get_location("[Reimu B] Patchouli Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
            multiworld.get_location("[Marisa A] Koakuma Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
            multiworld.get_location("[Marisa A] Patchouli Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
            multiworld.get_location("[Marisa B] Koakuma Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
            multiworld.get_location("[Marisa B] Patchouli Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
        else:
            multiworld.get_location("[Reimu] Koakuma Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
            multiworld.get_location("[Reimu] Patchouli Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
            multiworld.get_location("[Marisa] Koakuma Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
            multiworld.get_location("[Marisa] Patchouli Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1

    # Stage 5
    if difficulty_check:
        if shot_type:
            multiworld.get_location("[Easy][Reimu A] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu A] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu B] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu B] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa A] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa A] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa B] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa B] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu A] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu A] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu B] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu B] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu A] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu A] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu B] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu B] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu A] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu A] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu B] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu B] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa A] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa A] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa B] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa B] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
        else:
            multiworld.get_location("[Easy][Reimu] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Reimu] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3
            multiworld.get_location("[Easy][Marisa] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 3

            multiworld.get_location("[Normal][Reimu] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa] Sakuya - MidBoss 1", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa] Sakuya Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 4 or mode == 1) and state.count("Lower Difficulty", player) >= 0
    else:
        if shot_type:
            multiworld.get_location("[Reimu A] Sakuya - MidBoss 1", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
            multiworld.get_location("[Reimu A] Sakuya Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
            multiworld.get_location("[Reimu B] Sakuya - MidBoss 1", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
            multiworld.get_location("[Reimu B] Sakuya Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
            multiworld.get_location("[Marisa A] Sakuya - MidBoss 1", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
            multiworld.get_location("[Marisa A] Sakuya Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
            multiworld.get_location("[Marisa B] Sakuya - MidBoss 1", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
            multiworld.get_location("[Marisa B] Sakuya Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
        else:
            multiworld.get_location("[Reimu] Sakuya - MidBoss 1", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
            multiworld.get_location("[Reimu] Sakuya Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
            multiworld.get_location("[Marisa] Sakuya - MidBoss 1", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
            multiworld.get_location("[Marisa] Sakuya Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1

    # Stage 6
    if difficulty_check:
        if shot_type:
            multiworld.get_location("[Normal][Reimu A] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu A] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu B] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu B] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa A] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa B] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu A] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu A] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu B] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu B] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa A] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa B] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu A] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu A] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu B] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu B] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa A] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa A] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa B] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa B] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
        else:
            multiworld.get_location("[Normal][Reimu] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Reimu] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2
            multiworld.get_location("[Normal][Marisa] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 2

            multiworld.get_location("[Hard][Reimu] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Reimu] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1
            multiworld.get_location("[Hard][Marisa] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 1

            multiworld.get_location("[Lunatic][Reimu] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Reimu] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa] Sakuya - MidBoss 2", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
            multiworld.get_location("[Lunatic][Marisa] Remilia Defeated", player).access_rule = lambda state: (state.count("Next Stage", player) >= 5 or mode == 1) and state.count("Lower Difficulty", player) >= 0
    else:
        if shot_type:
            multiworld.get_location("[Reimu A] Sakuya - MidBoss 2", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
            multiworld.get_location("[Reimu A] Remilia Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
            multiworld.get_location("[Reimu B] Sakuya - MidBoss 2", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
            multiworld.get_location("[Reimu B] Remilia Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
            multiworld.get_location("[Marisa A] Sakuya - MidBoss 2", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
            multiworld.get_location("[Marisa A] Remilia Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
            multiworld.get_location("[Marisa B] Sakuya - MidBoss 2", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
            multiworld.get_location("[Marisa B] Remilia Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
        else:
            multiworld.get_location("[Reimu] Sakuya - MidBoss 2", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
            multiworld.get_location("[Reimu] Remilia Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
            multiworld.get_location("[Marisa] Sakuya - MidBoss 2", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
            multiworld.get_location("[Marisa] Remilia Defeated", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1

    # Stage Clear
    if shot_type:
        multiworld.get_location("[Reimu A] Stage 1 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 0 or mode == 1
        multiworld.get_location("[Reimu A] Stage 2 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
        multiworld.get_location("[Reimu A] Stage 3 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
        multiworld.get_location("[Reimu A] Stage 4 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
        multiworld.get_location("[Reimu A] Stage 5 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
        multiworld.get_location("[Reimu A] Stage 6 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
        multiworld.get_location("[Reimu B] Stage 1 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 0 or mode == 1
        multiworld.get_location("[Reimu B] Stage 2 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
        multiworld.get_location("[Reimu B] Stage 3 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
        multiworld.get_location("[Reimu B] Stage 4 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
        multiworld.get_location("[Reimu B] Stage 5 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
        multiworld.get_location("[Reimu B] Stage 6 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1

        multiworld.get_location("[Marisa A] Stage 1 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 0 or mode == 1
        multiworld.get_location("[Marisa A] Stage 2 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
        multiworld.get_location("[Marisa A] Stage 3 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
        multiworld.get_location("[Marisa A] Stage 4 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
        multiworld.get_location("[Marisa A] Stage 5 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
        multiworld.get_location("[Marisa A] Stage 6 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
        multiworld.get_location("[Marisa B] Stage 1 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 0 or mode == 1
        multiworld.get_location("[Marisa B] Stage 2 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
        multiworld.get_location("[Marisa B] Stage 3 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
        multiworld.get_location("[Marisa B] Stage 4 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
        multiworld.get_location("[Marisa B] Stage 5 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
        multiworld.get_location("[Marisa B] Stage 6 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1
    else:
        multiworld.get_location("[Reimu] Stage 1 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 0 or mode == 1
        multiworld.get_location("[Reimu] Stage 2 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
        multiworld.get_location("[Reimu] Stage 3 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
        multiworld.get_location("[Reimu] Stage 4 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
        multiworld.get_location("[Reimu] Stage 5 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
        multiworld.get_location("[Reimu] Stage 6 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1

        multiworld.get_location("[Marisa] Stage 1 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 0 or mode == 1
        multiworld.get_location("[Marisa] Stage 2 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 1 or mode == 1
        multiworld.get_location("[Marisa] Stage 3 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 2 or mode == 1
        multiworld.get_location("[Marisa] Stage 4 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 3 or mode == 1
        multiworld.get_location("[Marisa] Stage 5 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 4 or mode == 1
        multiworld.get_location("[Marisa] Stage 6 Clear", player).access_rule = lambda state: state.count("Next Stage", player) >= 5 or mode == 1

    # Stage Extra
    if extra != 0:
        rules = lambda state: state.count("Next Stage", player) >= 6 or mode == 1 if extra == 1 else state.has("Extra Stage", player, 1)

        if shot_type:
            multiworld.get_location("[Reimu A] Patchouli - MidBoss", player).access_rule = rules
            multiworld.get_location("[Reimu A] Flandre Defeated", player).access_rule = rules
            multiworld.get_location("[Reimu A] Stage Extra Clear", player).access_rule = rules
            multiworld.get_location("[Reimu B] Patchouli - MidBoss", player).access_rule = rules
            multiworld.get_location("[Reimu B] Flandre Defeated", player).access_rule = rules
            multiworld.get_location("[Reimu B] Stage Extra Clear", player).access_rule = rules
            multiworld.get_location("[Marisa A] Patchouli - MidBoss", player).access_rule = rules
            multiworld.get_location("[Marisa A] Flandre Defeated", player).access_rule = rules
            multiworld.get_location("[Marisa A] Stage Extra Clear", player).access_rule = rules
            multiworld.get_location("[Marisa B] Patchouli - MidBoss", player).access_rule = rules
            multiworld.get_location("[Marisa B] Flandre Defeated", player).access_rule = rules
            multiworld.get_location("[Marisa B] Stage Extra Clear", player).access_rule = rules
        else:
            multiworld.get_location("[Reimu] Patchouli - MidBoss", player).access_rule = rules
            multiworld.get_location("[Reimu] Flandre Defeated", player).access_rule = rules
            multiworld.get_location("[Reimu] Stage Extra Clear", player).access_rule = rules
            multiworld.get_location("[Marisa] Patchouli - MidBoss", player).access_rule = rules
            multiworld.get_location("[Marisa] Flandre Defeated", player).access_rule = rules
            multiworld.get_location("[Marisa] Stage Extra Clear", player).access_rule = rules

    # Regions
    if difficulty_check:
        if shot_type:
            connect_regions(multiworld, player, "Menu", "Reimu - A", lambda state: state.has("Reimu A - Homing Amulet", player))
            connect_regions(multiworld, player, "Menu", "Reimu - B", lambda state: state.has("Reimu B - Persuasion Needle", player))
            connect_regions(multiworld, player, "Menu", "Marisa - A", lambda state: state.has("Marisa A - Magic Missile", player))
            connect_regions(multiworld, player, "Menu", "Marisa - B", lambda state: state.has("Marisa B - Illusion Laser", player))
            connect_regions(multiworld, player, "Reimu - A", "Reimu - A - Early", None)
            connect_regions(multiworld, player, "Reimu - A", "Easy - Reimu - A - Early", None)
            connect_regions(multiworld, player, "Reimu - A", "Normal - Reimu - A - Early", None)
            connect_regions(multiworld, player, "Reimu - A", "Hard - Reimu - A - Early", None)
            connect_regions(multiworld, player, "Reimu - A", "Lunatic - Reimu - A - Early", None)

            connect_regions(multiworld, player, "Reimu - B", "Reimu - B - Early", None)
            connect_regions(multiworld, player, "Reimu - B", "Easy - Reimu - B - Early", None)
            connect_regions(multiworld, player, "Reimu - B", "Normal - Reimu - B - Early", None)
            connect_regions(multiworld, player, "Reimu - B", "Hard - Reimu - B - Early", None)
            connect_regions(multiworld, player, "Reimu - B", "Lunatic - Reimu - B - Early", None)

            connect_regions(multiworld, player, "Marisa - A", "Marisa - A - Early", None)
            connect_regions(multiworld, player, "Marisa - A", "Easy - Marisa - A - Early", None)
            connect_regions(multiworld, player, "Marisa - A", "Normal - Marisa - A - Early", None)
            connect_regions(multiworld, player, "Marisa - A", "Hard - Marisa - A - Early", None)
            connect_regions(multiworld, player, "Marisa - A", "Lunatic - Marisa - A - Early", None)

            connect_regions(multiworld, player, "Marisa - B", "Marisa - B - Early", None)
            connect_regions(multiworld, player, "Marisa - B", "Easy - Marisa - B - Early", None)
            connect_regions(multiworld, player, "Marisa - B", "Normal - Marisa - B - Early", None)
            connect_regions(multiworld, player, "Marisa - B", "Hard - Marisa - B - Early", None)
            connect_regions(multiworld, player, "Marisa - B", "Lunatic - Marisa - B - Early", None)

            connect_regions(multiworld, player, "Reimu - A - Early", "Reimu - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Reimu - A - Mid", "Reimu - A - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Easy - Reimu - A - Early", "Easy - Reimu - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Easy - Reimu - A - Mid", "Easy - Reimu - A - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Reimu - A - Early", "Normal - Reimu - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Reimu - A - Mid", "Normal - Reimu - A - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Reimu - A - Early", "Hard - Reimu - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Reimu - A - Mid", "Hard - Reimu - A - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Reimu - A - Early", "Lunatic - Reimu - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Reimu - A - Mid", "Lunatic - Reimu - A - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)

            connect_regions(multiworld, player, "Reimu - B - Early", "Reimu - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Reimu - B - Mid", "Reimu - B - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Easy - Reimu - B - Early", "Easy - Reimu - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Easy - Reimu - B - Mid", "Easy - Reimu - B - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Reimu - B - Early", "Normal - Reimu - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Reimu - B - Mid", "Normal - Reimu - B - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Reimu - B - Early", "Hard - Reimu - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Reimu - B - Mid", "Hard - Reimu - B - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Reimu - B - Early", "Lunatic - Reimu - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Reimu - B - Mid", "Lunatic - Reimu - B - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)

            connect_regions(multiworld, player, "Marisa - A - Early", "Marisa - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Marisa - A - Mid", "Marisa - A - End", lambda state: state.count("Life", player) >= lifeEnd and state.count("Bomb", player) >= bombsEnd and state.count("Lower Difficulty", player) >= difficutlyEnd)
            connect_regions(multiworld, player, "Easy - Marisa - A - Early", "Easy - Marisa - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Easy - Marisa - A - Mid", "Easy - Marisa - A - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Marisa - A - Early", "Normal - Marisa - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Marisa - A - Mid", "Normal - Marisa - A - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Marisa - A - Early", "Hard - Marisa - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Marisa - A - Mid", "Hard - Marisa - A - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Marisa - A - Early", "Lunatic - Marisa - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Marisa - A - Mid", "Lunatic - Marisa - A - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)

            connect_regions(multiworld, player, "Marisa - B - Early", "Marisa - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Marisa - B - Mid", "Marisa - B - End", lambda state: state.count("Life", player) >= lifeEnd and state.count("Bomb", player) >= bombsEnd and state.count("Lower Difficulty", player) >= difficutlyEnd)
            connect_regions(multiworld, player, "Easy - Marisa - B - Early", "Easy - Marisa - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Easy - Marisa - B - Mid", "Easy - Marisa - B - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Marisa - B - Early", "Normal - Marisa - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Marisa - B - Mid", "Normal - Marisa - B - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Marisa - B - Early", "Hard - Marisa - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Marisa - B - Mid", "Hard - Marisa - B - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Marisa - B - Early", "Lunatic - Marisa - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Marisa - B - Mid", "Lunatic - Marisa - B - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)

            if extra != 0:
                connect_regions(multiworld, player, "Reimu - A", "Reimu - A - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)
                connect_regions(multiworld, player, "Reimu - B", "Reimu - B - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)
                connect_regions(multiworld, player, "Marisa - A", "Marisa - A - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)
                connect_regions(multiworld, player, "Marisa - B", "Marisa - B - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)
        else:
            connect_regions(multiworld, player, "Menu", "Reimu", lambda state: state.has("Reimu A - Homing Amulet", player) or state.has("Reimu B - Persuasion Needle", player, 1))
            connect_regions(multiworld, player, "Menu", "Marisa", lambda state: state.has("Marisa A - Magic Missile", player) or state.has("Marisa B - Illusion Laser", player, 1))
            connect_regions(multiworld, player, "Reimu", "Reimu - Early", None)
            connect_regions(multiworld, player, "Reimu", "Easy - Reimu - Early", None)
            connect_regions(multiworld, player, "Reimu", "Normal - Reimu - Early", None)
            connect_regions(multiworld, player, "Reimu", "Hard - Reimu - Early", None)
            connect_regions(multiworld, player, "Reimu", "Lunatic - Reimu - Early", None)

            connect_regions(multiworld, player, "Marisa", "Marisa - Early", None)
            connect_regions(multiworld, player, "Marisa", "Easy - Marisa - Early", None)
            connect_regions(multiworld, player, "Marisa", "Normal - Marisa - Early", None)
            connect_regions(multiworld, player, "Marisa", "Hard - Marisa - Early", None)
            connect_regions(multiworld, player, "Marisa", "Lunatic - Marisa - Early", None)

            connect_regions(multiworld, player, "Reimu - Early", "Reimu - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Reimu - Mid", "Reimu - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Easy - Reimu - Early", "Easy - Reimu - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Easy - Reimu - Mid", "Easy - Reimu - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Reimu - Early", "Normal - Reimu - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Reimu - Mid", "Normal - Reimu - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Reimu - Early", "Hard - Reimu - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Reimu - Mid", "Hard - Reimu - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Reimu - Early", "Lunatic - Reimu - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Reimu - Mid", "Lunatic - Reimu - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)

            connect_regions(multiworld, player, "Marisa - Early", "Marisa - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Marisa - Mid", "Marisa - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Easy - Marisa - Early", "Easy - Marisa - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Easy - Marisa - Mid", "Easy - Marisa - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Marisa - Early", "Normal - Marisa - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Normal - Marisa - Mid", "Normal - Marisa - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Marisa - Early", "Hard - Marisa - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Hard - Marisa - Mid", "Hard - Marisa - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Marisa - Early", "Lunatic - Marisa - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Lunatic - Marisa - Mid", "Lunatic - Marisa - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)

            if extra != 0:
                connect_regions(multiworld, player, "Reimu", "Reimu - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)
                connect_regions(multiworld, player, "Marisa", "Marisa - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)

    else:
        if shot_type:
            connect_regions(multiworld, player, "Menu", "Reimu - A", lambda state: state.has("Reimu A - Homing Amulet", player))
            connect_regions(multiworld, player, "Menu", "Reimu - B", lambda state: state.has("Reimu B - Persuasion Needle", player))
            connect_regions(multiworld, player, "Menu", "Marisa - A", lambda state: state.has("Marisa A - Magic Missile", player))
            connect_regions(multiworld, player, "Menu", "Marisa - B", lambda state: state.has("Marisa B - Illusion Laser", player))
            connect_regions(multiworld, player, "Reimu - A", "Reimu - A - Early", None)
            connect_regions(multiworld, player, "Reimu - B", "Reimu - B - Early", None)
            connect_regions(multiworld, player, "Marisa - A", "Marisa - A - Early", None)
            connect_regions(multiworld, player, "Marisa - B", "Marisa - B - Early", None)
            connect_regions(multiworld, player, "Reimu - A - Early", "Reimu - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Reimu - B - Early", "Reimu - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Marisa - A - Early", "Marisa - A - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Marisa - B - Early", "Marisa - B - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Reimu - A - Mid", "Reimu - A - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Reimu - B - Mid", "Reimu - B - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Marisa - A - Mid", "Marisa - A - End", lambda state: state.count("Life", player) >= lifeEnd and state.count("Bomb", player) >= bombsEnd and state.count("Lower Difficulty", player) >= difficutlyEnd)
            connect_regions(multiworld, player, "Marisa - B - Mid", "Marisa - B - End", lambda state: state.count("Life", player) >= lifeEnd and state.count("Bomb", player) >= bombsEnd and state.count("Lower Difficulty", player) >= difficutlyEnd)

            if extra != 0:
                connect_regions(multiworld, player, "Reimu - A", "Reimu - A - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)
                connect_regions(multiworld, player, "Reimu - B", "Reimu - B - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)
                connect_regions(multiworld, player, "Marisa - A", "Marisa - A - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)
                connect_regions(multiworld, player, "Marisa - B", "Marisa - B - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)
        else:
            connect_regions(multiworld, player, "Menu", "Reimu", lambda state: state.has("Reimu A - Homing Amulet", player) or state.has("Reimu B - Persuasion Needle", player, 1))
            connect_regions(multiworld, player, "Menu", "Marisa", lambda state: state.has("Marisa A - Magic Missile", player) or state.has("Marisa B - Illusion Laser", player, 1))
            connect_regions(multiworld, player, "Reimu", "Reimu - Early", None)
            connect_regions(multiworld, player, "Marisa", "Marisa - Early", None)
            connect_regions(multiworld, player, "Reimu - Early", "Reimu - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Marisa - Early", "Marisa - Mid", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Reimu - Mid", "Reimu - End", lambda state: state.count("Life", player) >= lifeMid and state.count("Bomb", player) >= bombsMid and state.count("Lower Difficulty", player) >= difficutlyMid)
            connect_regions(multiworld, player, "Marisa - Mid", "Marisa - End", lambda state: state.count("Life", player) >= lifeEnd and state.count("Bomb", player) >= bombsEnd and state.count("Lower Difficulty", player) >= difficutlyEnd)

            if extra != 0:
                connect_regions(multiworld, player, "Reimu", "Reimu - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)
                connect_regions(multiworld, player, "Marisa", "Marisa - Extra", lambda state: state.count("Life", player) >= lifeExtra and state.count("Bomb", player) >= bombsExtra)

    # Failsafe if the ending required is set to all shot type and the shot type are not their own checks.
    if not shot_type and endingRequired == 2:
        endingRequired = 1

    # Win condition.
    if goal == 0 or extra == 0: # Remilia
        if endingRequired == 0: # One
            multiworld.completion_condition[player] = lambda state: state.has("[Reimu] Ending - Remilia", player) or state.has("[Marisa] Ending - Remilia", player)
        elif endingRequired == 1: # Both characters
            multiworld.completion_condition[player] = lambda state: state.has("[Reimu] Ending - Remilia", player) and state.has("[Marisa] Ending - Remilia", player)
        elif endingRequired == 2: # All Shot type
            multiworld.completion_condition[player] = lambda state: state.count("[Reimu] Ending - Remilia", player) >= 2 and state.count("[Marisa] Ending - Remilia", player) >= 2
    elif goal == 1: # Flandre
        if endingRequired == 0: # One
            multiworld.completion_condition[player] = lambda state: state.has("[Reimu] Ending - Flandre", player) or state.has("[Marisa] Ending - Flandre", player)
        elif endingRequired == 1: # Both characters
            multiworld.completion_condition[player] = lambda state: state.has("[Reimu] Ending - Flandre", player) and state.has("[Marisa] Ending - Flandre", player)
        elif endingRequired == 2: # All Shot type
            multiworld.completion_condition[player] = lambda state: state.count("[Reimu] Ending - Flandre", player) >= 2 and state.count("[Marisa] Ending - Flandre", player) >= 2
    elif goal == 2: # Both
        if endingRequired == 0: # One
            multiworld.completion_condition[player] = lambda state: (state.has("[Reimu] Ending - Remilia", player) or state.has("[Marisa] Ending - Remilia", player)) and (state.has("[Reimu] Ending - Flandre", player) or state.has("[Marisa] Ending - Flandre", player))
        elif endingRequired == 1: # Both characters
            multiworld.completion_condition[player] = lambda state: (state.has("[Reimu] Ending - Remilia", player) and state.has("[Marisa] Ending - Remilia", player)) and (state.has("[Reimu] Ending - Flandre", player) and state.has("[Marisa] Ending - Flandre", player))
        elif endingRequired == 2: # All Shot type
            multiworld.completion_condition[player] = lambda state: (state.count("[Reimu] Ending - Remilia", player) >= 2 and state.count("[Marisa] Ending - Remilia", player) >= 2) and (state.count("[Reimu] Ending - Flandre", player) >= 2 and state.count("[Marisa] Ending - Flandre", player) >= 2)