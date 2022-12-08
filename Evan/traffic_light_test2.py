from gpiozero import LED
from time import sleep

crossbutton = gpiozero.Button(19, pull_up=True)
green = LED(21)
amber = LED(26)
red = LED(17)

green.on()
amber.off()
red.off()

while True:
    sleep(10)
    green.off()
    amber.on()
    sleep(1)
    amber.off()
    red.on()
    sleep(10)
    amber.on()
    sleep(1)
    green.on()
    amber.off()
    red.off()
    