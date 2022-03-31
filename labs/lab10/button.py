"""
Name: Margaret Kimery
<()>.py
file: lab9.py
problem: Use Python's built-in list functions, Develop while control structures, Use boolean logic
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

class Button:
    def __init__(self, shape, string):
        self.shape = shape
        self.string = Text(shape.getCenter(), string)


    def get_label(self):
        label = self.string.getText()
        return label


    def set_label(self, label):
        self.string.setText(label)


    def draw(self, win):
        self.shape.draw(win)
        self.string.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.string.undraw()

    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        if p1.getX() <= point.getX() <= p2.getX() and p1.getY() <= point.getY() <= p2.getY():
            return True
        else:
            return False


    def color_button(self, color):
        self.shape.setFill(color)

