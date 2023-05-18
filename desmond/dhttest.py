import RPi.GPIO as GPIO
import dht11python as dht11
import time
import os
import sys
import time
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

rvr = SpheroRvrObserver()
# read data using pin 14
def main():
    rvr.wake()
    
    # Give RVR time to wake up
    time.sleep(2)
    
    rvr.reset_yaw()
    while True:
        instance = dht11.DHT11(pin = 7)
        result = instance.read()

        if result.is_valid():
           print("Temperature: %-3.1f C" % result.temperature)
           print("Humidity: %-3.1f %%" % result.humidity)
    #    else:
    #        print("Error: %d" % result.error_code)
        if result.temperature <= 22.0:
            rvr.drive_with_heading(
                speed=10, # Valid speed values are 0-255
                heading=0, # Valid heading values are 0-359
                flags=DriveFlagsBitmask.none.value
            )
        else :
             rvr.drive_with_heading(
                speed=10, # Valid speed values are 0-255
                heading=0, # Valid heading values are 0-359
                flags=DriveFlagsBitmask.drive_reverse.value
            )

            
        time.sleep(2)
         
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('program ended by Keyboard interrupt')
        rvr.close()
        GPIO.cleanup()
