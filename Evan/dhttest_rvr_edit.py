import os
import sys
import time
import RPi.GPIO as GPIO
import dht11python as dht11
import time
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask

rvr = SpheroRvrObserver()

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14

def main():
    
    # Give RVR time to wake up
    time.sleep(2)
    
    rvr.reset_yaw()

    while True:
        instance = dht11.DHT11(pin = 4)
        result = instance.read()

        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
#    else:
#        print("Error: %d" % result.error_code)
        
        if result.temperature <= 21.8:
            rvr.drive_with_heading(
                speed=50,
                heading=0,
                flags=DriveFlagsBitmask.none.value
            )
        else :
            rvr.drive_with_heading(
                speed=50,
                heading=0,
                flags=DriveFlagsBitmask.drive_reverse.value
            )
        
        time.sleep(2)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program ended by KeyboardInterrupt')
        rvr.close()
        GPIO.cleanup()