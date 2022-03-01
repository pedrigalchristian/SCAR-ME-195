""" This program is the low-level code for the 
    stepper motors. Functions include general rotation,
    autohome, and resetting the origin.

    Authors:    Jake Fulton, jake.fulton@sjsu.edu 
                Christian pedrigal, christian.pedrigal@sjsu.edu
"""
"""
     Version:    2
    Date: 02/24/2022
    Comments:
"""
from sklearn.metrics import jaccard_score
from machine import Pin
import time

# Global Constants
phase_num = 0
delay = 37.75 # ms 

# Initializations
PinA = Pin(14, Pin.OUT)
PinB = Pin(12, Pin.OUT)
PinC = Pin(13, Pin.OUT)
PinD = Pin(15, Pin.OUT)
PinLS = Pin(0, Pin.IN, Pin.PULL_UP)
pins_motor = [PinA, PinB, PinC, PinD]


PHASES = (
    (True, True, False,  False ),
    (False, True,  True,  False),
    (False,  False,  True, True),
    (True,  False, False, True ))
num_phases = len(PHASES)


origin = 0

# User Defined Functions
def rotate(i: int, j: int) -> None:   #i = steps of 1.8 deg, j = 1 --> cw, j = -1 --> ccw
    global PHASES, pins_motor, num_phases, phase_num, delay, origin
    old_time = time.time_ns()
    counter = 0
    while counter < i:
        if time.time_ns() - old_time > delay*100000:
            phase_num = phase_num % num_phases
            phase_values = PHASES[phase_num]
            for pin in range(len(pins_motor)):
                pins_motor[pin].value(phase_values[pin])
            phase_num += j
            old_time = time.time_ns()
            counter = counter + 1
            origin = origin + i*j*1.8 # Update origin in degrees



def reset_origin(pin: Pin) -> None:
        global origin
        origin = 0

def autohome() -> None:
    global origin
    while origin > 0:
        rotate(1, -1)
        origin -= 1

# Synthetic Code
def _autohome(pin: Pin) -> None:
        global origin
        while origin > 0:
            # rotate(1, -1)
            origin -= 1
            print(origin)
            time.sleep(delay)
        
def _rotate(i, j):
    global origin
    origin += i*j*1.8 # Update origin in degrees


# Interrupts
PinLS.irq(trigger = Pin.IRQ_RISING, handler = reset_origin)
