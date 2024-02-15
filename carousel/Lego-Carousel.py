delay = 400
stopSpeed = 9
currentSpeed = 0
isStopping = False
isStarting = False
radio.set_group(1)

def on_button_pressed_a():
    global isStopping, isStarting
    if not (isStarting):
        isStopping = False
        isStarting = True
        startUp(25)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global isStarting, isStopping
    if not (isStopping):
        isStarting = False
        isStopping = True
        stop()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global currentSpeed
    wuKong.stop_motor(wuKong.MotorList.M1)
    currentSpeed = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_value(name, value):
    if name == "start":
        startUp(value)
    elif name == "stop":
        stop()
radio.on_received_value(on_received_value)

def startUp(maxSpeed: number):
    global currentSpeed, isStarting
    basic.show_arrow(ArrowNames.NORTH)
    currentSpeed = stopSpeed
    radio.send_string("startmusic")
    while currentSpeed < maxSpeed:
        if isStopping:
            return
        currentSpeed += 1
        wuKong.set_motor_speed(wuKong.MotorList.M1, currentSpeed)
        basic.pause(delay)
    isStarting = False
    basic.show_icon(IconNames.YES)

def stop():
    global currentSpeed, isStopping
    basic.show_arrow(ArrowNames.SOUTH)
    radio.send_string("stopmusic")
    while currentSpeed > 0:
        if isStarting:
            return
        currentSpeed += -1
        wuKong.set_motor_speed(wuKong.MotorList.M1, currentSpeed)
        basic.pause(delay * 0.6)
    isStopping = False
    basic.show_icon(IconNames.SQUARE)








