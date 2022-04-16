import time
from machine import Pin, PWM

angle = 80
servo = PWM(Pin(12), freq = 50, duty = angle)

LSW = Pin(2, Pin.IN)

def close():
    global angle
    angle = 80
    servo.duty(angle)
    return angle

def open():
    global angle
    while True:
        time.sleep(0.025)
        check = LSW.value()
        if check == 1:
            angle = angle - 1
            servo.duty(angle)
        elif check == 0:
            print('triggered')
            return False
        else:
            print('error')