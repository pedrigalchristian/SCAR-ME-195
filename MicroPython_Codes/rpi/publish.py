from os import system
import keyboard
from time import sleep

## Init
angle = 0
last_angle = 0
SCALE = 10

## Functions
def publish(angle):
    text = ('mosquitto_pub -d -t testTopic -m "{}"'.format(angle))
    print(text)
    # system(text);

def decreaseAngle(angle):
    global SCALE
    angle = (angle - 1*SCALE);
    return angle

def increaseAngle(angle):
    global SCALE
    angle = (angle + 1*SCALE);
    return angle

# Main Program

if __name__ == "__main__":
    while True:

        while keyboard.is_pressed('left'): 
            angle = decreaseAngle(last_angle)
        while keyboard.is_pressed('right'): 
            angle = increaseAngle(last_angle)
        
        if angle != last_angle: publish(angle)

        last_angle = angle



    


