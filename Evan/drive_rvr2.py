import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask

rvr = SpheroRvrObserver()

def main():
    """ This program had RVR drive around in different directions
using the function drive_with_heading."""
    try:
        rvr.wake()
    # give RVR time to wake up
        time.sleep(10)
    except KeyboardInterrupt:
        print("\nProgram terminated with keyboard interrupt.")
        
    finally:
        rvr.close()

if __name__== '__main__':
    main()