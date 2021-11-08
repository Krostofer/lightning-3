a_button = 0
button_a_sound = 0
lightning_timer = 0
lightning_distance = 0
lightning_distance_kilometres = 0
display_complete = 0

def on_button_pressed_a():
    global a_button, button_a_sound, lightning_timer
    a_button += 1
    button_a_sound += 1
    while a_button > 0:
        lightning_timer += 1
        basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("Press the A button when you see the lightning.")
    basic.show_string("Press the B button when you see the thunder.")
    basic.show_string("Press A + B to repeat the lightning distance.")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global a_button, lightning_distance, lightning_distance_kilometres, display_complete
    music.stop_all_sounds()
    a_button = 0
    if lightning_timer > 0:
        basic.show_string("" + str((lightning_timer)))
        basic.show_string(" seconds.")
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        basic.pause(1000)
        lightning_distance = lightning_timer * 340
        basic.show_string(" Lightning is ")
        basic.show_string("" + str((lightning_distance)))
        basic.show_string(" metres away.")
        basic.show_leds("""
            . . . # #
                        . . # # #
                        . # # # .
                        # # # . .
                        # # . . .
        """)
        lightning_distance_kilometres = lightning_distance / 1000
        basic.show_string(" Or: ")
        basic.show_string("" + str((lightning_distance_kilometres)))
        basic.show_string(" km away")
        display_complete = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if display_complete == 1:
        basic.show_string(" Lightning is ")
        basic.show_string("" + str((lightning_distance)))
        basic.show_string(" metres away.")
        basic.show_leds("""
            . . . # #
                        . . # # #
                        . # # # .
                        # # # . .
                        # # . . .
        """)
        basic.show_string(" Or: ")
        basic.show_string("" + str((lightning_distance_kilometres)))
        basic.show_string(" km away")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_microbit_id_button_a():
    music.play_melody("C5 B A G F E D C ", 120)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_A,
    1,
    on_microbit_id_button_a)
