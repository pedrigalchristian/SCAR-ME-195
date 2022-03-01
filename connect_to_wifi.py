"""This is a subprogram that connects to your current Wifi network. 
Runs only once on main.py"""

# Built-in Libraries
import time
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

# User-Defined Libraries
from passwords import ssid, password, mqtt_server, mcu_sub
import flash_led

print(__name__, "working...")

# Global Constants
MCU_NUM = 1

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = mcu_sub[MCU_NUM].encode()
last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF) # Set the MCU as a wifi station
station.active(True)
station.connect(ssid, password)


# Main Program
while station.isconnected() == False:
  print('Connecting to', ssid, '...')
  time.sleep(5)

print('Connection successful')
print(station.ifconfig())