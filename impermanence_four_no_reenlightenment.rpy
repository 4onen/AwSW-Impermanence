label impermanence_four_no_reenlightenment_c1:
    $ renpy.pause (0.0)

    if trueselectable == True:
        show cenlightenment at Pan((100, 0), (0, 0), 2.0)
        $ cardenlightenment = True
    elif persistent.lastendingseen == "bad":
        show ctrauma at Pan((100, 0), (0, 0), 2.0)
        $ cardtrauma = True
    elif persistent.lastendingseen == "good":
        show cduty at Pan((100, 0), (0, 0), 2.0)
        $ cardduty = True
    else:
        show cinception at Pan((100, 0), (0, 0), 2.0)
        $ cardinception = True
    with dissolveslow


    show text1 with dissolveslow

    show chap1:
        ypos -120
        linear 7.0 ypos -360
    with dissolveslow

    jump impermanence_four_no_reenlightenment_c1_end

label impermanence_four_no_reenlightenment_c2:
    $ renpy.pause (0.0)

    if trueselectable == True:
        show cenlightenment at Pan((100, 0), (0, 0), 2.0) with dissolveslow
        $ cardenlightenment = True
    elif evil2points >= 12:
        show cpride at Pan((100, 0), (0, 0), 2.0) with dissolveslow
        $ cardpride = True
    elif chap2points >= 8:
        show cduty at Pan((100, 0), (0, 0), 2.0) with dissolveslow
        $ cardduty = True
    elif chap2points >= 5:
        show chope at Pan((100, 0), (0, 0), 2.0) with dissolveslow
        $ cardhope = True
    else:
        show cconflict at Pan((100, 0), (0, 0), 2.0) with dissolveslow
        $ cardconflict = True

    show text2 with dissolveslow
    play soundloop "fx/fire3.ogg" fadein 1.0

    show chap2:
        ypos -120
        linear 7.0 ypos -360
    with dissolveslow

    jump impermanence_four_no_reenlightenment_c2_end

