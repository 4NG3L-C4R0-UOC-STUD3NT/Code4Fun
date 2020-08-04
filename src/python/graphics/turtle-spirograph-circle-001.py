import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
turtle.pensize(2)
t.speed(0)

for i in range(6):
    for color in ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white']:
        turtle.color(color)
        turtle.circle(100)
        turtle.left(10)

time.sleep(30)

t.hideturtle()
turtle.done()

time.sleep(30)
