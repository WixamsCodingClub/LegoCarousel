let isStopping = false
let isStarting = false
let currentSpeed = 0
let stopSpeed = 9
let delay = 400
radio.setGroup(1)

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (!isStarting) {
        isStopping = false
        isStarting = true
        startUp(25)
    }
    
})

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (!isStopping) {
        isStarting = false
        isStopping = true
        stop()
    }
    
})

input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    wuKong.stopMotor(wuKong.MotorList.M1)
    currentSpeed = 0
})

radio.onReceivedValue(function on_received_value(name: string, value: number) {
    if (name == "start") {
        startUp(value)
    } else if (name == "stop") {
        stop()
    }
    
})

function startUp(maxSpeed: number) {
    
    basic.showArrow(ArrowNames.North)
    currentSpeed = stopSpeed
    radio.sendString("startmusic")
    while (currentSpeed < maxSpeed) {
        if (isStopping) {
            return
        }
        
        currentSpeed += 1
        wuKong.setMotorSpeed(wuKong.MotorList.M1, currentSpeed)
        basic.pause(delay)
    }
    isStarting = false
    basic.showIcon(IconNames.Yes)
}

function stop() {
    
    basic.showArrow(ArrowNames.South)
    radio.sendString("stopmusic")
    while (currentSpeed > 0) {
        if (isStarting) {
            return
        }
        
        currentSpeed += -1
        wuKong.setMotorSpeed(wuKong.MotorList.M1, currentSpeed)
        basic.pause(delay * 0.6)
    }
    isStopping = false
    basic.showIcon(IconNames.Square)
}