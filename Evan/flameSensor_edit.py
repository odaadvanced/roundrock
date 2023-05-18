#!/usr/bin/env python
import RPi.GPIO as GPIO
import ADC0832_edit
import time

Flame_DO_Pin = 5
LedPin = 21
thresholdVal = 150

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Flame_DO_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LedPin, GPIO.OUT)
    ADC0832_edit.setup()

def loop():	
    while True:
        global digitalVal, analogVal
        analogVal = ADC0832_edit.getResult(0)
        print ('Current analog value is %d'% analogVal) 
        GPIO.output(LedPin, GPIO.input(Flame_DO_Pin))
        time.sleep(0.2)
		
if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832_edit.destroy()
		print ('The end !')
