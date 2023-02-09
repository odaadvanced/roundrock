from gpiozero import RGBLED
from guizero import App, Slider, Text
from colorzero import Color
rgb_led = RGBLED (18, 23, 24)
red = 0
green = 0
blue = 0
def red_changed (value) :
    global red
    red = int (value)
    rgb_led.color = Color(red, green, blue)