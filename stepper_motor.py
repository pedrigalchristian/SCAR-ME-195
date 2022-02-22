from machine import Pin
import time

PinA = Pin(14, Pin.OUT)
PinB = Pin(12, Pin.OUT)
PinC = Pin(13, Pin.OUT)
PinD = Pin(15, Pin.OUT)

PHASES = (
    (True, True, False,  False ),
    (False, True,  True,  False),
    (False,  False,  True, True),
    (True,  False, False, True ))

pins_motor=[PinA, PinB, PinC, PinD]

num_phases = len(PHASES)

phase_num = 0

delay = 37.75*100000


def rotate(i, j):   #i = steps of 1.8 deg, j = 1 --> cw, j = -1 --> ccw
    global PHASES, pins_motor, num_phases, phase_num, delay
    counter = 0
    old_time = time.time_ns()
    while counter < i:
        if time.time_ns() - old_time > delay:
            phase_num = phase_num % num_phases
            phase_values = PHASES[phase_num]
            for pin in range(len(pins_motor)):
                pins_motor[pin].value(phase_values[pin])
            phase_num += j
            old_time = time.time_ns()
            counter = counter + 1