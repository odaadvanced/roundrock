#!/usr/bin/env python3
import os
import sys
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
from oled_io import Oled_io
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
import random


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

rvr = SpheroRvrObserver()
display = Oled_io()
camera = PiCamera()
ObstaclePin = 5
dhtPin = 17

def destroy():
    camera.stop_preview()


GPIO.setmode(GPIO.BCM)

MAX_UNCHANGE_COUNT = 100

STATE_INIT_PULL_DOWN = 1
STATE_INIT_PULL_UP = 2
STATE_DATA_FIRST_PULL_DOWN = 3
STATE_DATA_PULL_UP = 4
STATE_DATA_PULL_DOWN = 5

def readDht11():
    GPIO.setup(dhtPin, GPIO.OUT)
    GPIO.output(dhtPin, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(dhtPin, GPIO.LOW)
    time.sleep(0.02)
    GPIO.setup(dhtPin, GPIO.IN, GPIO.PUD_UP)

    unchanged_count = 0
    last = -1
    data = []
    while True:
        current = GPIO.input(dhtPin)
        data.append(current)
        if last != current:
            unchanged_count = 0
            last = current
        else:
            unchanged_count += 1
            if unchanged_count > MAX_UNCHANGE_COUNT:
                break

    state = STATE_INIT_PULL_DOWN

    lengths = []
    current_length = 0

    for current in data:
        current_length += 1

        if state == STATE_INIT_PULL_DOWN:
            if current == GPIO.LOW:
                state = STATE_INIT_PULL_UP
            else:
                continue
        if state == STATE_INIT_PULL_UP:
            if current == GPIO.HIGH:
                state = STATE_DATA_FIRST_PULL_DOWN
            else:
                continue
        if state == STATE_DATA_FIRST_PULL_DOWN:
            if current == GPIO.LOW:
                state = STATE_DATA_PULL_UP
            else:
                continue
        if state == STATE_DATA_PULL_UP:
            if current == GPIO.HIGH:
                current_length = 0
                state = STATE_DATA_PULL_DOWN
            else:
                continue
        if state == STATE_DATA_PULL_DOWN:
            if current == GPIO.LOW:
                lengths.append(current_length)
                state = STATE_DATA_PULL_UP
            else:
                continue
            
    if len(lengths) != 40:
        #print ("Data not good, skip")
        return False

    shortest_pull_up = min(lengths)
    longest_pull_up = max(lengths)
    halfway = (longest_pull_up + shortest_pull_up) / 2
    bits = []
    the_bytes = []
    byte = 0

    for length in lengths:
        bit = 0
        if length > halfway:
            bit = 1
        bits.append(bit)
    #print ("bits: %s, length: %d" % (bits, len(bits)))
    for i in range(0, len(bits)):
        byte = byte << 1
        if (bits[i]):
            byte = byte | 1
        else:
            byte = byte | 0
        if ((i + 1) % 8 == 0):
            the_bytes.append(byte)
            byte = 0
    #print (the_bytes)
    checksum = (the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3]) & 0xFF
    if the_bytes[4] != checksum:
        #print ("Data not good, skip")
        return False

    return the_bytes[0], the_bytes[2]

def main():

    while True:
        result = readDht11()
        if result:
            humidity, temperature = result
            print ("humidity: %s %%,  Temperature: %s ℃" % (humidity, temperature))
        time.sleep(1)

        
def setup():
   
   global direction
   direction = 0
   
   rvr.wake()
   
   time.sleep(2)

   rvr.reset_yaw()
  
   GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
   GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   camera.start_preview(alpha=200)

   camera.capture('/home/pi/my_photo.jpg')

def loop():
   global direction
   while True:
      result = readDht11()
      if result:
            humidity, temperature = result
            print ("humidity: %s %%,  Temperature: %s ℃" % (humidity, temperature))
            if temperature > 23:
                display.print(str("Done!"))
                destroy()
            if humidity > 70:
                display.print(str("Done!"))
                destroy()


      if (0 == GPIO.input(ObstaclePin)):
         
             
         display.print(str("Danger!"))
         direction = direction + 90
         if direction >= 359:
             direction = 0
         
         rvr.drive_with_heading(
            speed=10,  # Valid speed values are 0-255
            heading =direction,  # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )   
         
      else:
          display.print(str(" "))
         
          rvr.drive_with_heading(
            speed=25,  # Valid speed values are 0-255
            heading=direction,  # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
          )   
         
      time.sleep(1)


def destroy():
   GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
   setup()
   try:
      loop()
   except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
      destroy()
