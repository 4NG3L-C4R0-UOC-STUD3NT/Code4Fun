import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pensize(2)
t.speed(0)

t.color('red', 'yellow')
t.begin_fill()

while True:
    t.forward(300)
    t.left(170)
    if abs(t.pos()) < 1:
        break

t.end_fill()

time.sleep(15)

t.hideturtle()
turtle.done()

time.sleep(15)
