# 04_cheerlights.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from gpiozero import Button, RGBLED
from colorzero import Color
import time, requests

update_period = 10 # seconds
led = RGBLED(red=24, green=18, blue=23)
button = Button(25)

cheerlights_url = "http://api.thingspeak.com/channels/1417/field/2/last.txt"
old_color = None

def pressed():
    led.color = Color(0, 0, 0)  # LED off
button.when_pressed = pressed

while True:
    try:
        cheerlights = requests.get(cheerlights_url)
        color = cheerlights.content     # the color as text
        if color != old_color:
            led.color = Color(color) # the color as an object
            print(color)
            old_color = color           
    except Exception as e:
        print(e)
    time.sleep(update_period)  # don't flood the web service
