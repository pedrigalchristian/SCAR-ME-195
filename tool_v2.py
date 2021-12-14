from time import sleep
from math import floor
from machine import Pin, PWM
import hcsr04

# Params
MIN_DISTANCE = 10
DELAY = 0.005

# Init Hardware
sensor = hcsr04.HCSR04(12,14) # GPIO Pins 12 and 14 for Ultrasonic Sensor
servo = PWM(Pin(4), freq = 50, duty = 51) # Initialize at Pin 4 at 50 Hz and 0 degrees

def _calculate_pulse_width(angle):
    # Calculates the pulse width in bits from a given angle
    K = (2.48 - 1)/(180 - 0)  # Mapping between 0 to 180 deg with 1 to 2 ms
    pulse_width = (1 + K*float(angle))*10**(-3);

    MAX_DUTY = 1023
    FREQ = 50
    duty_cycle_value = (pulse_width*FREQ)*MAX_DUTY

    return round(duty_cycle_value)

# Functions
def angle(servo, angle):
    # Turns servo motor to a specified angle
    duty_value = _calculate_pulse_width(angle)

    servo.duty(duty_value)
    sleep(DELAY)

def close(servo):
    # Closes servo motor by turning to 180 degrees
    servo.duty(127) # 102 pulse width is 180 degrees
    sleep(DELAY)

def open(servo):
    # Opens servo motor by turning to 0 degrees
    servo.duty(51) # 51 pulse width is 0 degrees
    sleep(DELAY)

def main():
    # Measures distance from ultrasonic sensor
    distance = sensor.distance_cm()
    print("Distance: ", distance, "cm")

    # If the reported distance is less than the minimum distance
    if distance <= min_distance:
        # The servo motor turns to 180 degrees
        close(servo)
        print("Closing Tool since below", MIN_DISTANCE, "cm!")

    else: open(servo)

def main2():
    while True:
        x = input("Type an angle between 0 and 180: ")
        angle(servo, x)


# Main Loop
if __name__ == '__main__':
    main2()