from gpiozero import TrafficLights
from time import sleep

lights = TrafficLights(21, 20, 16)

lights.green.on()

while True:
    sleep(10)
    lights.green.off()
    lights.amber.on()
    sleep(5)
    lights.amber.off()
    lights.red.on()
    sleep(16)
    lights.green.on()
    lights.red.off()