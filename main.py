a_button = 0
lightning_timer = 0
lightning_distance = 0
display_complete = 0

def on_button_pressed_a():
    global a_button, lightning_timer
    basic.clear_screen()
    a_button += 1
    while a_button == 1:
        basic.pause(1000)
        lightning_timer += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("Press the A button when you see the lightning.")
    basic.show_string("Press the B button when you see the thunder.")
    basic.show_string("Press A + B to repeat the lightning distance.")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global a_button, lightning_distance, display_complete
    a_button += 1
    if lightning_timer > 1:
        a_button += 1
        basic.show_string("" + str((lightning_timer)))
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
        basic.show_string("" + str((lightning_distance)))
        basic.show_string("metres.")
        display_complete = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if display_complete == 1:
        basic.show_string("" + str((lightning_distance)))
        basic.show_string("metres.")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
