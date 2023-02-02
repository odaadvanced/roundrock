from gpiozero import Buzzer
bz = Buzzer(26)

bz.on()

if bz.is_active:
    print ("work")