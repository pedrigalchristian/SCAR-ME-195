import time
from machine import Pin, PWM, I2C
from ina219 import INA219
from logging import INFO

angle = 80
servo = PWM(Pin(12), freq = 50, duty = angle)

LSW = Pin(2, Pin.IN)

SHUNT_OHMS = 0.1
i2c = I2C(Pin(5), Pin(4))
ina = INA219(SHUNT_OHMS, i2c, log_level=INFO)
ina.configure()

def close():
    global angle
    while True:
        time.sleep(0.01)
        check = ina.current()
        if check > 0.2:
            angle = angle + 1
            servo.duty(angle)
        else:
            return False

def open():
    global angle
    while True:
        time.sleep(0.01)
        check = LSW.value()
        if check == 1:
            angle = angle - 1
            servo.duty(angle)
        elif check == 0:
            return False
        else:
            print('error')