define thg = Character("Мысли", who_outlines=[(absolute(2.5), "#000", absolute(0), absolute(0))])
define sete = Character("Учительница", color="#96001B", who_outlines=[(absolute(2.5), "#000", absolute(0), absolute(0))])
init python:
    PreCastMageLow = "mods/mhb/sound/PreCastMageLow.ogg"
    ShadowCast = "mods/mhb/sound/ShadowCast.ogg"
    NullifyPoison = "mods/mhb/sound/NullifyPoison.ogg"
    Teleport = "mods/mhb/sound/Teleport.ogg"
    Theramore1 = "mods/mhb/sound/Theramore1.mp3"
    Theramore2 = "mods/mhb/sound/Theramore2.mp3"
    Theramore3 = "mods/mhb/sound/Theramore3.mp3"
    Theramore4 = "mods/mhb/sound/Theramore4.mp3"
    mollysadmusic = "mods/mhb/sound/mollysad.mp3"
    PianoSad = "mods/mhb/sound/PianoSad.mp3"
    bonk = "mods/mhb/sound/bonk.mp3"
    renpy.music.register_channel('msound', 'sfx')
init 201 python:
    define_mods_images.update({
        "game_menu_molly_1":"mods/mhb/menu/game_menu_molly_1.png",
        "game_menu_molly_2":"mods/mhb/menu/game_menu_molly_2.png",
        "menu_MHB_1":"mods/mhb/menu/menu_MHB_1.png",
        "menu_MHB_2":"mods/mhb/menu/menu_MHB_2.png",
        "mhb_button_1_1":"mods/mhb/menu/mhb_button_1_1.png",
        "mhb_button_1_2":"mods/mhb/menu/mhb_button_1_2.png",
        "idle_mhb_button_2":"mods/mhb/menu/idle_mhb_button_2.png",
        "hover_mhb_button_2":"mods/mhb/menu/hover_mhb_button_2.png"
    })

init 1000 python:
    mhb = True
