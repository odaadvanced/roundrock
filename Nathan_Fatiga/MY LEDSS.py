import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups


rvr = SpheroRvrObserver()


def main():
    """ This program demonstrates how to set the all the LEDs.
    """

    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

        while True:
            rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [0, 0, 255]]
            )

            # Delay to show LEDs change
            time.sleep(0.125)

            rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [255, 255, 255]]
            )
            
            time.sleep(0.125)

            rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [0, 0, 255]]
            )
            
            time.sleep(0.125)

            rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [0, 0, 0]]
            )

            # Delay to show LEDs change
            time.sleep(0.125)
            
            rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [255, 0, 0]]
            )
            
            time.sleep(0.125)

            rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [255, 255, 255]]
            )

            # Delay to show LEDs change
            time.sleep(0.125)

            rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [255, 0, 0]]
            )

            # Delay to show LEDs change
            time.sleep(0.125)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()


if __name__ == '__main__':
    main()
