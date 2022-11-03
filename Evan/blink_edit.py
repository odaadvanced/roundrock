#09_01_blink.py

import gpiozero, time

led = gpiozero.LED(18)

while True:
    led.on()
    time.sleep(0.02)             # delay 0.5 seconds
    led.off()
    time.sleep(0.02)