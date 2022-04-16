from time import sleep
from math import floor
from machine import Pin, PWM, I2C

from ina219 import INA219
import vl6180


# Global Constants
DEBUG = True
MIN_DISTANCE = 10
DELAY = 0.050
MAX_DUTY = 1023
INIT_ANGLE = 90


# Pins
SERVO_PIN = 4 # Init at Pin 4 (D2)
LIMIT_PIN = 5 # Init at Pin 2 (D1)
SCL_CURR  = 0 # Init at Pin 0 (D3)
SDA_CURR  = 2 # Init at Pin 2 (D4)
SCL_DIST  = 14 # Init at Pin 14 (D5)
SDA_DIST  = 12 # Init at Pin 12 (D6)


# Init Hardware
# Servo Motor
servo = PWM(Pin(SERVO_PIN), freq = 50, duty = INIT_ANGLE) # Init at 50 Hz and 90 degrees

# VL6180 (Time-of-Flight Distance Sensor)
i2c = I2C(scl = Pin(SCL_DIST), sda = Pin(SDA_DIST)) 
dist_reader = vl6180.Sensor(i2c)

# INA219 (Current Sensor)
curr_reader = INA219(sda = SDA_CURR, scl = SCL_CURR)

# User Defined Functions
def _calculate_pulse_width(angle):
    # Calculates the pulse width in bits from a given angle
    K = (2 - 1)/(180 - 0)  # Mapping between 0 to 180 deg with 1 to 2 ms
    pulse_width = (1 + K*float(angle))*10**(-3);
    
    duty_cycle_value = (pulse_width*FREQ)*MAX_DUTY
    return round(duty_cycle_value)

def angle(servo, angle):
    # Turns servo motor to a specified angle
    duty_value = _calculate_pulse_width(angle)
    if DEBUG: print('Equivalent duty cycle value: {}'.format(duty_value))
    servo.duty(duty_value)
    sleep(DELAY)
    return int(angle)
    
def close(servo):
    # Closes servo motor by turning to 180 degrees
    servo.duty(90) # 102 pulse width is 180 degrees
    sleep(DELAY)

def open(servo):
    # Opens servo motor by turning to 0 degrees
    servo.duty(51) # 51 pulse width is 0 degrees
    sleep(DELAY)


# Main Programs
""" DOESN'T WORK
def main():
    # Measures distance from ultrasonic sensor
    distance = sensor.distance_cm()
    print("Distance: ", distance, "cm")

    # If the reported distance is less than the minimum distance
    if distance <= min_distance:
        # The servo motor turns to 180 degrees
        close(servo)
        print("Closing Tool since below", MIN_DISTANCE, "cm!")

    else: open(servo)
"""

def main2():
    while True:
        x = int(input("Type an angle between 0 and 180: "))
        angle(servo, x)
        sleep(1)


def main3():
    while True:
        open(servo)
        sleep(1)
        close(servo)
        sleep(2)

# Main Loop
if __name__ == '__main__':
    main3()