from machine import Pin
import flash_led

btn = Pin(10, Pin.IN)

if __name__ == "__main__":
    while True:
        print(btn.value())
