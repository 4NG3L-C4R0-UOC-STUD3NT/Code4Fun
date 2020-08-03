import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
turtle.pensize(2)
t.speed(5)

r,g,b = 255, 0, 0
for i in range(255 * 2):
    s.colormode(255)
    if i < 255//3:
        g += 3
    elif i < 255*2//3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < 255*4//3:
        g -= 3
    elif i < 255*5//3:
        r += 3
    else:
        b -= 3
    t.fd(50 + i)
    t.rt(91)
    t.pencolor(r,g,b)

time.sleep(30)

t.hideturtle()
turtle.done()

time.sleep(30)


