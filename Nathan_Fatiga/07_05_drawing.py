#07_05_drawing.py

from guizero import *

app = App(width=400, height=200)
drawing = Drawing(app, width="fill", height="fill")
drawing.rectangle(20, 20, 300, 100, color="red")
drawing.oval(30, 50, 290, 190, color='#ff2277')
drawing.line(0, 0, 400, 200, color='yellow', width=5)
drawing.text(37, 100, "YOOOOOO WHATS UP MY GUY", color="orange", font="LuckiestGuy", size=12)
app.display()
