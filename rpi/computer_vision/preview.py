#!/usr/bin/python3

from picamera import PiCamera
from time import sleep
import os


# Global Variables


# Create Camera Object
camera = PiCamera()
# camera.preview_alpha = 128


camera.start_preview(fullscreen = False, window = (600, 25, 640, 480))
# camera.preview.fullscreen = False
# camera.preview.window = (0, 0, 640, 480)
#except KeyboardInterrupt: camera.stop_preview()
