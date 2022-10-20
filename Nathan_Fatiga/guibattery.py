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
    
def battery_voltage_handler(battery_voltage_state):
    global voltage_state
    voltage_state = battery_voltage_state
    global state_info
    state_info = '[{}, {}, {}, {}]'.format(
    '{}: {}'.format(VoltageStates.unknown.name, VoltageStates.unknown.value),
    '{}: {}'.format(VoltageStates.ok.name, VoltageStates.ok.value),
    '{}: {}'.format(VoltageStates.low.name, VoltageStates.low.value),
    '{}: {}'.format(VoltageStates.critical.name, VoltageStates.critical.value)
    )
    global voltage_states
    voltage_states = 'Voltage: ' + state_info

def main():
    """ This program demonstrates how to retrive the battery state of RVR """
    try:
        rvr.wake()
        time.sleep(2)
        rvr.get_battery_percentage(handler=battery_percentage_handler)
        time.sleep(1)
        rvr.get_battery_voltage_state(handler=battery_voltage_handler)
        time.sleep(1)
        Text(app, text="Battery Percentage " + str(battery_percentage_out['percentage']))
        Text(app, text="Voltage State " + str(voltage_state['state']))
        Text(app, text=voltage_states)
        app.display()
    except KeyboardInterrupt:
        print("NO")
    finally:
        rvr.close()
        
if __name__ == '__main__':
    main()