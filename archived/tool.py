from machine import Pin, PWM
from time import sleep
import hcsr04

# Init Hardware
sensor = hcsr04.HCSR04(12,14) # GPIO Pins 12 and 14 for Ultrasonic Sensor
servo = PWM(Pin(4), freq = 50, duty = 51) # Initialize at Pin 4 at 50 Hz and 0 degrees


# Functions
def close(servo):
    # Closes servo motor by turning to 180 degrees
    servo.duty(102) # 180 degrees
    sleep(1)

def open(servo):
    # Opens servo motor by turning to 0 degrees
    servo.duty(51) # 0 degrees
    sleep(1)

def main():
    # Measures distance from ultrasonic sensor
    distance = sensor.distance_cm()
    print("Distance: ", distance, "cm")

    # If the reported distance is less than the minimum distance
    if distance <= min_distance:

        # The servo motor turns to 180 degrees
        close(servo)
        print("Closing Tool since below", min_distance, "cm!")

    else: open(servo) 

# Params
min_distance = 10

# Main Loop
while True:
  main()
end
