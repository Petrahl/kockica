if_i_press_shake_the_numbers_will_freeze = 0

def on_gesture_shake():
    global if_i_press_shake_the_numbers_will_freeze
    if True:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # . . .
                        . . # . .
                        . . . # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . . . . .
                        . # # # .
                        . . . . .
        """)
        if_i_press_shake_the_numbers_will_freeze = 6
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
