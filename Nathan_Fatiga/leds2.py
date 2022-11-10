import gpiozero, time
led = gpiozero.LED(18)
while True:
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)