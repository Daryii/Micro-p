from machine import Pin
from utime import sleep

led = Pin(2, Pin.OUT)

while True:
    led.toggle()
    sleep(1)