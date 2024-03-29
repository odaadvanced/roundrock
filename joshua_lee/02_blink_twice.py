# 02_blink_twice.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from gpiozero import LED
import time
from signal import pause

red_led1 = LED(17)
red_led2 = LED(22)

# The first number in blink() is the on time and the second is the off time (both in seconds)
red_led1.blink(1.0, 1.0)
time.sleep(0.5)
red_led2.blink(1.0, 1.0)

pause()

'''
The pause() is needed at the end to keep the program running.
If you remove it, the program will stop immediately and the LED's will stop blinking.
Use CTRL-c to stop the program running.
'''
