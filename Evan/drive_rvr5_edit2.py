import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask

rvr = SpheroRvrObserver()
a = "10"

def main():
    """ This program had RVR drive around in different directions
using the function drive_with_heading."""
    try:
        rvr.wake()
    # give RVR time to wake up
    while True:
        time.sleep(2) #Delay to allow RVR to drive
        rvr.drive_with_heading(
            speed=0,
            heading=90,
            flags=DriveFlagsBitmask.drive_reverse.value
        )
        time.sleep(2)
        rvr.drive_with_heading(
            speed=0,
            heading=180,
            flags=DriveFlagsBitmask.drive_reverse.value
        )
        time.sleep(2)
        
        rvr.drive_with_heading(
            speed=0,
            heading=270,
            flags=DriveFlagsBitmask.drive_reverse.value
        )
        time.sleep(2)
        
        rvr.drive_with_heading(
            speed=0,
            heading=0,
            flags=DriveFlagsBitmask.drive_reverse.value
        )
        time.sleep(2)
    
    except KeyboardInterrupt:
        print("\nProgram terminated with keyboard interrupt.")
        
    finally:
        rvr.close()

if __name__== '__main__':
    main()