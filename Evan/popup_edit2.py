#07_06_yes_no.py

from guizero import *

def ask():
    if yesno("Question", "Would you like to activate a drone strike on your location?"):
        warn("Result", "You clicked Yes")
    else:
        warn("Result", "You clicked Yes")

app = App()
button = PushButton(app, text="Click Me", command=ask)
app.display()