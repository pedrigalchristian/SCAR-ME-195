from machine import Pin, I2C
import time

from vl6180 import Sensor


i2c = I2C(scl = Pin(14), sda = Pin(12)) # 14 is D5, 12, is D6
s = Sensor(i2c)

def remap(x):
    """ Remaps x from Input Range (0 to 255) to Output Range (0 to 100)"""
    y = x * (100/255) 
    return y

while True:
    print(s.range())
    time.sleep(0.03)