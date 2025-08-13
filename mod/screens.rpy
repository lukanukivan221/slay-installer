################################################################################
## Initialization
################################################################################

init offset = -1


#####
# Hotkey screens — assigning hotkeys

screen keymap_screen():
    key "K_j" action ShowMenu('history')
    key "pad_righttrigger_pos" action ShowMenu('history')


################################################################################
## Styles
################################################################################


#### rest of style

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

# old
#style vscrollbar:
#    xsize gui.scrollbar_size
#    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    xalign 0
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb "gui/scrollbar/vertical_idle_thumb.png"

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"



    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    text_align 0.5
    xalign 0.5
    #xpos 900
    xsize 1800
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    #background Image("gui/textbox.png", xalign=1.0, yalign=1.0)

style voice_style:
    size 33
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    font "DejaVuSans.ttf"

style window_princess:
    font "gui/fonts/AmaticSC-Bold.ttf"
    size 60
    text_align 0.5
    xpos 100
    ypos -700
    xsize 500

style mound_style:
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    size 60
    text_align 0.5
    xpos 100
    ypos -700
    xsize 500

style mound_mid_style:
    size 80
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    text_align 0.5
    xalign 0.5
    ypos -500
    xsize 1200

style mound_scary_style:
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    size 60
    text_align 0.5
    xpos 100
    ypos -700
    xsize 500

style window_princess_mid:
    font "gui/fonts/AmaticSC-Bold.ttf"
    size 60
    text_align 0.5
    xpos 700
    ypos -700
    xsize 500

style window_spooky_princess:
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    size 76
    text_align 0.5
    xpos 50
    ypos -700
    xsize 600

style window_spooky_princess_right:
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    size 76
    text_align 0.5
    xpos 1200
    ypos -700
    xsize 500

style window_spooky_princess_mid:
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    size 90
    text_align 0.5
    xalign 0.5
    ypos -700
    xsize 800

style truth_style:
    size 70
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    text_align 0.5
    xalign 0.5
    ypos -100
    xsize 1300

style truth_small_style:
    size 50
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    text_align 0.5
    xalign 0.5
    ypos -100
    xsize 1300

style spooky_wild_style:
    size 64
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    text_align 0.5
    xalign 0.5
    ypos -50
    xsize 1300

style wild_style:
    size 52
    font "gui/fonts/AmaticSC-Bold.ttf"
    text_align 0.5
    xalign 0.5
    ypos -50
    xsize 1300

style wild_style_who:
    size 56
    font "gui/fonts/AmaticSC-Bold.ttf"
    text_align 0.5
    xalign 0.5
    ypos -125
    xsize 1300

style spooky_wild_style_who:
    size 66
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    text_align 0.5
    xalign 0.5
    ypos -125
    xsize 1300


style truth_mid_style:
    size 70
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    text_align 0.5
    xalign 0.5
    ypos -500
    xsize 1200

style truth_side_style:
    size 70
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    text_align 0.5
    xpos 100
    ypos -700
    xsize 500


style hero_dragon_style:
    size 60
    font "gui/fonts/AmaticSC-Bold.ttf"
    text_align 0.5
    xalign 0.5
    ypos -200
    xsize 800

style opportunist_dragon_style:
    size 70
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    text_align 0.5
    xalign 0.7
    ypos -700
    xsize 500

style cold_dragon_style:
    size 60
    font "gui/fonts/AmaticSC-Bold.ttf"
    text_align 0.5
    xalign 0.4
    ypos -450
    xsize 950

style truthside:
    font "gui/fonts/EastSeaDokdo-Regular.ttf"
    text_align 0.5
    xpos 100
    ypos -700
    xsize 800

style amatic:
    font "gui/fonts/AmaticSC-Bold.ttf"
    hover_color '#a84232'

style kelmscott:
    font "gui/fonts/KelmscottRomanNF.ttf"
    idle_color '#c2c2c2'
    hover_color '#a84232'
    selected_hover_color '#a84232'

style deja:
    font "DejaVuSans.ttf"
    color '#000000'
    idle_color '#000000'
    hover_color '#a84232'
    selected_hover_color '#a84232'

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5


style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos



#########################################
## Disable Click
## temporarily disables ability to click so animations can play out

screen disableclick(time):
    timer time action Hide("disableclick")
    key "mouseup_1" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_RETURN" action NullAction()

#######
# Special Disable Click for gallery

screen specialdisableclick():
    timer 1.20 action Hide("specialdisableclick")
    key "mouseup_1" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_RETURN" action NullAction()
    key "pad_a_press" action NullAction()
    key "pad_b_press" action NullAction()


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice
init python:
    def update_choice_icon():
        global choice_icon, default_mouse
        if default_mouse in config.mouse:
            choice_icon = config.mouse[default_mouse][0][0]
    choice_icon = None
    hovered_choice = -1

style choice_vscrollbar is vscrollbar
style choice_vscrollbar:
    #draggable True
    keyboard_focus False

screen choice(items):
    style_prefix "choice"
    default yadj = ui.adjustment()
    default hoveredrect = (1, 2, 3, 100)
    default hoveredy = 100


    key "repeat_K_UP" action ScrollViewport(yadj, 'up')
    key "K_UP" action ScrollViewport(yadj, 'up')
    key "K_DOWN" action ScrollViewport(yadj, 'down')
    key "repeat_K_DOWN" action ScrollViewport(yadj, 'down')
    key "pad_righty_neg" action ScrollViewport(yadj, 'up')
    key "repeat_pad_righty_neg" action ScrollViewport(yadj, 'up')
    key "pad_dpup_press" action ScrollViewport(yadj, 'up')
    key "repeat_pad_dpup_press" action ScrollViewport(yadj, 'up')
    key "pad_dpdown_press" action ScrollViewport(yadj, 'down')
    key "repeat_pad_dpdown_press" action ScrollViewport(yadj, 'down')
    key "pad_righty_pos" action ScrollViewport(yadj, 'down')
    key "repeat_pad_righty_pos" action ScrollViewport(yadj, 'down')
    key "pad_lefty_neg" action ScrollViewport(yadj, 'up')
    key "repeat_pad_lefty_neg" action ScrollViewport(yadj, 'up')
    key "pad_lefty_pos" action ScrollViewport(yadj, 'down')
    key "repeat_pad_lefty_pos" action ScrollViewport(yadj, 'down')
    #key "K_UP" action ScrollViewport(yadj, 'up', hoveredy)
    #key "K_DOWN" action ScrollViewport(yadj, 'down', hoveredy)
    #key "pad_righty_neg" action ScrollViewport(yadj, 'up', hoveredy)
    #key "pad_dpup_press" action ScrollViewport(yadj, 'up', hoveredy)
    #key "pad_dpdown_press" action ScrollViewport(yadj, 'down', hoveredy)
    #key "pad_righty_pos" action ScrollViewport(yadj, 'down', hoveredy)
    add "gui/choices_backdrop.png"
    if renpy.variant("console"):
        viewport yadjustment yadj:
            #draggable True
            #draggable "touch"
            mousewheel True
            scrollbars "vertical"
            xalign 0.0
            xsize 500
            ysize 650
            xpos 1410
            ypos 25
            vbox:
                for idx, i in enumerate(items):

                        hbox:
                            spacing 15
                            if hovered_choice == idx:
                                $ update_choice_icon()
                                add choice_icon ypos 0 yalign 0.5 xysize (48, 48)
                            else:
                                add Null(width=48, height=48, ypos=0, yalign=0.5)
                            if idx == 0:
                                textbutton i.caption xpos -10 action [i.action, Function(narrator.add_history, kind="adv", who=__(""), what=__(i.caption))] keyboard_focus True default_focus True:
                                    hovered SetVariable("hovered_choice", idx)
                                    unhovered SetVariable("hovered_choice", -1)
                            else:
                                textbutton i.caption xpos-10 action [i.action, Function(narrator.add_history, kind="adv", who=__(""), what=__(i.caption))]:
                                    hovered SetVariable("hovered_choice", idx)
                                    unhovered SetVariable("hovered_choice", -1)
    else:
        viewport yadjustment yadj:
            #draggable True
            #draggable "touch"
            mousewheel True
            scrollbars "vertical"
            xalign 0.0
            xsize 430
            ysize 650
            xpos 1480
            ypos 25
            vbox:
                for idx, i in enumerate(items):
                    if idx == 0:
                        textbutton i.caption action [i.action, Function(narrator.add_history, kind="adv", who=__(""), what=__(i.caption))] default_focus True keyboard_focus True
                            #hovered SetVariable("captured", renpy.focus_coordinates())
                    else:
                        textbutton i.caption action [i.action, Function(narrator.add_history, kind="adv", who=__(""), what=__(i.caption))] keyboard_focus True
                            #hovered SetVariable("captured", renpy.focus_coordinates())


#screen focus_screen(name):
#    default coord = GetFocusRect("rect") # Tuple of (x, y, w, h)
#    $ yadj = int(coord[3]) # Cast float to integer

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:

    xsize 350
    xpos 1470
    ypos 50

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    #color "#ffffff"
    outlines [ (3, "#000000")]

######## Viewport Scrolling ##############
init python:
    class ScrollViewport(Action):

        def __init__(self, yadj, scroll_dir, step=(gui.interface_text_size)*2.5):
        #def __init__(self, yadj, scroll_dir, step):
            self.yadj = yadj
            self.scroll_dir = scroll_dir
            self.step = step

        def __call__(self):
            #yadj = renpy.focus_coordinates()[3]
            # Don't confuse dir with the other use case for "up" which
            # refers to the state of the key (pressed/released)
            #print renpy.get_focus_rect()

            focused = renpy.get_focus_rect()
            if ( focused is not None ):
                self.yadj.change( focused[1] )
                renpy.restart_interaction
                return

            if self.scroll_dir == "up":
                if small_yadj:
                    self.yadj.change(self.yadj.value - (self.step/2))
                else:
                    self.yadj.change(self.yadj.value - self.step/1.3)
                renpy.display.behavior.queue_event('focus_up', up=False)
            else:
                if small_yadj:
                    self.yadj.change(self.yadj.value + (self.step/2))
                else:
                    self.yadj.change(self.yadj.value + self.step)
                renpy.display.behavior.queue_event('focus_down', up=False)
            renpy.restart_interaction


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if persistent.quick_menu:
        if quick_menu:
            hbox:
                style_prefix "quick"

                xalign 0.02
                yalign 0.02
                spacing 15

                #textbutton _("Back") action Rollback()
                #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                #textbutton _("Auto") action Preference("auto-forward", "toggle")
                if _preferences.language is not None:
                    imagebutton auto "gui/Quick Menu/auto_%s.png" action Preference("auto-forward", "toggle")
                else:
                    imagebutton auto "gui/Quick Menu/auto_eng_%s.png" action Preference("auto-forward", "toggle")
                if _preferences.language is not None:
                    imagebutton auto "gui/Quick Menu/skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True)
                else:
                    imagebutton auto "gui/Quick Menu/skip_eng_%s.png" action Skip() alternate Skip(fast=True, confirm=True)
                imagebutton auto "gui/Quick Menu/journal_%s.png" action ShowMenu('history')
                #imagebutton auto "gui/Quick Menu/journal_%s.png" action [Show("journal"), Play("audio", "audio/one_shot/pack_search_short.wav")] keyboard_focus False #currently showing journal
                imagebutton auto "gui/Quick Menu/save_%s.png" action ShowMenu('save')
                imagebutton auto "gui/Quick Menu/options_%s.png" action ShowMenu('preferences')


    #if quick_menu:

    #    hbox:
    #        style_prefix "quick"

    #        xalign 0.5
    #        yalign 1.0

            #textbutton _("Back") action Rollback()
    #        textbutton _("History") action ShowMenu('history')
    #        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
    #        textbutton _("Auto") action Preference("auto-forward", "toggle")
    #        textbutton _("Save") action ShowMenu('save')
    #        textbutton _("Q.Save") action QuickSave()
    #        textbutton _("Q.Load") action QuickLoad()
    #        textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    default temp_main_menu_store = False

    if main_menu == False and not renpy.get_screen("history") and not renpy.get_screen("preferences") and not renpy.get_screen("help_switch") and not renpy.get_screen("help_xbox") and not renpy.get_screen("help_ps"):
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            if persistent.gallery_unlocked:
                textbutton "Memories" action [ShowMenu("gallery"), Play("musicgallery", "audio/_music/mound/Oblivion.flac"), PauseAudio("music", True), PauseAudio("music2", True),PauseAudio("music3", True),PauseAudio("music4", True),PauseAudio("music5", True),PauseAudio("sound", True),PauseAudio("secondary", True),PauseAudio("tertiary", True)]

            textbutton _("Preferences") action ShowMenu("preferences")

            textbutton _("Subtitle Language") action ShowMenu("language_select_menu")

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("Main Menu") action MainMenu()

            if not renpy.variant("console"):
                textbutton _("Accessibility") action ToggleScreen("_accessibility")

            if renpy.variant("pc"):
                textbutton _("Join our Discord") action OpenURL("https://discord.gg/xCnAeqkkEY")

            #if renpy.variant("console_xbox"):
            #    textbutton _("Controls") action ShowMenu("help_xbox")

            #if renpy.variant("console_sony_ps5") or renpy.variant("console_sony_ps4"):
            #    textbutton _("Controls") action ShowMenu("help_ps")

            #if renpy.variant("console_nintendo_switch"):
            #    textbutton _("Controls") action ShowMenu("help_switch")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("Controls") action ShowMenu("help")

            if renpy.variant("pc"):

                ## The quit button is banned on iOS and unnecessary on Android and
                ## Web.
                textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
#style navigation_button_text is gui_button_text

style navigation_button_text is default:
    #xalign 0.5
    properties gui.button_text_properties("choice_button")
    #color "#ffffff"
    outlines [ (3, "#000000")]

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

# credit screens

screen credits_1():
    # tony + abby
    add "logo credits"
    text _("{=amatic}{size=75}Created by{/size}{/=amatic}") ypos 750 xalign 0.5
    text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=55}Tony Howard-Arias and Abby Howard{/size}" ypos 900 xalign 0.5


screen credits_2():
    # core team
    #text _("{=amatic}{size=80}The Team{/size}{/=amatic}") ypos 75 xalign 0.5

    # first row
    vbox:
        text _("{=amatic}{size=58}Written and\ndesigned by{/size}{/=amatic}") text_align 0.5 ypos 150 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Tony Howard-Arias{/size}" ypos 175 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=58}Illustrated, animated and edited by\n(and additional writing by){/size}{/=amatic}") text_align 0.5 ypos 150 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Abby Howard{/size}" text_align 0.5 ypos 175 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=58}Music\ncomposed by{/size}{/=amatic}") text_align 0.5 ypos 150 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Brandon Boone{/size}" text_align 0.5 ypos 175 xpos 1570 xalign 0.5

    # second row
    vbox:
        text _("{=amatic}{size=58}The Princess{/size}{/=amatic}") text_align 0.5 ypos 450 xalign 0.5 xpos 665
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Nichole Goodnight{/size}" text_align 0.5 ypos 500 xalign 0.5 xpos 665

    vbox:
        text _("{=amatic}{size=58}The Voices in Your Head {/size}{/=amatic}") text_align 0.5 ypos 450 xpos 1265 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Jonathan Sims{/size}" text_align 0.5 ypos 500 xpos 1265 xalign 0.5

    # third row
    #vbox:
        #text _("{=amatic}{size=58}Publishing Support{/size}{/=amatic}") text_align 0.5 ypos 800 xalign 0.5 xpos 350
        #text "{size=40}Tony Howard-Arias{/size}" ypos 275 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=58}Sound Design{/size}{/=amatic}") text_align 0.5 ypos 700 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Phil Michalski{/size}" text_align 0.5 ypos 750 xalign 0.5 xpos 960

    #vbox:
        #text _("{=amatic}{size=58}Localization{/size}{/=amatic}") text_align 0.5 ypos 800 xpos 1570 xalign 0.5
        #text "{size=40}Brandon Boone{/size}" text_align 0.5 ypos 275 xpos 1570 xalign 0.5

screen credits_3():

    ## serenity forge
    text _("{=amatic}{size=60}Slay the Princess — The Pristine Cut was published with our partners at{/size}{/=amatic}") ypos 30 xalign 0.5


    # row 1
    vbox:
        text _("{=amatic}{size=40}Publishing Director{/size}{/=amatic}") text_align 0.5 ypos 320 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Frigyes Racz{/size}" ypos 340 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Executive Director, Marketing Director and Product Designer{/size}{/=amatic}") text_align 0.5 ypos 320 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Zhenghua Yang (Z){/size}" text_align 0.5 ypos 340 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Lead Producer{/size}{/=amatic}") text_align 0.5 ypos 320 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Tim Garris{/size}" text_align 0.5 ypos 340 xpos 1570 xalign 0.5


    # row 2

    vbox:
        text _("{=amatic}{size=40}Lead Physical Publishing Producer{/size}{/=amatic}") text_align 0.5 ypos 470 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Erik Klein{/size}" text_align 0.5 ypos 490 xalign 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Lead Publishing Artist and{/size}{/=amatic}") text_align 0.5 ypos 470 xalign 0.5 xpos 960
        text _("{=amatic}{size=40}Lead Product Designer{/size}{/=amatic}") text_align 0.5 ypos 470 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Yu Ying Ong{/size}" ypos 490 xalign 0.5 text_align 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Production Manager{/size}{/=amatic}") text_align 0.5 ypos 470 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Kersti Forman{/size}" text_align 0.5 ypos 490 xpos 1570 xalign 0.5

    # row 3

    vbox:
        text _("{=amatic}{size=40}Product Designers and{/size}{/=amatic}") text_align 0.5 ypos 660 xalign 0.5 xpos 350
        text _("{=amatic}{size=40}Publishing Artists{/size}{/=amatic}") text_align 0.5 ypos 660 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Abby Stowers{/size}" text_align 0.5 ypos 680 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Sierre Harris{/size}" text_align 0.5 ypos 680 xalign 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Tech Lead{/size}{/=amatic}") text_align 0.5 ypos 675 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Zach Phillips{/size}" text_align 0.5 ypos 695 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Porting Engineers{/size}{/=amatic}") text_align 0.5 ypos 675 xalign 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Kevin Adams{/size}" text_align 0.5 ypos 695 xalign 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Matt Rader{/size}" text_align 0.5 ypos 695 xalign 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Adam Federbusch{/size}" text_align 0.5 ypos 695 xalign 0.5 xpos 1570

    # row 4

    vbox:
        text _("{=amatic}{size=40}Marketing Manager{/size}{/=amatic}") text_align 0.5 ypos 825 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Eric Grossman{/size}" text_align 0.5 ypos 845 xalign 0.5 xpos 960

screen credits_3a():

    ## serenity forge pt 2
    text _("{=amatic}{size=60}Slay the Princess — The Pristine Cut was published with our partners at{/size}{/=amatic}") ypos 30 xalign 0.5


    # row 1

    vbox:
        text _("{=amatic}{size=40}Quality Assurance{/size}{/=amatic}") text_align 0.5 ypos 320 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Erick Gonzalez{/size}" ypos 340 xalign 0.5 text_align 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Eliza Przygoda{/size}" ypos 340 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Quality Assurance Lead{/size}{/=amatic}") text_align 0.5 ypos 320 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Chris Souza{/size}" text_align 0.5 ypos 340 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Community Managers{/size}{/=amatic}") text_align 0.5 ypos 320 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Chris Souza{/size}" text_align 0.5 ypos 340 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Sara Misajlovska{/size}" text_align 0.5 ypos 340 xpos 1570 xalign 0.5


    # row 2

    vbox:
        text _("{=amatic}{size=40}Public Relations{/size}{/=amatic}") text_align 0.5 ypos 490 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Stephanie Tinsley{/size}" text_align 0.5 ypos 510 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Colby Tortorici{/size}" text_align 0.5 ypos 510 xalign 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Influencer Relations{/size}{/=amatic}") text_align 0.5 ypos 490 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Adolfo Aguirre{/size}" ypos 510 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Poe Chuang{/size}" ypos 510 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Alex Handziuk{/size}" ypos 510 xalign 0.5 text_align 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Marketing Associates{/size}{/=amatic}") text_align 0.5 ypos 490 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Luke Rica{/size}" text_align 0.5 ypos 510 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Zsófi Hámori-Gecser{/size}" text_align 0.5 ypos 510 xpos 1570 xalign 0.5

    # row 3

    #vbox:
    #    text _("{=amatic}{size=40}Ratings Associate{/size}{/=amatic}") text_align 0.5 ypos 660 xalign 0.5 xpos 350
    #    text "{size=30}Seohyeon Jeong{/size}" text_align 0.5 ypos 680 xalign 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Ratings Associate{/size}{/=amatic}") text_align 0.5 ypos 700 xalign 0.5 xpos 610
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Seohyeon Jeong{/size}" text_align 0.5 ypos 720 xalign 0.5 xpos 610

    vbox:
        text _("{=amatic}{size=40}Trailer Editors{/size}{/=amatic}") text_align 0.5 ypos 700 xalign 0.5 xpos 1310
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Péter Zentai and Luca Bonta{/size}" text_align 0.5 ypos 720 xalign 0.5 xpos 1310

    #vbox:
    #    text _("{=amatic}{size=40}Porting Engineers{/size}{/=amatic}") text_align 0.5 ypos 675 xalign 0.5 xpos 1570
    #    text "{size=30}Kevin Adams{/size}" text_align 0.5 ypos 695 xalign 0.5 xpos 1570
    #    text "{size=30}Matt Rader{/size}" text_align 0.5 ypos 695 xalign 0.5 xpos 1570
    #    text "{size=30}Adam Federbusch{/size}" text_align 0.5 ypos 695 xalign 0.5 xpos 1570

    # row 4

screen credits_3b():

    text _("{=amatic}{size=60}Slay the Princess — The Pristine Cut was published with our partners at{/size}{/=amatic}") ypos 30 xalign 0.5

    vbox:
        text _("{=amatic}{size=40}Business Director{/size}{/=amatic}") text_align 0.5 ypos 320 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Kevin Zhang{/size}" ypos 340 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Legal{/size}{/=amatic}") text_align 0.5 ypos 320 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Brandon J. Huffman{/size}" text_align 0.5 ypos 340 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Connor Richards{/size}" text_align 0.5 ypos 340 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Sales & Finance Director{/size}{/=amatic}") text_align 0.5 ypos 320 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Christine Gallagher{/size}" text_align 0.5 ypos 340 xpos 1570 xalign 0.5

    vbox:
        text _("{=amatic}{size=40}Additional Support{/size}{/=amatic}") text_align 0.5 ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Michael Yum{/size}" text_align 0.5 ypos 540 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Tim Pivnicny{/size}" text_align 0.5 ypos 540 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Máté Gecser{/size}" text_align 0.5 ypos 540 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Boan “Dian” Ding{/size}" text_align 0.5 ypos 540 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Alex Brown{/size}" text_align 0.5 ypos 540 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Jacob Bloom{/size}" text_align 0.5 ypos 540 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Special Thanks{/size}{/=amatic}") text_align 0.5 ypos 850 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Tao Sila, Chloé Giusti, Ted Regulski, Shuhei Yoshida, Alice Liang, Lori Jee, Caspar Gray,\nTina Kowalewski, nicolith, Johnson Lin, Mike Mitchell, Justin Shake,\n Zoe, Shirley, & Ezra Klein; Brian, Ethan, & Noah Gallagher; Mattie, Seneca, & Faraday Yang{/size}" text_align 0.5 ypos 870 xalign 0.5 xpos 960


screen credits_4():

    ## altagram
    text _("{=amatic}{size=60}Localization Credits{/size}{/=amatic}") ypos 30 xalign 0.5

    # row 1
    vbox:
        text _("{=amatic}{size=40}Localization Project Manager{/size}{/=amatic}") text_align 0.5 ypos 150 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Mathilde Gribaudi{/size}" ypos 170 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Senior Localization Project Managers{/size}{/=amatic}") text_align 0.5 ypos 150 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Ye Sol Lee{/size}" text_align 0.5 ypos 170 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Amira Elmasry{/size}" text_align 0.5 ypos 170 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}QA Project Manager{/size}{/=amatic}") text_align 0.5 ypos 150 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Jin Ryoo{/size}" text_align 0.5 ypos 170 xpos 1570 xalign 0.5

    # row 2

    vbox:
        text _("{=amatic}{size=40}QA Test Lead{/size}{/=amatic}") text_align 0.5 ypos 330 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Marcos Ferreira{/size}" ypos 350 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Senior Localization Engineer{/size}{/=amatic}") text_align 0.5 ypos 330 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Wolfgang Hoffmann-Schoenborn{/size}" text_align 0.5 ypos 350 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Localization Engineer{/size}{/=amatic}") text_align 0.5 ypos 330 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Antonio Manuel Beleño Rodríguez{/size}" text_align 0.5 ypos 350 xpos 1570 xalign 0.5

    # row 3

    vbox:
        text _("{=amatic}{size=40}German Translation{/size}{/=amatic}") text_align 0.5 ypos 500 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Henrike Kupsch{/size}" text_align 0.5 ypos 520 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Iris Schäfer{/size}" text_align 0.5 ypos 520 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Jakob Semmer{/size}" text_align 0.5 ypos 520 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Julia Meter{/size}" text_align 0.5 ypos 520 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Sandra Kohl{/size}" text_align 0.5 ypos 520 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Stephan Grabowski{/size}" text_align 0.5 ypos 520 xalign 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}French Translation{/size}{/=amatic}") text_align 0.5 ypos 500 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Amandine Obry{/size}" ypos 520 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Jean-Yves Bleuyard{/size}" ypos 520 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Laly Dufossé{/size}" ypos 520 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Karine Goldstein{/size}" ypos 520 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Romain Portelli{/size}" ypos 520 xalign 0.5 text_align 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Korean Translation{/size}{/=amatic}") text_align 0.5 ypos 500 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Thomas Oh{/size}" text_align 0.5 ypos 520 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Harriet Kim{/size}" text_align 0.5 ypos 520 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Runo Lee{/size}" text_align 0.5 ypos 520 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Derek Kim{/size}" text_align 0.5 ypos 520 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Kim Dong Woo{/size}" text_align 0.5 ypos 520 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Eojin Jang{/size}" text_align 0.5 ypos 520 xpos 1570 xalign 0.5

    # row 4

    vbox:
        text _("{=amatic}{size=40}Japanese Translation{/size}{/=amatic}") text_align 0.5 ypos 800 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Natsuko Tanaka{/size}" ypos 820 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Saori Yatsuhashi{/size}" ypos 820 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Mana Sato{/size}" ypos 820 xalign 0.5 text_align 0.5 xpos 960

screen credits_4a():

    ## altagram 2
    text _("{=amatic}{size=60}Localization Credits{/size}{/=amatic}") ypos 30 xalign 0.5

    # row 1

    vbox:
        text _("{=amatic}{size=40}Simplified Chinese Translation{/size}{/=amatic}") text_align 0.5 ypos 150 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Feng Shang{/size}" text_align 0.5 ypos 170 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Xiaoyu Tian{/size}" text_align 0.5 ypos 170 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Xavier Wang{/size}" text_align 0.5 ypos 170 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Ivy Wang{/size}" text_align 0.5 ypos 170 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Xuan Pan{/size}" text_align 0.5 ypos 170 xalign 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Traditional Chinese Translation{/size}{/=amatic}") text_align 0.5 ypos 150 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Sharon Lin{/size}" text_align 0.5 ypos 170 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Celine Ku{/size}" text_align 0.5 ypos 170 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Siew Ng{/size}" text_align 0.5 ypos 170 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Yachi Chu{/size}" text_align 0.5 ypos 170 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Simon Wang{/size}" text_align 0.5 ypos 170 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Eve Wu{/size}" text_align 0.5 ypos 170 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Amy Lin{/size}" text_align 0.5 ypos 170 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Tony Tang{/size}" text_align 0.5 ypos 170 xpos 960 xalign 0.5

    vbox:
        text _("{=amatic}{size=40}Brazilian Portuguese Translation{/size}{/=amatic}") text_align 0.5 ypos 150 xalign 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Bruno Dias{/size}" ypos 170 xalign 0.5 text_align 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Fábio Ludwig{/size}" ypos 170 xalign 0.5 text_align 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Felipe Getirana{/size}" ypos 170 xalign 0.5 text_align 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Isadora Aires{/size}" ypos 170 xalign 0.5 text_align 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Leila Ibarra{/size}" ypos 170 xalign 0.5 text_align 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Marcelo Almeida{/size}" ypos 170 xalign 0.5 text_align 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Murilo Martins{/size}" ypos 170 xalign 0.5 text_align 0.5 xpos 1570

    # row 2

    vbox:
        text _("{=amatic}{size=40}Spanish (ES) Translation{/size}{/=amatic}") text_align 0.5 ypos 510 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}J. Angel Alvarez Sanchez{/size}" text_align 0.5 ypos 530 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Juan Ferragud Sáez{/size}" text_align 0.5 ypos 530 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Mar Campayo Chaparra{/size}" text_align 0.5 ypos 530 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Nerea González Alonso{/size}" text_align 0.5 ypos 530 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Pedro José Sepúlveda{/size}" text_align 0.5 ypos 530 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Itziar Ugarte Lechuga{/size}" text_align 0.5 ypos 530 xalign 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Spanish (LATAM) Translation{/size}{/=amatic}") text_align 0.5 ypos 540 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Ana Bethsaida Avila{/size}" text_align 0.5 ypos 560 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Candela dos Ramos{/size}" text_align 0.5 ypos 560 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Dalia Jiménez Velón{/size}" text_align 0.5 ypos 560 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Joaquin Herrero{/size}" text_align 0.5 ypos 560 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Jesica Miotti{/size}" text_align 0.5 ypos 560 xpos 960 xalign 0.5

    vbox:
        text _("{=amatic}{size=40}Polish Translation{/size}{/=amatic}") text_align 0.5 ypos 510 xalign 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Adam Mieczynski{/size}" ypos 530 xalign 0.5 text_align 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Anna Roma{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}{size=23}ń{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}ska-Babut{/size}" ypos 530 xalign 0.5 text_align 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Piotr Wilk{/size}" ypos 530 xalign 0.5 text_align 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Rados{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}{size=23}ł{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}aw Aleksanderek{/size}" ypos 530 xalign 0.5 text_align 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Gabriela Janiszewska{/size}" ypos 530 xalign 0.5 text_align 0.5 xpos 1570


    # row 3

    vbox:
        text _("{=amatic}{size=40}Italian Translation{/size}{/=amatic}") text_align 0.5 ypos 830 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Beatrice Ceruti; Francesco Caligiuri{/size}" text_align 0.5 ypos 850 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Federico Castellano{/size}" text_align 0.5 ypos 850 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Laura Innocenti{/size}" text_align 0.5 ypos 850 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Luca Moretti{/size}" text_align 0.5 ypos 850 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Sara Baroni{/size}" text_align 0.5 ypos 850 xalign 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Ukrainian Translation{/size}{/=amatic}") text_align 0.5 ypos 830 xalign 0.5 xpos 1570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Lukanukivan{/size}" ypos 850 xalign 0.5 text_align 0.5 xpos 1570
        

    vbox:
        text _("{=amatic}{size=40}Russian Translation{/size}{/=amatic}") text_align 0.5 ypos 830 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Alexandra Frolova; Kate Stepanova{/size}" ypos 850 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Anya Tuntiya; Nadezhda Lynova{/size}" ypos 850 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Karina Avanesova{/size}" ypos 850 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Kristina Lantratova{/size}" ypos 850 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Svetlana Postuma{/size}" ypos 850 xalign 0.5 text_align 0.5 xpos 960

screen credits_4b():

    default schinesetrans = "{size=30}Simplified Chinese{/size}"
    default espanishtrans = "{size=30}Spanish (ES){/size}"
    default ukrainiantrans = "{size=30}Ukrainian{/size}"
    default russiantrans = "{size=30}Russian{/size}"
    default japanesetrans = "{size=30}Japanese{/size}"
    default polishtrans = "{size=30}Polish{/size}"
    default frenchtrans = "{size=30}French{/size}"
    default tchinesetrans = "{size=30}Traditional Chinese"
    default latamspanishtrans = "{size=30}Spanish (LATAM)"
    default btprtrans = "{size=30}Brazilian Portuguese"
    default koreantrans = "{size=30}Korean"
    default germantrans = "{size=30}German"
    default italiantrans = "{size=30}Italian"

    ## altagram 3
    text _("{=amatic}{size=60}Localization Credits{/size}{/=amatic}") ypos 30 xalign 0.5

    # row 1

    text _("{=amatic}{size=40}Localization Quality Assurance{/size}{/=amatic}") ypos 150 xalign 0.5

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Yong Kang He — {/size}" + "{=kelmscott}[schinesetrans!t]" text_align 0.5 ypos 200 xalign 0.5 xpos 570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Marco Nieto — {/size}" + "{=kelmscott}[espanishtrans!t]" text_align 0.5 ypos 220 xalign 0.5 xpos 570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Lukanukivan — {/size}" + "{=kelmscott}[ukrainiantrans!t]" text_align 0.5 ypos 240 xalign 0.5 xpos 570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Anastasia Tales — {/size}" + "{=kelmscott}[russiantrans!t]" text_align 0.5 ypos 260 xalign 0.5 xpos 570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Misato Otomo; Rene Koike — {/size}" + "{=kelmscott}[japanesetrans!t]" text_align 0.5 ypos 280 xalign 0.5 xpos 570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Iwona Rzepi{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}{size=23}ń{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}ska — {/size}" + "{=kelmscott}[polishtrans!t]" text_align 0.5 ypos 300 xalign 0.5 xpos 570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Laurence Chane-Hoong — {/size}" + "{=kelmscott}[frenchtrans!t]" text_align 0.5 ypos 320 xalign 0.5 xpos 570

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Xiaoman Tu; Mei Lam (Kate) Lai — {/size}" + "{=kelmscott}[tchinesetrans!t]" ypos 200 xalign 0.5 text_align 0.5 xpos 1350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Alejandra Cortes — {/size}" + "{=kelmscott}[latamspanishtrans!t]" ypos 220 xalign 0.5 text_align 0.5 xpos 1350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Vanessa Andrade — {/size}" + "{=kelmscott}[btprtrans!t]" ypos 230 xalign 0.5 text_align 0.5 xpos 1350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Taeyeon Hwang; Yura Eom; Seoyun Kim — {/size}" + "{=kelmscott}[koreantrans!t]" ypos 230 xalign 0.5 text_align 0.5 xpos 1350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Golo Hennig — {/size}" + "{=kelmscott}[germantrans!t]" ypos 230 xalign 0.5 text_align 0.5 xpos 1350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Anna Severi — {/size}" + "{=kelmscott}[italiantrans!t]" ypos 230 xalign 0.5 text_align 0.5 xpos 1350

    # row 2

    vbox:
        text _("{=amatic}{size=40}Head of QA{/size}{/=amatic}") text_align 0.5 ypos 450 xpos 960 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Ingrid Perez{/size}" text_align 0.5 ypos 470 xpos 960 xalign 0.5

    # row 3

    vbox:
        text _("{=amatic}{size=40}Linguistic Team Lead{/size}{/=amatic}") text_align 0.5 ypos 600 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Dylan L. Martin{/size}" ypos 620 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Project Manager Team Leads{/size}{/=amatic}") text_align 0.5 ypos 600 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Jonathan Aplin{/size}" text_align 0.5 ypos 620 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Yasmin Babb{/size}" text_align 0.5 ypos 620 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Partnership Manager{/size}{/=amatic}") text_align 0.5 ypos 600 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Jared Swift{/size}" text_align 0.5 ypos 620 xpos 1570 xalign 0.5

    # row 4

    vbox:
        text _("{=amatic}{size=40}Altagram CCO{/size}{/=amatic}") text_align 0.5 ypos 800 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Karolina Drapala{/size}" ypos 820 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Altagram COO{/size}{/=amatic}") text_align 0.5 ypos 800 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Balint Acsay{/size}" text_align 0.5 ypos 820 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Altagram CEO{/size}{/=amatic}") text_align 0.5 ypos 800 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Marie Amigues{/size}" text_align 0.5 ypos 820 xpos 1570 xalign 0.5


screen credits_4c():

    ## Viridian
    text _("{=amatic}{size=60}Console Porting{/size}{/=amatic}") ypos 30 xalign 0.5

    vbox:
        text _("{=amatic}{size=40}Technical Producer — Porting{/size}{/=amatic}") text_align 0.5 ypos 320 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Thomas Cashman{/size}" ypos 340 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Producer — Porting{/size}{/=amatic}") text_align 0.5 ypos 320 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Paul McInerney{/size}" text_align 0.5 ypos 340 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Senior Software Engineer — Porting{/size}{/=amatic}") text_align 0.5 ypos 320 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Jade Macho{/size}" text_align 0.5 ypos 340 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Josh Free{/size}" text_align 0.5 ypos 340 xpos 1570 xalign 0.5


    # row 2

    vbox:
        text _("{=amatic}{size=40}Graphics Engineer — Porting{/size}{/=amatic}") text_align 0.5 ypos 540 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Caleb Cornett{/size}" text_align 0.5 ypos 560 xalign 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Software Engineer — Porting{/size}{/=amatic}") text_align 0.5 ypos 540 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}James Mooney{/size}" ypos 560 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Conor McDonagh-Rollo{/size}" ypos 560 xalign 0.5 text_align 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Senior QA Tester — Porting{/size}{/=amatic}") text_align 0.5 ypos 540 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Sean Duggan{/size}" text_align 0.5 ypos 560 xpos 1570 xalign 0.5

    # row 3

    vbox:
        text _("{=amatic}{size=40}UX Tester — Porting{/size}{/=amatic}") text_align 0.5 ypos 750 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}James McEvaddy{/size}" ypos 770 xalign 0.5 text_align 0.5 xpos 960

screen credits_5():

    default vocals = "{size=35}Vocals{/size}"
    default guitar = "{size=35}Guitar{/size}"
    default cello = "{size=35}Cello{/size}"
    default woodwinds = "{size=35}Woodwinds{/size}"
    default violin = "{size=35}Violin{/size}"
    default piano = "{size=35}Piano{/size}"

    ## amelia + instrmentalists
    text _("{=amatic}{size=80}Vocals and Instrumentalists{/size}{/=amatic}") ypos 40 xalign 0.5

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Amelia Jones — {/size}" + "{=kelmscott}[vocals!t]" ypos 180 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'Transformation'{/size}" ypos 185 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}''The Shifting Mound Movements 1-5'{/size}" ypos 190 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Apotheosis'{/size}" ypos 195 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'Oblivion'{/size}" ypos 200 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Wild'{/size}" ypos 205 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Princess and the Dragon'{/size}" ypos 210 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'A Tapestry Undone'{/size}" ypos 215 xalign 0.5 text_align 0.5 xpos 960

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Dan Zappulla — {/size}" + "{=kelmscott}[guitar!t]" ypos 580 xalign 0.5 text_align 0.5 xpos 650
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Witch'{/size}" ypos 600 xalign 0.5 text_align 0.5 xpos 650

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Scotty Wells — {/size}" + "{=kelmscott}[guitar!t]" ypos 580 xalign 0.5 text_align 0.5 xpos 1270
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Apotheosis'{/size}" ypos 600 xalign 0.5 text_align 0.5 xpos 1270

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Andrew Dunn — {/size}" + "{=kelmscott}[cello!t]" ypos 730 xalign 0.5 text_align 0.5 xpos 650
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'I Meant It'{/size}" ypos 750 xalign 0.5 text_align 0.5 xpos 650

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Adrew Goodwin — {/size}" + "{=kelmscott}[woodwinds!t]" ypos 730 xalign 0.5 text_align 0.5 xpos 1270
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Princess and the Dragon'{/size}" ypos 750 xalign 0.5 text_align 0.5 xpos 1270

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Matheus Sardinha Garcia Souza — {/size}" + "{=kelmscott}[violin!t]" ypos 890 xalign 0.5 text_align 0.5 xpos 650
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'I Meant It'{/size}" ypos 910 xalign 0.5 text_align 0.5 xpos 650

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Mark Choi — {/size}" + "{=kelmscott}[piano!t]" ypos 890 xalign 0.5 text_align 0.5 xpos 1270
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Unknown Together'{/size}" ypos 910 xalign 0.5 text_align 0.5 xpos 1270

screen credits_6():

    default composer = "{size=40}Composer{/size}"
    default playersmusic = "{size=40}Players{/size}"
    default orchestrator = "{size=40}Orchestrator{/size}"
    default conductormusic = "{size=40}Conductor{/size}"
    default copyist = "{size=40}Copyist{/size}"
    default musicproducer = "{size=40}Music Producer{/size}"

    ## orchestra
    text _("{=amatic}{size=80}Orchestra{/size}{/=amatic}") ypos 40 xalign 0.5

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Brandon Boone — {/size}" + "{=kelmscott}[composer!t]" ypos 185 xalign 0.5 text_align 0.5 xpos 960
        text _("{size=40}Czech National Symphony Orchestra — {/size}") + "{=kelmscott}[playersmusic!t]" ypos 190 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Catherine Nguyen — {/size}" + "{=kelmscott}[orchestrator!t]" ypos 195 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Vladimir Martinka — {/size}" + "{=kelmscott}[conductormusic!t]" ypos 200 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Shireen Ghosh — {/size}" + "{=kelmscott}[copyist!t]" ypos 205 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=40}Alex Palmer — {/size}" + "{=kelmscott}[musicproducer!t]" ypos 210 xalign 0.5 text_align 0.5 xpos 960

    vbox:
        text _("{size=40}Tracks{/size}") ypos 600 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'Transformation'{/size}" ypos 620 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}''The Shifting Mound Movements 2, 3, 5'{/size}" ypos 630 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Apotheosis'{/size}" ypos 640 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Unknown Together'{/size}" ypos 650 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Princess (Gallery Version)'{/size}" ypos 660 xalign 0.5 text_align 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}'The Damsel (Gallery Version)'{/size}" ypos 670 xalign 0.5 text_align 0.5 xpos 960


screen credits_7():

    ## laundry bear
    text _("{=amatic}{size=80}Gallery co-developed with{/size}{/=amatic}") ypos 40 xalign 0.5
    # row 1
    vbox:
        text _("{=amatic}{size=40}Technical Director{/size}{/=amatic}") text_align 0.5 ypos 420 xalign 0.5 xpos 350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Andrew Carvalho{/size}" ypos 440 xalign 0.5 text_align 0.5 xpos 350

    vbox:
        text _("{=amatic}{size=40}Operations{/size}{/=amatic}") text_align 0.5 ypos 420 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Jayme Last{/size}" text_align 0.5 ypos 440 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=40}Programmer{/size}{/=amatic}") text_align 0.5 ypos 420 xpos 1570 xalign 0.5
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Kai Banks{/size}" text_align 0.5 ypos 440 xpos 1570 xalign 0.5

    # row 2

    vbox:
        text _("{=amatic}{size=40}Ren'py Consultant{/size}{/=amatic}") text_align 0.5 ypos 650 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Sunny Evans{/size}" text_align 0.5 ypos 670 xalign 0.5 xpos 960

screen credits_8():

    ## amanda/manuela/fonts
    vbox:
        text _("{=amatic}{size=50}VFX{/size}{/=amatic}") ypos 75 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Team Dogpit{/size}" ypos 95 xalign 0.5 xpos 960

    vbox:
        text _("{=amatic}{size=50}Game Logo{/size}{/=amatic}") ypos 75 xalign 0.5 xpos 570
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Amanda Williams{/size}" ypos 95 xalign 0.5 xpos 570

    vbox:
        text _("{=amatic}{size=50}Sound Assistant{/size}{/=amatic}") ypos 75 xalign 0.5 xpos 1350
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Krzysztof Wasilewski{/size}" ypos 95 xalign 0.5 xpos 1350

    vbox:
        text _("{=amatic}{size=40}Stock Footage{/size}{/=amatic}") ypos 270 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}realism (pond5.com){/size}" ypos 290 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}tanaonte (pond5.com){/size}" ypos 290 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=30}Endimion (pond5.com){/size}" ypos 290 xalign 0.5 xpos 960



    vbox:
        text _("{=amatic}{size=40}Fonts{/size}{/=amatic}") ypos 500 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}KelmscottRoman NF (nicksfonts.com){/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Amatic SC (Vernon Adams){/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Deja Vu Sans{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}East Sea Dokdo (YoonDesign Inc){/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Noto Serif{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}Mushin{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}GenEiAntique{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}New Tegomin{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}YuzuPenKai{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}SourceHanSans-Normal{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}KaiTi{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}DFHannotateW7{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}DFHsiuW3{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}DFPKanTingLiuW9-GB{/size}" ypos 520 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=25}DFPKanTingLiuW9{/size}" ypos 520 xalign 0.5 xpos 960




screen credits_9():

    ## patrons
    text _("{=amatic}{size=65}Thanks to all of our alpha testers from Patreon{/size}{/=amatic}") ypos 30 xalign 0.5

screen credits_10():

    ## special thanks
    text _("{=amatic}{size=65}And finally, special thanks{/size}{/=amatic}") ypos 40 xalign 0.5

    vbox:
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Gab Smolders{/size}" text_align 0.5 ypos 150 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Markiplier{/size}" text_align 0.5 ypos 170 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}ManlyBadassHero{/size}" text_align 0.5 ypos 190 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}@horrorvisuals{/size}" text_align 0.5 ypos 210 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Laura Stringer{/size}" text_align 0.5 ypos 230 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Alpha Beta Gamer{/size}" text_align 0.5 ypos 250 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Stride PR{/size}" text_align 0.5 ypos 270 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Manuela Malasaña{/size}" text_align 0.5 ypos 290 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Jenny Windom{/size}" text_align 0.5 ypos 310 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Trevor Henderson{/size}" text_align 0.5 ypos 330 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}GLITCH{/size}" text_align 0.5 ypos 350 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Sophie Wolvin{/size}" text_align 0.5 ypos 370 xalign 0.5 xpos 960
        text "{font=gui/fonts/KelmscottRomanNF.ttf}{size=35}Ren'py Tom{/size}" text_align 0.5 ypos 390 xalign 0.5 xpos 960
        text _("{size=35}And everyone who's supported us along the way{/size}") text_align 0.5 ypos 420 xalign 0.5 xpos 960
        text _("{size=35}(including you!){/size}") text_align 0.5 ypos 440 xalign 0.5 xpos 960

    text _("{size=30}And an extra special thanks\nto our lil' creatures:") text_align 0.5 ypos 500 xalign 0.5 xpos 340 line_spacing 5
    text _("{size=30}Wednesday (Snake),\nSpoons (Cat),\n and Nubs (Small Monster){/size}") text_align 0.5 ypos 610 xalign 0.5 xpos 340 line_spacing 5

screen credits_11():
    ## Additional Credits Page
    text _("{=amatic}{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}{size=65}Від автора українізатора{/size}{/=amatic}") ypos 40 xalign 0.5

    vbox:
        xalign 0.5  # Центруємо контейнер
        text "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}{size=30}Перекладом займався - lukanukivan{/size}" text_align 0.0 ypos 150
    
    
    text _("{=amatic}{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}{size=65}Дуже вдячний цим людям за допомогу:{/size}{/=amatic}") ypos 260 xalign 0.5
   
    vbox:
        xalign 0.5  # Центруємо контейнер
        text "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}{size=30}Дякую, за допомогу з переносом тексту між версіями - ТГ @quantumInverter{/size}" text_align 0.0 ypos 370
        text "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}{size=30}Дякую, за створення інсталятора - ТГ @djighoul29{/size}" text_align 0.0 ypos 390
        text "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}{size=30}Дякую, за перевірку тексту на помилки - ТГ @Froggy_8 та Didinson{/size}" text_align 0.0 ypos 410

screen song():


    $ song_ypos = 200
    if final_ending == "good":
        vbox:
            xalign 0.5
            text "{size=30}The Princess{/size}" ypos song_ypos xpos 0
            $ song_ypos += 25
            text "{size=30}The World Ender{/size}" ypos song_ypos xpos 0
            $ song_ypos += 25
            text "{size=30}Eternal Bliss (Yay, you did it!){/size}" ypos song_ypos xpos 0
    else:
        hbox:
            xalign 0.5
            vbox:
                text "{size=30}The Princess{/size}" ypos song_ypos xpos 0
                $ song_ypos += 25
                if first_princess != "stranger":
                    text "{size=30}The World Ender{/size}" ypos song_ypos xpos 0
                    $ song_ypos += 25
                if final_ending != "oblivion":
                    if oblivion_when_met == 0:
                        text "{size=30}Oblivion{/size}" ypos song_ypos xpos 0
                        $ song_ypos += 25
                if loops_finished >= 1:
                    if first_mound == "adversary":
                        text "{size=30}The Song We Write in Our Blood{/size}" ypos song_ypos xpos 0
                    elif first_mound == "needle":
                        text "{size=30}The Eye of the Needle{/size}" ypos song_ypos xpos 0
                    elif first_mound == "beast":
                        text "{size=30}I Am So Much More Than You{/size}" ypos song_ypos xpos 0
                    elif first_mound == "damsel":
                        text "{size=30}It Was Always That Easy{/size}" ypos song_ypos xpos 0
                    elif first_mound == "dereal":
                        text "{size=30}I Just Want to Make You Happy{/size}" ypos song_ypos xpos 0
                    elif first_mound == "nightmare":
                        text "{size=30}I Want to Watch It Happen{/size}" ypos song_ypos xpos 0
                    elif first_mound == "clarity":
                        text "{size=30}The Moment of Clarity{/size}" ypos song_ypos xpos 0
                    elif first_mound == "prisonerhead":
                        text "{size=30}Eyes on Me{/size}" ypos song_ypos xpos 0
                    elif first_mound == "prisonerchain":
                        text "{size=30}I Don't Like Small Talk{/size}" ypos song_ypos xpos 0
                    elif first_mound == "razorheart":
                        text "{size=30}The Razor{/size}" ypos song_ypos xpos 0
                    elif first_mound == "razor":
                        text "{size=30}Mutually Assured Destruction{/size}" ypos song_ypos xpos 0
                    elif first_mound == "spectre":
                        if spectre_end == "free":
                            text "{size=30}Hitching a Ride{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}The Spectre{/size}" ypos song_ypos xpos 0
                    elif first_mound == "stranger":
                        text "{size=30}To Be Everything{/size}" ypos song_ypos xpos 0
                    elif first_mound == "tower":
                        text "{size=30}Supplication{/size}" ypos song_ypos xpos 0
                    elif first_mound == "witch":
                        text "{size=30}It's in Our Nature{/size}" ypos song_ypos xpos 0
                    elif first_mound == "thorn":
                        if thorn_end == "free_kiss":
                            text "{size=30}A Kiss From a Thorn{/size}" ypos song_ypos xpos 0
                        elif thorn_end == "free":
                            text "{size=30}The Thorn{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}A Moment Trapped for All Time{/size}" ypos song_ypos xpos 0
                    elif first_mound == "greydamsel":
                        text "{size=30}The Grey (Fire){/size}" ypos song_ypos xpos 0
                    elif first_mound == "greyprisoner":
                        text "{size=30}The Grey (Water){/size}" ypos song_ypos xpos 0
                    elif first_mound == "wildnerves":
                        text "{size=30}The Wild{/size}" ypos song_ypos xpos 0
                    elif first_mound == "wildwound":
                        text "{size=30}The Wild{/size}" ypos song_ypos xpos 0
                    elif first_mound == "wraith":
                        text "{size=30}I'm Taking What I'm Owed{/size}" ypos song_ypos xpos 0
                    elif first_mound == "apotheosis":
                        if final_ending != "liberation":
                            text "{size=30}The Apotheosis{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}A Tapestry Undone{/size}" ypos song_ypos xpos 0
                    elif first_mound == "den":
                        if beast_2_end == "free":
                            text "{size=30}Hand-in-Claw{/size}" ypos song_ypos xpos 0
                        elif beast_2_end == "consume" or beast_2_end == "slay":
                            text "{size=30}The Rhythm of the Flesh{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}The Den{/size}" ypos song_ypos xpos 0
                    elif first_mound == "fury":
                        if fury_end == "leave" or fury_end == "free" or fury_end == "slay":
                            text "{size=30}There's Nothing I Can Do To Bring You Back{/size}" ypos song_ypos xpos 0
                        elif fury_end == "slay_unarmed":
                            text "{size=30}The Bell{/size}" ypos song_ypos xpos 0
                        elif fury_end == "slay_tower":
                            text "{size=30}An Empty Void that Dared to Dream it Was Alive{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}The Fury{/size}" ypos song_ypos xpos 0
                    elif first_mound == "furyheart":
                        text "{size=30}Thirty-Trillion Cells{/size}" ypos song_ypos xpos 0
                    elif first_mound == "happy":
                        if happy_end == "dance":
                            text "{size=30}I Meant It{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}What Remains After the Fire{/size}" ypos song_ypos xpos 0
                    elif first_mound == "happydry":
                        text "{size=30}Our Happy Ending{/size}" ypos song_ypos xpos 0
                    elif first_mound == "dragonhand":
                        text "{size=30}The Life-Taker{/size}" ypos song_ypos xpos 0
                    elif first_mound == "dragonfused":
                        text "{size=30}The Princess and the Dragon{/size}" ypos song_ypos xpos 0
                    elif first_mound == "dragon":
                        text "{size=30}What Once Was One{/size}" ypos song_ypos xpos 0
                    elif first_mound == "cage":
                        if cage_end == "free":
                            text "{size=30}An Open Door{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}A Prison of Flesh{/size}" ypos song_ypos xpos 0
                    $ song_ypos += 25
                    text "{size=30}The Shifting Mound Movement I{/size}" ypos song_ypos xpos 0
                    $ song_ypos += 25

                # second loop
                if final_ending != "oblivion":
                    if oblivion_when_met == 1:
                        text "{size=30}Oblivion{/size}" ypos song_ypos xpos 0
                        $ song_ypos += 25
                if loops_finished >= 2:
                    if second_mound == "adversary":
                        text "{size=30}The Song We Write in Our Blood{/size}" ypos song_ypos xpos 0
                    elif second_mound == "needle":
                        text "{size=30}The Eye of the Needle{/size}" ypos song_ypos xpos 0
                    elif second_mound == "beast":
                        text "{size=30}I Am So Much More Than You{/size}" ypos song_ypos xpos 0
                    elif second_mound == "damsel":
                        text "{size=30}It Was Always That Easy{/size}" ypos song_ypos xpos 0
                    elif second_mound == "dereal":
                        text "{size=30}I Just Want to Make You Happy{/size}" ypos song_ypos xpos 0
                    elif second_mound == "nightmare":
                        text "{size=30}I Want to Watch It Happen{/size}" ypos song_ypos xpos 0
                    elif second_mound == "clarity":
                        text "{size=30}The Moment of Clarity{/size}" ypos song_ypos xpos 0
                    elif second_mound == "prisonerhead":
                        text "{size=30}Eyes on Me{/size}" ypos song_ypos xpos 0
                    elif second_mound == "prisonerchain":
                        text "{size=30}I Don't Like Small Talk{/size}" ypos song_ypos xpos 0
                    elif second_mound == "razorheart":
                        text "{size=30}The Razor{/size}" ypos song_ypos xpos 0
                    elif second_mound == "razor":
                        text "{size=30}Mutually Assured Destruction{/size}" ypos song_ypos xpos 0
                    elif second_mound == "spectre":
                        if spectre_end == "free":
                            text "{size=30}Hitching a Ride{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}The Spectre{/size}" ypos song_ypos xpos 0
                    elif second_mound == "stranger":
                        text "{size=30}To Be Everything{/size}" ypos song_ypos xpos 0
                    elif second_mound == "tower":
                        text "{size=30}Supplication{/size}" ypos song_ypos xpos 0
                    elif second_mound == "witch":
                        text "{size=30}It's in Our Nature{/size}" ypos song_ypos xpos 0
                    elif second_mound == "thorn":
                        if thorn_end == "free_kiss":
                            text "{size=30}A Kiss From a Thorn{/size}" ypos song_ypos xpos 0
                        elif thorn_end == "free":
                            text "{size=30}The Thorn{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}A Moment Trapped for All Time{/size}" ypos song_ypos xpos 0
                    elif second_mound == "greydamsel":
                        text "{size=30}The Grey (Fire){/size}" ypos song_ypos xpos 0
                    elif second_mound == "greyprisoner":
                        text "{size=30}The Grey (Water){/size}" ypos song_ypos xpos 0
                    elif second_mound == "wildnerves":
                        text "{size=30}The Wild{/size}" ypos song_ypos xpos 0
                    elif second_mound == "wildwound":
                        text "{size=30}The Wild{/size}" ypos song_ypos xpos 0
                    elif second_mound == "wraith":
                        text "{size=30}I'm Taking What I'm Owed{/size}" ypos song_ypos xpos 0
                    elif second_mound == "apotheosis":
                        if final_ending != "liberation":
                            text "{size=30}The Apotheosis{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}A Tapestry Undone{/size}" ypos song_ypos xpos 0
                    elif second_mound == "den":
                        if beast_2_end == "free":
                            text "{size=30}Hand-in-Claw{/size}" ypos song_ypos xpos 0
                        elif beast_2_end == "consume" or beast_2_end == "slay":
                            text "{size=30}The Rhythm of the Flesh{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}The Den{/size}" ypos song_ypos xpos 0
                    elif second_mound == "fury":
                        if fury_end == "leave" or fury_end == "free" or fury_end == "slay":
                            text "{size=30}There's Nothing I Can Do To Bring You Back{/size}" ypos song_ypos xpos 0
                        elif fury_end == "slay_unarmed":
                            text "{size=30}The Bell{/size}" ypos song_ypos xpos 0
                        elif fury_end == "slay_tower":
                            text "{size=30}An Empty Void that Dared to Dream it Was Alive{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}The Fury{/size}" ypos song_ypos xpos 0
                    elif second_mound == "furyheart":
                        text "{size=30}Thirty-Trillion Cells{/size}" ypos song_ypos xpos 0
                    elif second_mound == "happy":
                        if happy_end == "dance":
                            text "{size=30}I Meant It{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}What Remains After the Fire{/size}" ypos song_ypos xpos 0
                    elif second_mound == "happydry":
                        text "{size=30}Our Happy Ending{/size}" ypos song_ypos xpos 0
                    elif second_mound == "dragonhand":
                        text "{size=30}The Life-Taker{/size}" ypos song_ypos xpos 0
                    elif second_mound == "dragonfused":
                        text "{size=30}The Princess and the Dragon{/size}" ypos song_ypos xpos 0
                    elif second_mound == "dragon":
                        text "{size=30}What Once Was One{/size}" ypos song_ypos xpos 0
                    elif second_mound == "cage":
                        if cage_end == "free":
                            text "{size=30}An Open Door{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}A Prison of Flesh{/size}" ypos song_ypos xpos 0
                    $ song_ypos += 25
                    text "{size=30}The Shifting Mound Movement II{/size}" ypos song_ypos xpos 0
                    $ song_ypos += 25

                # third mound
                if final_ending != "oblivion":
                    if oblivion_when_met == 2:
                        text "{size=30}Oblivion{/size}" ypos song_ypos xpos 0
                        $ song_ypos += 25
                if loops_finished >= 3:
                    if third_mound == "adversary":
                        text "{size=30}The Song We Write in Our Blood{/size}" ypos song_ypos xpos 0
                    elif third_mound == "needle":
                        text "{size=30}The Eye of the Needle{/size}" ypos song_ypos xpos 0
                    elif third_mound == "beast":
                        text "{size=30}I Am So Much More Than You{/size}" ypos song_ypos xpos 0
                    elif third_mound == "damsel":
                        text "{size=30}It Was Always That Easy{/size}" ypos song_ypos xpos 0
                    elif third_mound == "dereal":
                        text "{size=30}I Just Want to Make You Happy{/size}" ypos song_ypos xpos 0
                    elif third_mound == "nightmare":
                        text "{size=30}I Want to Watch It Happen{/size}" ypos song_ypos xpos 0
                    elif third_mound == "clarity":
                        text "{size=30}The Moment of Clarity{/size}" ypos song_ypos xpos 0
                    elif third_mound == "prisonerhead":
                        text "{size=30}Eyes on Me{/size}" ypos song_ypos xpos 0
                    elif third_mound == "prisonerchain":
                        text "{size=30}I Don't Like Small Talk{/size}" ypos song_ypos xpos 0
                    elif third_mound == "razorheart":
                        text "{size=30}The Razor{/size}" ypos song_ypos xpos 0
                    elif third_mound == "razor":
                        text "{size=30}Mutually Assured Destruction{/size}" ypos song_ypos xpos 0
                    elif third_mound == "spectre":
                        if spectre_end == "free":
                            text "{size=30}Hitching a Ride{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}The Spectre{/size}" ypos song_ypos xpos 0
                    elif third_mound == "stranger":
                        text "{size=30}To Be Everything{/size}" ypos song_ypos xpos 0
                    elif third_mound == "tower":
                        text "{size=30}Supplication{/size}" ypos song_ypos xpos 0
                    elif third_mound == "witch":
                        text "{size=30}It's in Our Nature{/size}" ypos song_ypos xpos 0
                    elif third_mound == "thorn":
                        if thorn_end == "free_kiss":
                            text "{size=30}A Kiss From a Thorn{/size}" ypos song_ypos xpos 0
                        elif thorn_end == "free":
                            text "{size=30}The Thorn{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}A Moment Trapped for All Time{/size}" ypos song_ypos xpos 0
                    elif third_mound == "greydamsel":
                        text "{size=30}The Grey (Fire){/size}" ypos song_ypos xpos 0
                    elif third_mound == "greyprisoner":
                        text "{size=30}The Grey (Water){/size}" ypos song_ypos xpos 0
                    elif third_mound == "wildnerves":
                        text "{size=30}The Wild{/size}" ypos song_ypos xpos 0
                    elif third_mound == "wildwound":
                        text "{size=30}The Wild{/size}" ypos song_ypos xpos 0
                    elif third_mound == "wraith":
                        text "{size=30}I'm Taking What I'm Owed{/size}" ypos song_ypos xpos 0
                    elif third_mound == "apotheosis":
                        if final_ending != "liberation":
                            text "{size=30}The Apotheosis{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}A Tapestry Undone{/size}" ypos song_ypos xpos 0
                    elif third_mound == "den":
                        if beast_2_end == "free":
                            text "{size=30}Hand-in-Claw{/size}" ypos song_ypos xpos 0
                        elif beast_2_end == "consume" or beast_2_end == "slay":
                            text "{size=30}The Rhythm of the Flesh{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}The Den{/size}" ypos song_ypos xpos 0
                    elif third_mound == "fury":
                        if fury_end == "leave" or fury_end == "free" or fury_end == "slay":
                            text "{size=30}There's Nothing I Can Do To Bring You Back{/size}" ypos song_ypos xpos 0
                        elif fury_end == "slay_unarmed":
                            text "{size=30}The Bell{/size}" ypos song_ypos xpos 0
                        elif fury_end == "slay_tower":
                            text "{size=30}An Empty Void that Dared to Dream it Was Alive{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}The Fury{/size}" ypos song_ypos xpos 0
                    elif third_mound == "furyheart":
                        text "{size=30}Thirty-Trillion Cells{/size}" ypos song_ypos xpos 0
                    elif third_mound == "happy":
                        if happy_end == "dance":
                            text "{size=30}I Meant It{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}What Remains After the Fire{/size}" ypos song_ypos xpos 0
                    elif third_mound == "happydry":
                        text "{size=30}Our Happy Ending{/size}" ypos song_ypos xpos 0
                    elif third_mound == "dragonhand":
                        text "{size=30}The Life-Taker{/size}" ypos song_ypos xpos 0
                    elif third_mound == "dragonfused":
                        text "{size=30}The Princess and the Dragon{/size}" ypos song_ypos xpos 0
                    elif third_mound == "dragon":
                        text "{size=30}What Once Was One{/size}" ypos song_ypos xpos 0
                    elif third_mound == "cage":
                        if cage_end == "free":
                            text "{size=30}An Open Door{/size}" ypos song_ypos xpos 0
                        else:
                            text "{size=30}A Prison of Flesh{/size}" ypos song_ypos xpos 0
                    $ song_ypos += 25
                    if oblivion_when_met != 2 and oblivion_when_met != 1 and oblivion_when_met != 0 and final_ending != "oblivion":
                        text "{size=30}The Shifting Mound Movement III{/size}" ypos song_ypos xpos 0
                        $ song_ypos += 25

            vbox:
                $ song_ypos = 200
                xalign 1.0

                # third mound carry-over to stop overflow
                if (oblivion_when_met == 2 or oblivion_when_met == 1 or oblivion_when_met == 0) and final_ending != "oblivion":
                    text "{size=30}The Shifting Mound Movement III{/size}" ypos song_ypos xpos 150
                    $ song_ypos += 25

                # fourth mound
                if final_ending != "oblivion":
                    if oblivion_when_met == 3:
                        text "{size=30}Oblivion{/size}" ypos song_ypos xpos 150
                        $ song_ypos += 25
                if loops_finished >= 4:
                    if fourth_mound == "adversary":
                        text "{size=30}The Song We Write in Our Blood{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "needle":
                        text "{size=30}The Eye of the Needle{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "beast":
                        text "{size=30}I Am So Much More Than You{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "damsel":
                        text "{size=30}It Was Always That Easy{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "dereal":
                        text "{size=30}I Just Want to Make You Happy{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "nightmare":
                        text "{size=30}I Want to Watch It Happen{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "clarity":
                        text "{size=30}The Moment of Clarity{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "prisonerhead":
                        text "{size=30}Eyes on Me{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "prisonerchain":
                        text "{size=30}I Don't Like Small Talk{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "razorheart":
                        text "{size=30}The Razor{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "razor":
                        text "{size=30}Mutually Assured Destruction{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "spectre":
                        if spectre_end == "free":
                            text "{size=30}Hitching a Ride{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}The Spectre{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "stranger":
                        text "{size=30}To Be Everything{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "tower":
                        text "{size=30}Supplication{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "witch":
                        text "{size=30}It's in Our Nature{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "thorn":
                        if thorn_end == "free_kiss":
                            text "{size=30}A Kiss From a Thorn{/size}" ypos song_ypos xpos 150
                        elif thorn_end == "free":
                            text "{size=30}The Thorn{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}A Moment Trapped for All Time{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "greydamsel":
                        text "{size=30}The Grey (Fire){/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "greyprisoner":
                        text "{size=30}The Grey (Water){/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "wildnerves":
                        text "{size=30}The Wild{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "wildwound":
                        text "{size=30}The Wild{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "wraith":
                        text "{size=30}I'm Taking What I'm Owed{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "apotheosis":
                        if final_ending != "liberation":
                            text "{size=30}The Apotheosis{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}A Tapestry Undone{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "den":
                        if beast_2_end == "free":
                            text "{size=30}Hand-in-Claw{/size}" ypos song_ypos xpos 150
                        elif beast_2_end == "consume" or beast_2_end == "slay":
                            text "{size=30}The Rhythm of the Flesh{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}The Den{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "fury":
                        if fury_end == "leave" or fury_end == "free" or fury_end == "slay":
                            text "{size=30}There's Nothing I Can Do To Bring You Back{/size}" ypos song_ypos xpos 150
                        elif fury_end == "slay_unarmed":
                            text "{size=30}The Bell{/size}" ypos song_ypos xpos 150
                        elif fury_end == "slay_tower":
                            text "{size=30}An Empty Void that Dared to Dream it Was Alive{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}The Fury{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "furyheart":
                        text "{size=30}Thirty-Trillion Cells{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "happy":
                        if happy_end == "dance":
                            text "{size=30}I Meant It{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}What Remains After the Fire{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "happydry":
                        text "{size=30}Our Happy Ending{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "dragonhand":
                        text "{size=30}The Life-Taker{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "dragonfused":
                        text "{size=30}The Princess and the Dragon{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "dragon":
                        text "{size=30}What Once Was One{/size}" ypos song_ypos xpos 150
                    elif fourth_mound == "cage":
                        if cage_end == "free":
                            text "{size=30}An Open Door{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}A Prison of Flesh{/size}" ypos song_ypos xpos 150
                    $ song_ypos += 25
                    text "{size=30}The Shifting Mound Movement IV{/size}" ypos song_ypos xpos 150
                    $ song_ypos += 25

                # fifth mound

                if loops_finished >= 5:
                    if fifth_mound == "adversary":
                        text "{size=30}The Song We Write in Our Blood{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "needle":
                        text "{size=30}The Eye of the Needle{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "beast":
                        text "{size=30}I Am So Much More Than You{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "damsel":
                        text "{size=30}It Was Always That Easy{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "dereal":
                        text "{size=30}I Just Want to Make You Happy{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "nightmare":
                        text "{size=30}I Want to Watch It Happen{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "clarity":
                        text "{size=30}The Moment of Clarity{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "prisonerhead":
                        text "{size=30}Eyes on Me{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "prisonerchain":
                        text "{size=30}I Don't Like Small Talk{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "razorheart":
                        text "{size=30}The Razor{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "razor":
                        text "{size=30}Mutually Assured Destruction{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "spectre":
                        if spectre_end == "free":
                            text "{size=30}Hitching a Ride{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}The Spectre{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "stranger":
                        text "{size=30}To Be Everything{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "tower":
                        text "{size=30}Supplication{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "witch":
                        text "{size=30}It's in Our Nature{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "thorn":
                        if thorn_end == "free_kiss":
                            text "{size=30}A Kiss From a Thorn{/size}" ypos song_ypos xpos 150
                        elif thorn_end == "free":
                            text "{size=30}The Thorn{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}A Moment Trapped for All Time{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "greydamsel":
                        text "{size=30}The Grey (Fire){/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "greyprisoner":
                        text "{size=30}The Grey (Water){/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "wildnerves":
                        text "{size=30}The Wild{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "wildwound":
                        text "{size=30}The Wild{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "wraith":
                        text "{size=30}I'm Taking What I'm Owed{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "apotheosis":
                        if final_ending != "liberation":
                            text "{size=30}The Apotheosis{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}A Tapestry Undone{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "den":
                        if beast_2_end == "free":
                            text "{size=30}Hand-in-Claw{/size}" ypos song_ypos xpos 150
                        elif beast_2_end == "consume" or beast_2_end == "slay":
                            text "{size=30}The Rhythm of the Flesh{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}The Den{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "fury":
                        if fury_end == "leave" or fury_end == "free" or fury_end == "slay":
                            text "{size=30}There's Nothing I Can Do To Bring You Back{/size}" ypos song_ypos xpos 150
                        elif fury_end == "slay_unarmed":
                            text "{size=30}The Bell{/size}" ypos song_ypos xpos 150
                        elif fury_end == "slay_tower":
                            text "{size=30}An Empty Void that Dared to Dream it Was Alive{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}The Fury{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "furyheart":
                        text "{size=30}Thirty-Trillion Cells{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "happy":
                        if happy_end == "dance":
                            text "{size=30}I Meant It{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}What Remains After the Fire{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "happydry":
                        text "{size=30}Our Happy Ending{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "dragonhand":
                        text "{size=30}The Life-Taker{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "dragonfused":
                        text "{size=30}The Princess and the Dragon{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "dragon":
                        text "{size=30}What Once Was One{/size}" ypos song_ypos xpos 150
                    elif fifth_mound == "cage":
                        if cage_end == "free":
                            text "{size=30}An Open Door{/size}" ypos song_ypos xpos 150
                        else:
                            text "{size=30}A Prison of Flesh{/size}" ypos song_ypos xpos 150
                    $ song_ypos += 25
                    if final_ending != "slay" and final_ending != "good":
                        text "{size=30}The Long Quiet{/size}" ypos song_ypos xpos 150
                        $ song_ypos += 25
                    text "{size=30}The Shifting Mound Movement V{/size}" ypos song_ypos xpos 150
                    $ song_ypos += 25
                    if mound_fight_triggered:
                        text "{size=30}Transformation{/size}" ypos song_ypos xpos 150
                        $ song_ypos += 25
                if final_ending == "oblivion":
                    text "{size=30}Oblivion{/size}" ypos song_ypos xpos 150
                if final_ending == "liberation":
                    text "{size=30}The Apotheosis{/size}" ypos song_ypos xpos 150
                if final_ending == "slay":
                    text "{size=30}The Long Quiet{/size}" ypos song_ypos xpos 150
                if final_ending == "loop":
                    text "{size=30}The End of Everything, The Beginning of Something New{/size}" ypos song_ypos xpos 150
                if final_ending == "good":
                    text "{size=30}The Long Quiet{/size}" ypos song_ypos xpos 150
                if final_ending == "leave":
                    text "{size=30}The Unknown Together{/size}" ypos song_ypos xpos 150

screen ending():
    style_prefix "navigation"

    imagebutton:
        #auto "images/credits/sh_end_%s.png"
        auto "images/credits/sh_border_%s.png"
        xpos 99
        ypos 425
        action OpenURL("steam://openurl/https://store.steampowered.com/app/1609230/Scarlet_Hollow/")

    imagebutton:
        auto "images/credits/wl_end_%s.png"
        xpos 1286
        ypos 425
        action OpenURL("steam://openurl/https://store.steampowered.com/app/1989270/Slay_the_Princess/")

    imagebutton:
        auto "images/credits/discord_end_%s.png"
        xpos 660
        ypos 841
        action OpenURL("https://discord.com/invite/xCnAeqkkEY")

    #textbutton _("Continue") action Jump("credits") xpos 1412 ypos 941


    imagebutton:
        #auto "images/credits/continue_end_%s.png"
        #xpos 1612
        #ypos 941
        auto "images/credits/continue_%s.png"
        xpos 1412
        ypos 941
        action Jump("credits")

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen fake_menu():
    key "K_ESCAPE" action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]
    key "pad_start_press" action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]
    key "pad_b_press" action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]
    tag menu
    modal True

    if persistent.performance_mode == False and persistent.flickering:
        add Movie(size=(1920, 1080))
        on "show" action Play("movie", "images/menu/main_menu.webm", loop=True)
        on "hide" action Stop("movie")
        on "hide" action Hide(screen = "navigation")
        on "replace" action Play("movie", "images/menu/main_menu.webm", loop=True)
        on "replace" action Show(screen = "navigation")
        on "replaced" action Stop("movie")
    else:
        add "menu static"
    #add "choices_backdrop_menu"
    #add "logo_menu_final"
    add "logo_menu_pristine"

    vbox:
        style_prefix "main_menu"
        xalign 0.5
        #xpos 1737
        xpos 237
        yanchor 0
        yoffset 230

        spacing gui.navigation_spacing

        textbutton _("Continue") action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]

        textbutton _("Continue") action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]

        textbutton _("Continue") action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]

        textbutton _("Continue") action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]
        textbutton _("Continue") action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]
        textbutton _("Continue") action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]
        textbutton _("Continue") action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]
        textbutton _("Continue") action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]
        textbutton _("Continue") action [Hide(screen = "fake_menu"), Jump("console_wait_jump")]

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    if persistent.performance_mode == False and persistent.flickering:
        add Movie(size=(1920, 1080), channel="mm_movie")
        on "show" action Play("mm_movie", "images/menu/main_menu.webm", loop=True)
        on "hide" action Stop("mm_movie")
        on "hide" action Hide(screen = "navigation")
        on "replace" action Play("mm_movie", "images/menu/main_menu.webm", loop=True)
        on "replace" action Show(screen = "navigation")
        on "replaced" action Stop("mm_movie")
    else:
        add "menu static"
    #add "choices_backdrop_menu"
    #add "logo_menu_final"
    add "logo_menu_pristine"

    vbox:
        style_prefix "main_menu"
        xalign 0.5
        #xpos 1737
        xpos 237
        yanchor 0
        yoffset 230

        spacing gui.navigation_spacing


    # add this where appropriate
        if renpy.newest_slot != None:

            textbutton _("Continue") action Continue() default_focus True

        textbutton _("New Game") action Start() default_focus True

        textbutton _("Load Game") action ShowMenu("load") default_focus True

        textbutton _("Preferences") action ShowMenu("preferences")

        #if renpy.variant("console_xbox"):
        #    textbutton _("Controls") action ShowMenu("help_xbox")

        #if renpy.variant("console_sony_ps5") or renpy.variant("console_sony_ps4"):
        #    textbutton _("Controls") action ShowMenu("help_ps")

        #if renpy.variant("console_nintendo_switch"):
        #    textbutton _("Controls") action ShowMenu("help_switch")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Controls") action ShowMenu("help")

        if not renpy.variant("console"):
            textbutton _("Accessibility") action ToggleScreen("_accessibility")

        #textbutton "Gallery" action [ShowMenu("gallery"), Show("specialdisableclick")]

        #textbutton "Memories" action [ShowMenu("gallery"), Play("music", "audio/_music/mound/Oblivion.flac")]
        if persistent.gallery_unlocked:
            textbutton _("Memories") action [ShowMenu("gallery"), Play("musicgallery", "audio/_music/mound/Oblivion.flac"), PauseAudio("music", True), PauseAudio("music2", True),PauseAudio("music3", True),PauseAudio("music4", True),PauseAudio("music5", True),PauseAudio("sound", True),PauseAudio("secondary", True),PauseAudio("tertiary", True)]

        if persistent.gallery_unlocked:
            textbutton _("Reset Gallery") action [Confirm(_("Are you sure you want to clear your gallery progress? This action cannot be undone."), yes = Function(galleryInitializer.reset_galleries))]

        textbutton _("Subtitle Language") action ShowMenu("language_select_menu")

        #textbutton _("Wishlist on Steam") action OpenURL("steam://openurl/https://store.steampowered.com/app/1989270/Slay_the_Princess")

        # STEAM
        #textbutton _("Visit Scarlet Hollow") action OpenURL("steam://openurl/https://store.steampowered.com/app/1609230/Scarlet_Hollow/")

        # GOG
        # textbutton _("Visit Scarlet Hollow") action OpenURL("https://www.gog.com/en/game/scarlet_hollow")
        if renpy.variant("pc"):
            textbutton _("Join Our Discord") action OpenURL("https://discord.gg/blacktabbygames")

        #textbutton _("Follow us on Twitter") action OpenURL("https://twitter.com/blacktabbygames")

        #textbutton _("Follow us on Twitter") action OpenURL("https://twitter.com/blacktabbygames")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

    ## This empty frame darkens the main menu.
    #frame:
    #    style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    #imagebutton:
    #    auto "images/menu/menu_buttons/start_%s.png"
    #    xalign 0.5
    #    xpos 1540
    #    ypos 320
    # old
        #xpos 104
        #ypos 793
        #action Start()

    #imagebutton:
    #    auto "images/menu/menu_buttons/load_%s.png"
    #    xalign 0.5
    #    xpos 1540
    #    ypos 420
        #xpos 463
        #ypos 793
    #    action ShowMenu("load")

    #imagebutton:
    #    auto "images/menu/menu_buttons/options_%s.png"
    #    xalign 0.5
    #    xpos 1540
    #    ypos 520
    # old
        #xpos 769
        #ypos 793
    #    action ShowMenu("preferences")

    #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
    #    imagebutton:
    #        auto "images/menu/menu_buttons/controls_%s.png"
    #        xalign 0.5
    #        xpos 1540
    #        ypos 620
    # old
            #xpos 1109
            #ypos 793
    #        action ShowMenu("help")



    #imagebutton:
    #    auto "images/menu/menu_buttons/wishlist_%s.png"
    #    xalign 0.5
    #    xpos 1540
    #    ypos 720
        # old
        #xpos 292
        #ypos 940
    #    action OpenURL("steam://openurl/https://store.steampowered.com/app/1989270/Slay_the_Princess")

    #imagebutton:
    #    auto "images/menu/menu_buttons/sh_%s.png"
    #    xalign 0.5
    #    xpos 1540
    #    ypos 820
    # old
        #xpos 935
        #ypos 945
        #action OpenURL("steam://openurl/https://store.steampowered.com/app/1609230/Scarlet_Hollow/")

    #if renpy.variant("pc"):
    #    imagebutton:
    #        auto "images/menu/menu_buttons/quit_%s.png"
    #        xalign 0.5
    #        xpos 1540
    #        ypos 920
    # old
            #xpos 1527
            #ypos 793
    #        action Quit(confirm=not main_menu)

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 0.5
    xoffset -30
    xmaximum 1200
    #yalign 1.0
    #yoffset -30

style main_menu_button:
    xalign 0.5

style main_menu_button_text is default:
    xalign 0.5
    properties gui.button_text_properties("choice_button")
    #color "#ffffff"
    outlines [ (3, "#000000")]

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen language_select():

    add "images/_sprites/special/farback quiet p.png" at distortion

    text _("Subtitle Language") ypos 50 xalign 0.5 size 125 style "spookytext_style"


    #textbutton "English":
    #    action Confirm("Set English as your subtitle language?", yes = [Language(None), SetVariable ("persistent.language_set", True), SetVariable("language_string", "english"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")])


    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}English{/font}":
        xalign 0.5
        ypos 225
        xpos 750
        #text_color 'c2c2c2'
        #text_hover_color '#a84232'

        action [Language(None), SetVariable ("persistent.language_set", True), SetVariable("language_string", "english"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Español (LATAM){/font}":
        xalign 0.5
        ypos 350
        xpos 750

        action [Language("spanish_latam"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "spanish_latam"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]

    textbutton "{font=gui/fonts/tl/chinese/NotoSerifTC-VariableFont_wght.ttf}繁體中文{/font}":

        xalign 0.5
        ypos 475
        xpos 750

        action [Language("chinese_traditional"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "chinese_traditional"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Português (Brasil){/font}":
        ypos 600
        xalign 0.5
        xpos 750

        action [Language("pt_br"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "pt_br"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]



    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Polski{/font}":
        xalign 0.5
        ypos 725
        xpos 750

        action [Language("polish"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "polish"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]



    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Deutsch{/font}":
        ypos 850
        xalign 0.5
        xpos 750

        action [Language("german"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "german"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Français{/font}":
        xalign 0.5
        ypos 225
        xpos 1170

        action [Language("french"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "french"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]




    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Español (EU){/font}":
        ypos 350
        xalign 0.5
        xpos 1170

        action [Language("spanish_eu"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "spanish_eu"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]

    textbutton "{font=gui/fonts/tl/chinese/SourceHanSans-Normal.ttf}简体中文{/font}":

        xalign 0.5
        ypos 475
        xpos 1170

        action [Language("chinese_simplified"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "chinese_simplified"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Русский{/font}":
        ypos 600
        xalign 0.5
        xpos 1170

        action [Language("russian"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "russian"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Українська{/font}":
        ypos 725
        xalign 0.5
        xpos 1170

        action [Language("ukrainian"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "ukrainian"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]
    
    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Italiano{/font}":
        ypos 850
        xalign 0.5
        xpos 1170

        action [Language("italian"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "italian"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]

    textbutton "{font=gui/fonts/tl/korean/NotoSerifKR-VariableFont_wght.ttf}한국어{/font}":
        ypos 950
        xalign 0.5
        xpos 750

        action [Language("korean"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "korean"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]

    textbutton "{font=gui/fonts/tl/japanese/NewTegomin-Regular.ttf}日本語{/font}":
        ypos 950
        xalign 0.5
        xpos 1170

        action [Language("japanese"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "japanese"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")]



screen language_select_menu():

    key "K_ESCAPE"  action Return()
    key "K_BACKSPACE" action Return()
    key "pad_start_press" action Return()
    key "pad_b_press" action Return()

    tag menu

    add "images/_sprites/special/farback quiet p.png" at distortion

    text _("Subtitle Language") ypos 50 xalign 0.5 size 125 style "spookytext_style"


    #textbutton "English":
    #    action Confirm("Set English as your subtitle language?", yes = [Language(None), SetVariable ("persistent.language_set", True), SetVariable("language_string", "english"), Hide("language_select", Dissolve(1.0)), Jump("splashscreen")])


    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}English{/font}":
        xalign 0.5
        ypos 225
        xpos 750
        #text_color 'c2c2c2'
        #text_hover_color '#a84232'

        action [Language(None), SetVariable ("persistent.language_set", True), SetVariable("language_string", "english"), Hide("language_select_menu", Dissolve(0.5)), Return()]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Español (LATAM){/font}":
        xalign 0.5
        ypos 350
        xpos 750

        action [Language("spanish_latam"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "spanish_latam"), Hide("language_select_menu", Dissolve(0.5)), Return()]

    textbutton "{font=gui/fonts/tl/chinese/NotoSerifTC-VariableFont_wght.ttf}繁體中文{/font}":

        xalign 0.5
        ypos 475
        xpos 750

        action [Language("chinese_traditional"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "chinese_traditional"), Hide("language_select_menu", Dissolve(0.5)), Return()]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Português (Brasil){/font}":
        ypos 600
        xalign 0.5
        xpos 750

        action [Language("pt_br"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "pt_br"), Hide("language_select_menu", Dissolve(0.5)), Return()]



    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Polski{/font}":
        xalign 0.5
        ypos 725
        xpos 750

        action [Language("polish"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "polish"), Hide("language_select_menu", Dissolve(0.5)), Return()]



    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Deutsch{/font}":
        ypos 850
        xalign 0.5
        xpos 750

        action [Language("german"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "german"), Hide("language_select_menu", Dissolve(0.5)), Return()]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Français{/font}":
        xalign 0.5
        ypos 225
        xpos 1170

        action [Language("french"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "french"), Hide("language_select_menu", Dissolve(0.5)), Return()]




    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Español (EU){/font}":
        ypos 350
        xalign 0.5
        xpos 1170

        action [Language("spanish_eu"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "spanish_eu"), Hide("language_select_menu", Dissolve(0.5)), Return()]

    textbutton "{font=gui/fonts/tl/chinese/SourceHanSans-Normal.ttf}简体中文{/font}":

        xalign 0.5
        ypos 475
        xpos 1170

        action [Language("chinese_simplified"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "chinese_simplified"), Hide("language_select_menu", Dissolve(0.5)), Return()]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Русский{/font}":
        ypos 600
        xalign 0.5
        xpos 1170

        action [Language("russian"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "russian"), Hide("language_select_menu", Dissolve(0.5)), Return()]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Українська{/font}":
        ypos 725
        xalign 0.5
        xpos 1170

        action [Language("ukrainian"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "ukrainian"), Hide("language_select_menu", Dissolve(0.5)), Return()]

    textbutton "{font=gui/fonts/tl/latin/NotoSerif-VariableFont_wdth,wght.ttf}Italiano{/font}":
        ypos 850
        xalign 0.5
        xpos 1170

        action [Language("italian"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "italian"), Hide("language_select_menu", Dissolve(0.5)), Return()]

    textbutton "{font=gui/fonts/tl/korean/NotoSerifKR-VariableFont_wght.ttf}한국어{/font}":
        ypos 950
        xalign 0.5
        xpos 750

        action [Language("korean"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "korean"), Hide("language_select_menu", Dissolve(0.5)), Return()]

    textbutton "{font=gui/fonts/tl/japanese/NewTegomin-Regular.ttf}日本語{/font}":
        ypos 950
        xalign 0.5
        xpos 1170

        action [Language("japanese"), SetVariable ("persistent.language_set", True), SetVariable("language_string", "japanese"), Hide("language_select_menu", Dissolve(0.5)), Return()]


screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():
    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                if renpy.variant("console"):
                    for page in range(1, 9):
                        textbutton "[page]" action FilePage(page)
                else:
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                if renpy.variant("console"):
                    textbutton _(">") action FilePageNext(max=8)
                else:
                    textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences")):

        vbox:
            ypos -50
            hbox:
                #box_wrap True

                if (renpy.variant("pc") or renpy.variant("web")) and renpy.variant("steam_deck") == False:

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window") text_style "kelmscott"
                        textbutton _("Fullscreen") action Preference("display", "fullscreen") text_style "kelmscott"

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle") text_style "kelmscott"
                    textbutton _("After Choices") action Preference("after choices", "toggle") text_style "kelmscott"
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) text_style "kelmscott"


                vbox:
                    style_prefix "radio"
                    label _("Quick Menu")
                    textbutton _("Visible") action [SetVariable("persistent.quick_menu", True), SetVariable("quick_menu", True)] text_style "kelmscott"
                    textbutton _("Hidden") action [SetVariable("persistent.quick_menu", False), SetVariable("quick_menu", False)] text_style "kelmscott"

                if renpy.variant("steam_deck") == False:
                    vbox:
                        style_prefix "radio"
                        label _("Blinking CTC")
                        textbutton _("On") action SetVariable("persistent.ctc", True) text_style "kelmscott"
                        textbutton _("Off") action SetVariable("persistent.ctc", False) text_style "kelmscott"

                #vbox:
                #    style_prefix "radio"
                #    label _("Rollback Side")
                #    textbutton _("Disable") action Preference("rollback side", "disable")
                #    textbutton _("Left") action Preference("rollback side", "left")
                #    textbutton _("Right") action Preference("rollback side", "right")



                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (1.8 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    style_prefix "radio"
                    label _("Boil Effect")
                    textbutton _("On") action SetVariable("persistent.performance_mode", False) text_style "kelmscott"
                    textbutton _("Off") action SetVariable("persistent.performance_mode", True) text_style "kelmscott"

                if renpy.variant("steam_deck") == False:
                    vbox:
                        style_prefix "radio"
                        label _("Parallax Effect")
                        textbutton _("On") action SetVariable("persistent.parallax_on", True) text_style "kelmscott"
                        textbutton _("Off") action SetVariable("persistent.parallax_on", False) text_style "kelmscott"

                vbox:
                    style_prefix "radio"
                    label _("Flickering Images")
                    textbutton _("On") action SetVariable("persistent.flickering", True) text_style "kelmscott"
                    textbutton _("Off") action SetVariable("persistent.flickering", False) text_style "kelmscott"

                if renpy.variant("steam_deck") == False:
                    vbox:
                        style_prefix "radio"
                        label _("Auto-Advance Text")
                        textbutton _("On") action SetVariable("preferences.afm_enable", True) text_style "kelmscott"
                        textbutton _("Off") action SetVariable("preferences.afm_enable", False) text_style "kelmscott"



            null height (1.8 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                vbox:

                #    label _("Text Speed")

                #    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                #vbox:
                #    style_prefix "radio"
                #    label _("Revert to old OST. (Not recommended)")
                #    textbutton _("On") action SetVariable("persistent.flickering", True)
                #    textbutton _("Off") action SetVariable("persistent.flickering", False)


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_button_text_hover_color is gui_button_text_hover_color
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    key "K_j" action Return()
    key "pad_righttrigger_pos" action Return()

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        #if "color" in h.who_args:
                            #text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Controls"), scroll="viewport"):
        style_prefix "help"

        vbox:
            spacing 20

            hbox:

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad") default_focus True

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard") default_focus True
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")



            if device == "gamepad":
                use gamepad_help
            elif device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help


screen keyboard_help():

    if not renpy.variant("console"):
        hbox:
            label "Shift+A"
            text _("Opens the accessibility menu.")

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Tab//Ctrl")
        text _("Skips dialogue when pressed//while held down.")

    hbox:
        label _("T")
        text _("Toggles auto-advancing dialogue.")

    hbox:
        label _("F5")
        text _("Quick Save.")

    hbox:
        label _("F9")
        text _("Quick load.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "J"
        text _("History.")




screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel")
        text _("Scroll dialogue options.")

screen help_xbox():

    key "K_ESCAPE" action Return()


    key "K_BACKSPACE" action Return()

    key "pad_start_press" action Return()
    key "pad_b_press" action Return()

    tag menu

    add "images/_sprites/special/farback quiet p.png"
    add "gui/controller/controller xbox.png" at distortion

    text _("Quick Save.") ypos 230 xpos 310
    text _("Quick Load.") ypos 130 xpos 570

    text _("History.") ypos 150 xpos 1080
    text _("Skips previously seen dialogue.") ypos 230 xpos 1230
    text _("Accesses the game menu.") ypos 325 xpos 1370

    text _("Hides the user interface.") ypos 395 xpos 1408
    text _("Auto") ypos 455 xpos 1450

    text _("Back.") ypos 535 xpos 1470
    text _("Select.") ypos 690 xpos 1460

    text _("Navigate the interface.") ypos 500 xpos 90
    text _("Navigate the interface.") ypos 900 xalign 0.475

    textbutton _("Return"):
        style "return_button"

        action Return()


screen help_switch():

    key "K_ESCAPE" action Return()


    key "K_BACKSPACE" action Return()

    key "pad_start_press" action Return()
    key "pad_b_press" action Return()

    tag menu

    add "images/_sprites/special/farback quiet p.png"
    add "gui/controller/controller switch.png" at distortion

    text _("Quick Save.") ypos 215 xpos 395
    text _("Quick Load.") ypos 130 xpos 670

    text _("History.") ypos 130 xpos 1080
    text _("Skips previously seen dialogue.") ypos 190 xpos 1250
    text _("Accesses the game menu.") ypos 335 xpos 1410

    text _("Hides the user interface.") ypos 400 xpos 1400
    text _("Auto") ypos 470 xpos 1430

    text _("Back.") ypos 543 xpos 1420
    text _("Select.") ypos 650 xpos 1425

    #text _("Navigate the interface.") ypos 450 xpos 125
    #text _("Navigate the interface.") ypos 575 xpos 110
    text _("Navigate the interface.") ypos 510 xpos 170

    text _("Navigate the interface.") ypos 760 xpos 1410

    textbutton _("Return"):
        style "return_button"

        action Return()



screen help_ps():

    key "K_ESCAPE" action Return()


    key "K_BACKSPACE" action Return()

    key "pad_start_press" action Return()
    key "pad_b_press" action Return()

    tag menu

    add "images/_sprites/special/farback quiet p.png"
    add "gui/controller/controller sony.png" at distortion

    text _("Quick Save.") ypos 350 xpos 240
    text _("Quick Load.") ypos 170 xpos 310

    text _("History.") ypos 220 xpos 1330
    text _("Skips previously seen dialogue.") ypos 285 xpos 1350
    text _("Accesses the game menu.") ypos 345 xpos 1370

    text _("Hides the user interface.") ypos 410 xpos 1370
    text _("Auto") ypos 490 xpos 1370

    text _("Back.") ypos 580 xpos 1390
    text _("Select.") ypos 715 xpos 1385

    text _("Navigate the interface.") ypos 515 xalign 0.085
    text _("Navigate the interface.") ypos 800 xalign 0.5

    textbutton _("Return"):
        style "return_button"

        action Return()



screen gamepad_help():

    hbox:
        label _("Bottom Face Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Right Trigger")
        text _("History.")

    hbox:
        label _("Right Shoulder")
        text _("Skips previously seen dialogue.")

    hbox:
        label _("Left Shoulder")
        text _("Quick Save.")

    hbox:
        label _("Back\nSelect")
        text _("Quick Load.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Face Button")
        text _("Hides the user interface.")

    hbox:
        label _("X/Left Face Button")
        text _("Toggles auto-advancing dialogue.")

    hbox:
        label _("Left Trigger")
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    textbutton _("Calibrate") action GamepadCalibrate()



style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:

    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action text_style("amatic") text_size 45
                textbutton _("No") action no_action text_style("amatic") text_size 45 default_focus True

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)



style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
