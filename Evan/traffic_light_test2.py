import gpiozero
from gpiozero import LED
from time import sleep

crossbutton = gpiozero.Button(19, pull_up=True)
green = LED(21)
amber = LED(26)
red = LED(17)

green.off()
amber.off()
red.on()

while True:
    if crossbutton.is_pressed:
        sleep(5)
        amber.on()
        red.off()
        sleep(3)
        amber.off()
        green.on()
        sleep(15)
        green.off()
        amber.on()
        sleep(3)
        amber.off()
        red.on()