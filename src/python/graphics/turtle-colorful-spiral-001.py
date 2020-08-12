import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pensize(2)
t.speed(0)

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

time.sleep(15)

t.hideturtle()
turtle.done()

time.sleep(15)
