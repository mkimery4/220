"""
Name: Margaret Kimery
<greeting_card()>.py
file: lab4.py
problem: Develop a Python program that uses the author's graphics package
certification of authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
from math import *


def greeting_card():
    win = GraphWin("Circle", 500, 500)
    center = Point(250, 250)
    radius = 50
    circle = Circle(center, radius)
    circle.draw(win)
    circle.setFill("pink")
    circle.setOutline("pink")
    center2 = Point(330, 250)
    radius2 = 50
    circle2 = Circle(center2, radius2)
    circle2.draw(win)
    circle2.setFill("pink")
    circle2.setOutline("pink")
    triangle = Polygon(Point(199, 260), Point(381, 260), Point((circle.getCenter().getX() + circle2.getCenter().getX()) / 2, 400))
    triangle.draw(win)
    triangle.setFill("pink")
    triangle.setOutline("pink")
    text = Text(Point(140, 140), "Happy Valentine's Day!")
    text2 = Text(Point(250, 450), "Click anywhere to close")
    text.draw(win)
    text2.draw(win)
    line = Line(Point(0, 500), Point(-50, 550))
    line.setArrow("first")
    line.draw(win)
    line.setFill("red")
    center3 = Point(330, 250)
    radius3 = 50
    circle3 = Circle(center2, radius2)
    circle3.draw(win)
    circle3.setFill("pink")
    circle3.setOutline("pink")
    for i in range(45):
        time.sleep(0.1)
        line.move(13, -10)
    win.getMouse()
    win.close()

greeting_card()





