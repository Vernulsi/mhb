init python hide:
    import os
    for file in renpy.list_files():
        if file.startswith('mods/mhb/images/'):
            name = os.path.splitext(file.replace('mods/mhb/images/',''))[0]
            renpy.image(name, Image(file))
            continue
init 2000 python:
    if customizationmod:
        default_image_list.append("mods/mhb/menu/main_menu_MHB_image.png")
    else:
        installed_menu_images.append(BackgroundImage(name="Main menu Molly MHB", file="mods/mhb/menu/main_menu_MHB.png"))
    install_profile_outfit('Molly', "Molly image 1", define_mods_images["game_menu_molly_1"])
    install_profile_outfit('Molly', "Molly image 2", define_mods_images["game_menu_molly_2"])
