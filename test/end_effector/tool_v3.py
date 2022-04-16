import time
from math import floor
from machine import Pin, PWM, I2C

from ina219 import INA219
# import vl6180


# Global Constants
DEBUG: bool      = True
MIN_DIST: int    = 10
DELAY: float     = 0.050
MAX_DUTY: int    = 1023
INIT_ANGLE: int  = 90


# Pins
SERVO_PIN = 4  # Init at Pin 4 (D2)
LIMIT_PIN = 5  # Init at Pin 2 (D1)
SCL_CURR  = 0  # Init at Pin 0 (D3)
SDA_CURR  = 2  # Init at Pin 2 (D4)
SCL_DIST  = 14 # Init at Pin 14 (D5)
SDA_DIST  = 12 # Init at Pin 12 (D6)


# Init Hardware
# Servo Motor
servo = PWM(Pin(SERVO_PIN), freq = 50, duty = INIT_ANGLE) # Init at 50 Hz and 90 degrees
# VL6180 (Time-of-Flight Distance Sensor)
i2c = I2C(scl = Pin(SCL_DIST), sda = Pin(SDA_DIST)) 
#dist_reader = vl6180.Sensor(i2c)
# INA219 (Current Sensor)
curr_reader = INA219(_sda = SDA_CURR, _scl = SCL_CURR)
# Limit Switch
limit_switch = Pin(LIMIT_PIN, Pin.IN, Pin.PULL_UP) # Default HIGH


# Initializations
angle: int = 0

# User Defined Functions
def close(servo: PWM) -> None:
    """ Fingers of end effector will approach each other until the current
        sensor receives a spike in current. This is when the fingers
        touch each other.
        
        Note: This is a blocking function.
        
        Parameters:
        servo: PWM object of microservo.
    """
    


def open(servo: PWM) -> None:
    """ Fingers of end effectors will depart from each other until the
        limit switch is triggered. This is when the fingers reach the wall.
        
        Note: This is a blocking function.
        
        Parameters:
        servo: PWM object of microservo.
    """
    while limit_switch.value():
        angle -= 1
        servo.duty(angle)
        time.sleep(DELAY)

# Main Programs
def main_user_command_to_open() -> None:
    """ This main program opens and closes by user control. The servo wil
        stop actuating from the limit and current sensors.
    """
    while True:
        ans = input("Press 'x' to open, and 'z' to close")
        if ans == 'x': open(servo)
        elif ans == 'z': close(servo) 
        else: print("Pressed a wrong key. Try again.")

def main_debug_curr_reader():
    while True:
        print(curr_reader.readI())
        time.sleep(DELAY)

def main_debug_limit_switch():
    while True:
        while limit_switch.value():
            print("HIGH")
        print("LOW")
        
# Main Loop
if __name__ == '__main__':
    main_debug_limit_switch()