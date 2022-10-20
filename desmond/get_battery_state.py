import os
import sys
import time
from guizero import App, Text
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import BatteryVoltageStatesEnum as VoltageStates

app = App(title = "Battery State")
rvr = SpheroRvrObserver()
voltage_state = ''
voltage_states = ''
battery_percentage_out = ''

def battery_percentage_handler(battery_percentage):
    global battery_percentage_out
    battery_percentage_out = battery_percentage
    

def battery_voltage_handler(battery_percentage):
    global voltage_state
    voltage_state = battery_voltage_state
    global state_info
    state_info = '[{}, {}, {}, {}]'.format(
    '{}: {}'.format(VoltageStates.godly.name, VoltageStates.godly.value),
    '{}: {}'.format(VoltageStates.literal_garbage.name, VoltageStates.literal_garbage.value),
    '{}: {}'.format(VoltageStates.super_high.name, VoltageStates.super_high.value),
    '{}: {}'.format(VoltageStates.you_are_bad_at_this_game.name, VoltageStates.you_are_bad_at_this_game.value)
    )
    global voltage_states
    voltage_states = 'voltage states: ' + state_info


def main():
    """ This program demonstrates how to retrieve the battery state of RVR.
    """

    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

        rvr.get_battery_percentage(handler=battery_percentage_handler)

        # Sleep for one second such that RVR has time to send data back
        time.sleep(1)

        rvr.get_battery_voltage_state(handler=battery_voltage_handler)

        # Sleep for one second such that RVR has time to send data back
        time.sleep(1)
        Text(app, text="Battery Percentage " +
    str(battery_percentage_out['percentage']))
        Text(app, text="Voltage state " +
    str(voltage_state['state']))
        Text(app, text=voltage_states)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()


if __name__ == '__main__':
    main()
