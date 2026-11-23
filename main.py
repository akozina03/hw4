def on_button_pressed_a():
    global happiness, kill
    happiness += 1
    if kill:
        kill = False
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string(" Hello-AK")
    basic.show_string("S")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if not (kill):
        music.play(music.create_sound_expression(WaveShape.NOISE,
                5000,
                2559,
                142,
                255,
                1000,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_icon(IconNames.ANGRY)
        basic.pause(2000)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    if not (kill):
        basic.show_string(" Hi!")
        basic.show_icon(IconNames.HEART)
        basic.pause(2000)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

kill = False
happiness = 10
radio.set_group(8)

def on_forever():
    while not (kill):
        if input.temperature() > 17:
            basic.show_icon(IconNames.ASLEEP)
            basic.pause(5000)
        if input.temperature() <= 17:
            basic.show_icon(IconNames.CHESSBOARD)
            basic.pause(5000)
    if kill:
        basic.show_icon(IconNames.SAD)
basic.forever(on_forever)

def on_forever2():
    global happiness, kill
    basic.pause(120000)
    if not (kill):
        happiness += -1
    if happiness <= 0:
        kill = True
basic.forever(on_forever2)

def on_forever3():
    pass
basic.forever(on_forever3)
