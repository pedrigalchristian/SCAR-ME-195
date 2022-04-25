#!/bin/bash
#date: 04/20/2022
#author: pedrigalchristian@gmail.com

#go to convert-model dir from SCAR-ME-195
cd /home/pi/convert-model
source bin/activate


# Go to tensor-flow-lite dir
cd /home/pi/Desktop/SCAR-ME-195/rpi/machine_learning/rasppi-tensorflow-yolov4-tflite
python detect.py --weights ./checkpoints/anpr-416.tflite --size 416 --model yolov4 --image /home/pi/Desktop/SCAR-ME-195/images/scissors.jpg --framework tflite	




 

