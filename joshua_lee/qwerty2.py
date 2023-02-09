from oled_io import Oled_io

display = Oled_io()

while True:
    display.print("hello world")
    if show_colon:
        display.colon = True
        show_colon = False
    else:
        display.colon = False
        show_colon = True
    time.sleep(0.5)