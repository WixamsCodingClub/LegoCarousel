radio.set_group(1)
maxSpeed = 60

def on_button_pressed_a():
    radio.send_value("start", maxSpeed)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global maxSpeed
    if maxSpeed <= 100:
        maxSpeed += 5
    else:
        maxSpeed = 10
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_value("stop", 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_number(maxSpeed)
basic.forever(on_forever)