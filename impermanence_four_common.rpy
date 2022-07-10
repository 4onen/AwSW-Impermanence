init:
    # Settings menu
    screen impermanence_four_modsettings tag smallscreen2:
        modal True
        window id "impermanence_four_modsettings" at popup2:
            style "smallwindow"
            vbox:
                hbox:
                    align (0.5, 0.5)
                    spacing 10
                    imagebutton:
                        xcenter 0.5
                        ycenter 0.5
                        idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                        hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                        selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                        selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                        action [MTSTogglePersistentBool("impermanence_four_no_reenlightenment"),
                                Play("audio", "se/sounds/yes.wav")]
                        hovered Play("audio", "se/sounds/select.ogg")
                        focus_mask None
                    text "Disable \"Enlightenment\" card after first true ending"
                hbox:
                    align (0.5, 0.5)
                    spacing 10
                    imagebutton:
                        xcenter 0.5
                        ycenter 0.5
                        idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                        hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                        selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                        selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                        action [MTSTogglePersistentBool("impermanence_four_killer"),
                                Play("audio", "se/sounds/yes.wav")]
                        hovered Play("audio", "se/sounds/select.ogg")
                        focus_mask None
                    text "Killer Mode"
                null
                text "In Killer Mode, Impermanence removes all protections. Characters and events will largely ignore the persistence file and rely only on actions completed this playthrough. {i}This will make the true ending impossible.{/i} Without Killer Mode, people can enter safe steady states once their good endings are completed, surviving unless you explicitly let them become Bad or Abandoned.":
                    align (0.5,0.3)

            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("my_cool_screen"), Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button




label impermanence_four_adine_killer:
    python:
        if remydead == False and (remygoodending == True or (persistent.remygoodending == True and not persistent.impermanence_four_killer)):
            # Remy saves Adine
            pass
        elif adine4unplayed == False:
            # Player saves Adine
            pass
        else:
            # Adine dies in the flying compettition
            adinedead = True

    jump impermanence_four_adine_killer_return