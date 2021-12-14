from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
led2 = Pin(16, Pin.OUT)

def run():
    while True:
        led.on()
        led2.value(not led.value())
        print(led.value())
        sleep(1)

        led.off()
        led2.value(not led.value())
        print(led.value())
        sleep(1)

if __name__ == "__main__":
    while True:
        run()
