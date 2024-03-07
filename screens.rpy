screen MHB():
    tag menu
    if cheater or punished == True:
        add define_mods_images["menu_MHB_1"]
    else:
        add define_mods_images["menu_MHB_2"]
    use modmenunavigation(_("Кнопка исцеления Молли"))
    if cheater or punished == True:
        imagebutton:
            xpos 1313
            ypos 190
            idle define_mods_images["mhb_button_1_2"]
    else:
        imagebutton:
            xpos 1313
            ypos 190
            idle define_mods_images["mhb_button_1_1"]
    imagebutton:
        xpos 1313
        ypos 343
        idle define_mods_images["idle_mhb_button_2"]
        hover define_mods_images["hover_mhb_button_2"]
        action [If(cheater == False and punished == False, true = If(slumberreset3 == True, true = [SetVariable("cheater", False), SetVariable("punished", True)], false = [SetVariable("cheater", True), SetVariable("punished", False)]), false = [SetVariable("cheater", False), SetVariable("punished", False)]), Replay("mhb", scope={"cheater":cheater, "punished":punished}, locked=False)]
