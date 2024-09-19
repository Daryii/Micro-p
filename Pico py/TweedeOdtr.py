from machine import Pin
import time

LED1_PIN = 0
LED2_PIN = 5
BUTTON_PIN = 27
BUTTON_PIN2 = 21


led1 = Pin(LED1_PIN, Pin.OUT)
led2 = Pin(LED2_PIN, Pin.OUT)

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(BUTTON_PIN2, Pin.IN, Pin.PULL_DOWN)


led_state = False


def toggle_leds():
    global led_state
    led_state = not led_state
    if led_state:
        led1.on()
        led2.on()
    else:
        led1.off()
        led2.off()


previous_button2_state = False

while True:

    if button.value():
        led1.on()
        led2.on()
    else:
        led1.off()
        led2.off()


    current_button2_state = button2.value()


    if current_button2_state and not previous_button2_state:
        toggle_leds()


    previous_button2_state = current_button2_state


    time.sleep(0.05)