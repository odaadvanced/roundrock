# 11_02_fancy_clock.py
from oled_io import Oled_io
import time, gpiozero
from gpiozero import LED, DigitalOutputDevice
from PiAnalog import *
display = Oled_io()
switch = gpiozero.Button(19, pull_up=True)
show_colon = True
no_cross, countdown_mode, date_mode, slow_mode, sleeper = range(5)
disp_mode = no_cross

red2 = LED(25)
green2 = LED(23)
yellow2 = LED(24)
red_led = LED(22)
yellow_led = LED(20)
green_led = LED(17)

R = LED(26)
G = LED(12)
Y = LED(13)
pin1 = DigitalOutputDevice(5)
pin2 = DigitalOutputDevice(6)
p = PiAnalog()

slowv = True

canpress = True

def buzz(pitch, duration):
    period = 1.0 / pitch
    p2 = period / 2
    cycles = int(duration * pitch)
    for i in range(0, cycles):
        pin1.on()
        pin2.off()
        delay(p2)
        pin1.off()
        pin2.on()
        delay(p2)

def delay(xp):
    t0 = time.time()
    while time.time() < t0 + xp:
        pass

def display_cross_f():
    yellow2.off()
    red_led.off()
    R.on()
    green_led.on()
    mes = "DO NOT CROSS"
    red2.on()
    canpress = True
    display.print(mes)

def countdown():
    global disp_mode
    canpress = False
    tm = 15
    while tm >= 1:
        display.print(str(tm))
        buzz(350, 0.3)
        tm = tm - 1
        display.print("DO NOT CROSS")
        time.sleep(0.6)
        if tm == 0:
            break
        elif tm == 5:
            green_led.off()
            yellow_led.on()
        elif tm == 2:
            yellow_led.off()
            red_led.on()
    canpress = True
    disp_mode = disp_mode + 1

def countdown2():
    global disp_mode
    canpress = False
    ot = 10
    R.off()
    G.on()
    while ot >= 0:
        display.print(str(ot))
        buzz(350, 0.3)
        ot = ot - 1
        display.print("DO NOT CROSS")
        time.sleep(0.6)
        if ot == 0:
            break
        elif ot == 5:
            G.off()
            Y.on()
        elif ot == 2:
            Y.off()
            R.on()
    ti = 15
    while ti > 0:
        display.print(str(ti))
        buzz(450, 0.3)
        ti = ti - 1
        display.print("May Cross")
        time.sleep(0.6)
        if ti == 0:
            break
        elif ti == 5:
            green2.off()
            yellow2.on()
        elif ti == 2:
            yellow2.off()
            red2.on()
    disp_mode = disp_mode + 1
        
        
def display_cross():
    red2.off()
    green2.on()
    mes2 = "May Cross"
    display.print(mes2)
    time.sleep(1)
    disp_mode = 5
    countdown2()

def display_slow():
    green2.off()
    yellow2.on()
    mes3 = "DO NOT CROSS"
    display.print(mes3)
    time.sleep(3)
    display_cross_f()
    disp_mode = no_cross

while True:
    if switch.is_pressed:
        if canpress == True:
            disp_mode = 1
            
    if disp_mode == no_cross:
        display_cross_f()
    elif disp_mode == countdown_mode:
        countdown()
    elif disp_mode == date_mode:
        display_cross()
    elif disp_mode == slow_mode:
        display_slow()
        disp_mode = 5
    elif disp_mode == sleeper:
        a = 1