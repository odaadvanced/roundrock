#09_04_switch.py

import gpiozero, time
led = gpiozero.LED(18)

switch = gpiozero.Button(23, pull_up=True)

while True:
    if switch.is_pressed:
        led.toggle()
        print("Button Pressed")
        time.sleep(0.2)