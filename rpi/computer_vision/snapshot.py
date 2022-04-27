#! /usr/bin/python3

from picamera import PiCamera
from time import sleep
import os


# Global Variables


# Create Camera Object
camera = PiCamera()
# camera.awb_mode = 'greyworld'


# Create Directory for Dumping Pics
curr_path = os.getcwd()
dir_name = "Pics_and_Vids"
full_path = os.path.join(curr_path, dir_name)
print(full_path)

if not os.path.exists(full_path):
	os.mkdir(full_path)
	print(full_path, " folder created!")
os.chdir(full_path)
print(f"Changed path to {full_path}")


# Start Camera Capture
x = str(input('What is the name of this pic? ')) + '.jpg'
camera.capture(x)
print('Picture snapped!')

