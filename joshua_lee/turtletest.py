from turtle import *
color('blue', 'cyan')
begin_fill()
while True:
    forward(1)
    left(0.5)
    if abs(pos()) < 1:
        break
end_fill()
while True:
    forward(100)
    left(90)
    if abs(pos()) < 1:
        break
end_fill()
while True:
    forward(100)
    left(120)
    if abs(pos()) < 1:
        break
end_fill()

done()