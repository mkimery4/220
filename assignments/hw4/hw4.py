"""
Name: Margaret Kimery
hw4.py
Problem: Python graphics.
Use the author-supplied graphics package.
Practice accumulating sequences.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import *
from math import *

def squares():
    win = GraphWin("Square", 500, 500)
    text = Text(Point(80, 80), "Click to draw a square")
    text.draw(win)
    p1 = Point(150, 150)
    p2 = Point(200, 200)
    rect = Rectangle(p1, p2)

    rect.draw(win)
    rect.setFill("purple")

    for i in range(5):
        p3 = win.getMouse()
        rect2 = Rectangle(Point(p3.getX()-25, p3.getY()-25), Point(p3.getX()+25, p3.getY()+25))
        rect2.draw(win)
        rect2.setFill("purple")
    text2 = Text(Point(250, 400), "Click again to close")
    text2.draw(win)
    win.getMouse()
    win.close()

def rectangle():
    win = GraphWin("Rectangle", 500, 500)
    p1 = win.getMouse()
    p2 = win.getMouse()
    rect = Rectangle(p1, p2)

    rect.draw(win)
    rect.setFill("purple")
    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getY() - p1.getY())
    perimeter = (length + width) * 2
    area = length * width
    text = Text(Point(250, 350), "Perimeter:" + str(perimeter))
    text.draw(win)
    text2 = Text(Point(250, 400), "Area:" + str(area))
    text2.draw(win)
    text3 = Text(Point(80, 80), "Click again to close")
    text3.draw(win)
    win.getMouse()
    win.close()

def circle():
    win = GraphWin("Circle", 500, 500)
    center = win.getMouse()
    circum = win.getMouse()
    radius = sqrt((center.getX() - circum.getX())**2 + (center.getY() - circum.getY())**2)
    circle = Circle(center, radius)
    circle.draw(win)
    circle.setFill("purple")
    text = Text(Point(250, 350), "Radius:" + str(radius))
    text.draw(win)
    text2 = Text(Point(250, 400), "Click again to close")
    text2.draw(win)
    win.getMouse()
    win.close()

def pi2():
    total = 0
    n = eval(input("enter the number of terms to sum: "))
    num_add = int(n / 2) + (n % 2)
    num_sub = int(n / 2)
    for i in range(num_add):
        num = 4
        denom = 4 * i + 1
        frac = (num / denom)
        total += frac
    for i in range(num_sub):
        num = 4
        denom = 4 * i + 3
        frac = (num / denom)
        total -= frac
    print("pi approximation:", total)
    approx = abs(math.pi - total)
    print("accuracy:", approx)













