# 11_02_fancy_clock_class.py
import time
from datetime import datetime
from oled_io import Oled_io
import gpiozero

display = Oled_io()

switch = gpiozero.Button(23, pull_up=True)
time_mode, seconds_mode, date_mode = range(3)
disp_mode = time_mode
show_colon = True

def display_time():
    global show_colon
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    display.print(current_time)
    if show_colon:
        display.colon = True
        show_colon = False
    else:
        display.colon = False
        show_colon = True
    time.sleep(0.5)

def display_seconds():
    now = datetime.now()
    current_seconds = now.strftime("  %S")
    display.print(current_seconds)
    time.sleep(0.5)

def display_date():
    now = datetime.now()
    current_date = now.strftime("%m%d")
    display.print(current_date)
    time.sleep(0.5)

while True:
    if switch.is_pressed:
        disp_mode = disp_mode + 1
        if disp_mode > date_mode:
            disp_mode = time_mode
    if disp_mode == time_mode:
        display_time()
    elif disp_mode == seconds_mode:
        display_seconds()
    elif disp_mode == date_mode:
        display_date()