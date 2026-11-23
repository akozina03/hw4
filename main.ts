input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    happiness += 1
    if (kill) {
        kill = false
    }
    
    basic.showIcon(IconNames.Happy)
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString(" Hello-AK")
    basic.showString("S")
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    if (!kill) {
        music.play(music.createSoundExpression(WaveShape.Noise, 5000, 2559, 142, 255, 1000, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        basic.showIcon(IconNames.Angry)
        basic.pause(2000)
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    if (!kill) {
        basic.showString(" Hi!")
        basic.showIcon(IconNames.Heart)
        basic.pause(2000)
    }
    
})
let kill = false
let happiness = 10
radio.setGroup(8)
basic.forever(function on_forever() {
    while (!kill) {
        if (input.temperature() > 17) {
            basic.showIcon(IconNames.Asleep)
            basic.pause(5000)
        }
        
        if (input.temperature() <= 17) {
            basic.showIcon(IconNames.Chessboard)
            basic.pause(5000)
        }
        
    }
    if (kill) {
        basic.showIcon(IconNames.Sad)
    }
    
})
basic.forever(function on_forever2() {
    
    basic.pause(120000)
    if (!kill) {
        happiness += -1
    }
    
    if (happiness <= 0) {
        kill = true
    }
    
})
