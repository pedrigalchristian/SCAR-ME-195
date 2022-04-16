from machine import Pin

PIN_LED = 16

led = Pin(PIN_LED, Pin.OUT)

led.value(False)
print("LED is ON!")