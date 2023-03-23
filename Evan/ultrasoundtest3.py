import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import RPi.GPIO as GPIO
import asyncio
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
import time
from gpiozero import DigitalOutputDevice
from PiAnalog import *

GPIO.setwarnings(False)

loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)
GPIO.setmode(GPIO.BCM)

right_trigger = 20
right_echo = 21
left_trigger = 23
left_echo = 24
buzz1 = DigitalOutputDevice(5)
buzz2 = DigitalOutputDevice(6)
p = PiAnalog()

GPIO.setup(left_trigger, GPIO.OUT)
GPIO.setup(left_echo, GPIO.IN)
GPIO.setup(right_trigger, GPIO.OUT)
GPIO.setup(right_echo, GPIO.IN)

def distance_left():
    GPIO.output(left_trigger, True)
    
    time.sleep(0.00001)
    GPIO.output(left_trigger, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    while GPIO.input(left_echo) == 0:
        start_time = time.time()
        
    while GPIO.input(left_echo) == 1:
        stop_time = time.time()
        
    time_elapsed = stop_time - start_time
    
    distance = (time_elapsed * 34300) / 2
    return distance


def distance_right():
    GPIO.output(right_trigger, True)
    
    time.sleep(0.00001)
    GPIO.output(right_trigger, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    while GPIO.input(right_echo) == 0:
        start = time.time()
        
    while GPIO.input(right_echo) == 1:
        stop_time = time.time()
        
    time_elapsed = stop_time - start_time
    
    distance = (time_elapsed * 34300) / 2
    return distance


def buzz(pitch, duration):
    period = 1.0 / pitch
    p2 = period / 2
    cycles = int(duration * pitch)
    print (cycles)
    for i in range(0, cycles):
        print ("i = " + str(i))
        buzz1.on()
        buzz2.off()
        delay(p2)
        buzz1.off()
        buzz2.on()
        delay(p2)
        
        
def delay(p):
    t0 = time.time()
    while time.time() < t0 + p:
        pass
    


async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(5)
    while True:
        dist_r = distance_right()
        dist_l = distance_left()
        await asyncio.sleep(.05)
        print('Measurements are {0} cm right and {1} cm left'.format(dist_r, dist_l))
        if dist_r < 35:
            while  dist_r < 35:
                await rvr.raw_motors(2,255,1,255)
                dist_r = distance_right()
                await asyncio.sleep(.05)
                buzz(2000, 0.5)
                print('turning right')
            await rvr.reset_yaw()
        elif dist_l < 35:
            while dist_l < 35:
                await rvr.raw_motors(1,255,2,255)
                dist_l = distance_left()
                await asyncio.sleep(.05)
                buzz(2000, 0.5)
                print('turning left')
            await rvr.reset_yaw()
        elif dist_l >= 35 and dist_r >= 35:
            await rvr.drive_with_heading(90,0,0)
            
            
try:
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )
except KeyboardInterrupt:
    print('Program ended by KeyboardInterrupt')
    GPIO.cleanup()