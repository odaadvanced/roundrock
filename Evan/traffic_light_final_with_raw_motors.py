#this is an incomplete program and it will not drive the rover,
#it will only do what the original traffic light final program does


import sys
import os
import time
import gpiozero
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RawMotorModesEnum
from gpiozero import LED
from gpiozero import DigitalOutputDevice
from time import sleep
from oled_io import Oled_io

rvr = SpheroRvrObserver()
crossbutton = gpiozero.Button(19, pull_up=True)
green = LED(21)
amber = LED(26)
red = LED(17)
buzz1 = DigitalOutputDevice(20)
buzz2 = DigitalOutputDevice(16)
display = Oled_io()

def buzz(pitch, duration):
    period = 1.0 / pitch
    p2 = period / 2
    cycles = int(duration * pitch)
    for i in range(0, cycles):
        buzz1.on()
        buzz2.off()
        delay(p2)
        buzz1.off()
        buzz2.on()
        delay(p2)
        
def delay(p):
    t0 = time.time()
    while time.time() < t0 +p:
        pass

green.off()
amber.off()
red.on()

while True:
    if crossbutton.is_pressed:
        timer = 15
        while timer > 0:
            display.print(str(timer))
            timer = timer - 1
            buzz(1000, 0.5)
            sleep(0.5)
        timer = 15
        amber.on()
        red.off()
        sleep(3)
        amber.off()
        green.on()
        while timer > 0:
            display.print(str(timer))
            timer = timer - 1
            buzz(2000, 0.5)
            sleep(0.5)
        green.off()
        amber.on()
        sleep(3)
        amber.off()
        red.on()