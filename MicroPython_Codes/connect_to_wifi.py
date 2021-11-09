"""This is a subprogram that connects to your current Wifi network. 
Runs only once on main.py"""

import time
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

print(__name__, "working...")

ssid = 'Christian Pedrigal'
password = 'craftmine'
mqtt_server = '172.20.10.9' # Raspberry Pi Static IP Address
"""
ssid = 'SJSU_premier'
password = 'Rubb3rsoul!'
"""
"""
ssid = 'apnet-xfin2.4'
# ssid = 'apnet-deco' # Wifi Name
password = '!Marinduqu321' # Wifi Password """

# mqtt_server = '192.168.68.59' # Raspberry Pi Static IP Address
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'testTopic'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  print('Connecting to', ssid, '...')
  time.sleep(5)

print('Connection successful')
print(station.ifconfig())