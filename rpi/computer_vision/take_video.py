#! /usr/bin/python3

from picamera import PiCamera
from time import sleep
import os


# Global Variables
VID_LENGTH = 10

# Create Camera Object
camera = PiCamera()


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


# Start Camera Video/Picture
x = str(input('What is the name of this video? ')) + '.h264'
camera.start_recording(x)
print('Started recording!')
sleep(VID_LENGTH)
camera.stop_recording()
print('Ended recording!')
