#07_05_drawing.py

from guizero import *

app = App(width=400, height=200)
drawing = Drawing(app, width="fill", height="fill")
drawing.rectangle(0, 0, 130, 500, color="green")
drawing.rectangle(250, 0, 130, 5000, color='white')
drawing.rectangle(300, 0, 130, 5000, color='red')
drawing.text(50, 70, "Hola Mundo!", color="black", font="Zapfino", size=35)
app.display()

#This program is unfinished
