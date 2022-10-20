#07_06_yes_no.py

from guizero import *

def ask():
    if yesno("Question", "Yes or Yes?"):
        info("Result", "You clicked Yes")
    else:
        info("Result", "You clicked Yes")

app = App()
button = PushButton(app, text="Click Me", command=ask)
app.display()