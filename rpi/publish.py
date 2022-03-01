from os import system
from time import sleep

import keyboard
from passwords import mcu_sub

# Global Constants
SCALE = 10
MCU_NUM = 1

# Initializations
angle = 0
last_angle = 0
rpi_topic = mcu_sub[MCU_NUM]

# Keyboard List for each MCU
increase_key = ['w', 'r', 'y', 'i', 'p']
decrease_key = ['q', 'e', 't', 'u', 'o']
try:
    len(increase_key) <= 5
except:
    raise Exception("Size too large than number of MCUs")

# User-Defined Functions
def publish(angle: int, direction: int) -> None:
    text = (f'mosquitto_pub -d -t {rpi_topic} -m "{angle, direction}"')
    # print(text)
    system(text);

"""
def decreaseAngle(angle):
    global SCALE
    angle = (angle - 1*SCALE);
    return angle

def increaseAngle(angle):
    global SCALE
    angle = (angle + 1*SCALE);
    return angle
"""

# If increase or decrease key is pressed, a message is sent from the RPi terminal
keyboard.add_hotkey(increase_key[MCU_NUM], publish(1*SCALE, 1))
keyboard.add_hotkey(decrease_key[MCU_NUM], publish(-1*SCALE, -1))

# Main Program
if __name__ == "__main__":
    keyboard.wait()





    


