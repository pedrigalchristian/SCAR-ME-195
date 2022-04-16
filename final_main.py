"""
This program is the current final program that would be 
uploaded to ESP8266. This should be copy and pasted to 
main.py
"""

# Shows user that running boot.py
import test.blink as blink
from umqttsimple import MQTTClient
import src.connect_to_wifi as connect_to_wifi
from src.connect_to_wifi import (client_id, mqtt_server, topic_sub,
                             last_message, message_interval, counter)
import time
import test.stepper_motors.stepper_motor as stepper_motor
import src.flash_led as flash_led


"""Callback function: After 1 function is done, immediately another function is triggered to begin."""
def sub_cb(topic, msg):
    # Stands for "subscribed callback"
    print((topic, msg))
    
    (angle, direction) = tuple(map(int, msg.split(', ')))

    stepper_motor._rotate(angle, direction)
    
    print(stepper_motor.origin)



def connect_and_subscribe():
    print("Connecting to MQTT Broker...")
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server, port = 1883)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()

# Main Program
while True:
    try:
        client.check_msg()
        if (time.time() - last_message) > message_interval:
            print("testing..", __name__, counter)
            last_message = time.time()
            counter += 1
    except OSError as e:
        restart_and_reconnect()







