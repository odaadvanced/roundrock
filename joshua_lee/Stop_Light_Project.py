from gpiozero import TrafficLights, Button, DigitalOutputDevice
from time import sleep
from oled_io import Oled_io

display = Oled_io()

lights = TrafficLights(22, 27, 17)

button = Button(5)

bz = DigitalOutputDevice(26)

bz.on()
bz.off()

lights.red.on()

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

while True:
    if button.is_pressed:
        display.print("15")
        bz.on()
        bz.off()
        sleep(1)
        display.print("14")
        bz.on()
        bz.off()
        sleep(1)
        display.print("13")
        bz.on()
        bz.off()
        sleep(1)
        display.print("12")
        bz.on()
        bz.off()
        sleep(1)
        display.print("11")
        bz.on()
        bz.off()
        sleep(1)
        display.print("10")
        bz.on()
        bz.off()
        sleep(1)
        display.print("9")
        bz.on()
        bz.off()
        sleep(1)
        display.print("8")
        bz.on()
        bz.off()
        sleep(1)
        display.print("7")
        bz.on()
        bz.off()
        sleep(1)
        display.print("6")
        bz.on()
        bz.off()
        sleep(1)
        display.print("5")
        bz.on()
        bz.off()
        sleep(1)
        display.print("4")
        bz.on()
        bz.off()
        sleep(1)
        display.print("3")
        bz.on()
        bz.off()
        sleep(1)
        display.print("2")
        bz.on()
        bz.off()
        sleep(1)
        display.print("1")
        bz.on()
        bz.off()
        sleep(1)
        lights.red.off()
        lights.green.on()
        display.print("GO 15")
        sleep(1)
        display.print("GO 14")
        sleep(1)
        display.print("GO 13")
        sleep(1)
        display.print("GO 12")
        sleep(1)
        display.print("GO 11")
        sleep(1)
        display.print("GO 10")
        sleep(1)
        display.print("GO 9")
        sleep(1)
        display.print("GO 8")
        sleep(1)
        display.print("GO 7")
        sleep(1)
        display.print("GO 6")
        sleep(1)
        display.print("GO 5")
        sleep(1)
        display.print("GO 4")
        sleep(1)
        display.print("GO 3")
        sleep(1)
        display.print("GO 2")
        sleep(1)
        display.print("GO 1")
        sleep(1)
        display.print("GO")
        lights.amber.on()
        lights.green.off()
        sleep(3)
        display.print ("STOP")
        lights.green.off()
        lights.amber.off()
        lights.red.on()
    else:
        display.print("STOP")
        