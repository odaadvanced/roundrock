import os
import sys
import time
import RPi.GPIO as GPIO
import dht11python as dht11
import time
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

count = 0
rvr = SpheroRvrObserver()
rvr.wake()
time.sleep(2)
rvr.reset_yaw()

# read data using pin 14
def update_temp():
    global count
    instance = dht11.DHT11(pin = 4)
    result = instance.read()

    if result.is_valid():
        temperature = result.temperature;
        temperature = "%.2f" % temperature
        temp_textvalue = temperature
        count = count + 1
        print(f'temperature = {temperature}count = {count}')
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
        
    temp_text.after(1000, update_temp)
#    else:
#        print("Error: %d" % result.error_code)
        
 #   time.sleep(2)
 
 app = App(title = "Thermometer", width="400", height="300")
 Text(app, text="Temp F", size 32)
 temp_text = Text(app, text="0.00", size=110)
 temp_text.after(1, update_temp)
 
 app.display()