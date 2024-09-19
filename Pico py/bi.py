from machine import Pin
from utime import sleep


green_led = Pin(0, Pin.OUT)  
red_led = Pin(9, Pin.OUT)    


button1 = Pin(18, Pin.IN, Pin.PULL_DOWN)  
button2 = Pin(20, Pin.IN, Pin.PULL_DOWN) 
button3 = Pin(26, Pin.IN, Pin.PULL_DOWN)  
button4 = Pin(22, Pin.IN, Pin.PULL_DOWN)  

vault_code = [1, 2, 3, 4]  
input_sequence = [] 


def flash_led(led, times, delay=0.3):
    for _ in range(times):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)


def check_vault_code():
    if input_sequence == vault_code:
        flash_led(green_led, 3)  
        print("Vault unlocked! Green LED is flashing.")
    else:
        flash_led(red_led, 3)  
        print("Incorrect code! Red LED is flashing.")
    sleep(2)
    input_sequence.clear()  

while True:
    if button1.value() == 1:
        input_sequence.append(1)
        print("Button 1 pressed.")
        sleep(0.5)  # Debounce delay
    elif button2.value() == 1:
        input_sequence.append(2)
        print("Button 2 pressed.")
        sleep(0.5)
    elif button3.value() == 1:
        input_sequence.append(3)
        print("Button 3 pressed.")
        sleep(0.5)
    elif button4.value() == 1:
        input_sequence.append(4)
        print("Button 4 pressed.")
        sleep(0.5)

 
    if len(input_sequence) == 4:
        check_vault_code()