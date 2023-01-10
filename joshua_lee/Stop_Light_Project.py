from gpiozero import TrafficLights
from time import sleep
from gpiozero import Button
from gpiozero import DigitalOutputDevice
import adafruit_ssd1306


lights = TrafficLights(22, 27, 17)

button = Button(5)

bz = DigitalOutputDevice(25)

bz.on()

lights.red.on()

while True:
    if button.is_pressed:
        sleep(15)
        while lights.red.on():
            bz.on(0.5)
            sleep(0.5)
            bz.toggle()
        lights.red.off()
        lights.green.on()
        print ("MAY CROSS")
        sleep(15)
        lights.amber.on()
        lights.green.off()
        print ("DO NOT CROSS")
        sleep(3)
        lights.green.off()
        lights.amber.off()
        lights.red.on()
    else:
        print("DO NOT CROSS")
        