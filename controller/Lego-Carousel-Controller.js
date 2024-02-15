radio.setGroup(1)
let maxSpeed = 60

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendValue("start", maxSpeed)
})

input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    if (maxSpeed <= 100) {
        maxSpeed += 5
    } else {
        maxSpeed = 10
    }
    
})

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendValue("stop", 0)
})

basic.forever(function on_forever() {
    basic.showNumber(maxSpeed)
})