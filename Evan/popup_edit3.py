#07_06_yes_no.py

from guizero import *

def ask():
    if yesno("Question", "Would you like to money?"):
        info("Result", "Then go get a job")
    else:
        info("Result", "Really?")

app = App()
button = PushButton(app, text="Click Me", command=ask)
app.display()