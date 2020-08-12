# https://mcsp.wartburg.edu/zelle/
# https://mcsp.wartburg.edu/zelle/pubs.html
# https://mcsp.wartburg.edu/zelle/python/index.html
# https://mcsp.wartburg.edu/zelle/python/graphics.py

# http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html

from _graphics import *
import time

win = GraphWin()

pt = Point(100, 50)
pt.draw(win)

time.sleep(4)

cir = Circle(pt, 25)
cir.draw(win)
cir.setOutline('red')
cir.setFill('blue')

time.sleep(4)

line = Line(pt, Point(150, 100))
line.draw(win)

time.sleep(4)

line.move(10, 40)

time.sleep(4)

rect = Rectangle(Point(20, 10), pt)
rect.draw(win)

time.sleep(4)

message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()


