#09_01_blink.py

import gpiozero, time

led = gpiozero.LED(26)
led.off()

dot = .5
dash = 3 * dot
space = dot
letter_space = 3*dot
word_space = 7 * dot

letters = {
    "a": [dot,dash],
    "b": [dash,dot,dot,dot]
    }

def show_led (blinks) :
    for blink in blinks:
        if blink == dash:
            led.on()
        if blink == dot:
            led.on()
        time.sleep(blink)
        led.off()
        time.sleep(dot)
        
try:
    while True:
        b = letters['b']
        show_led(b)
        
except KeyboardInterrupt:
    led.off()
    print ('Bye')
    
