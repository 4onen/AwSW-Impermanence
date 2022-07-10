label impermanence_four_remy_c2picturesseenskip:
    python:
        remy2pictures = False
        remy2pictures2 = True
        remy2picturesn = 2
    jump impermanence_four_remy_c2picturesseenskip_return


label impermanence_four_remy_c3endingmenu:
    python:
        # Break base game
        remy3choiceyes = False
        # Fixup chapter2 pictures not always existing
        remy2pictures2 = renpy.python.store_dicts["store"].get("remy2pictures2", False)
        # Make decision
        if remy2pictures2 == True or adine2unplayed == False:
            if chapter2libraryunplayed == False:
                if adinestatus != "bad":
                    if varasaved == True or (persistent.varasaved == True and not persistent.impermanence_four_killer):
                        remy3choiceyes = True
    jump impermanence_four_remy_c3endingmenu_return


label impermanence_four_remy_c5_killer:
    python:
        if remystatus == "bad":
            remydead = True
        elif remystatus == "abandoned":
            remydead = True
    jump impermanence_four_remy_c5_killer_return