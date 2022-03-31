"""
Name: Margaret Kimery
<()>.py
file: lab9.py
problem: Use Python's built-in list functions, Develop while control structures, Use boolean logic
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

class Door:
    def __init__(self, shape, string):
        self.shape = shape
        self.text = Text(shape.getCenter(), string)
        self.secret = False

    def get_label(self):
        label = self.text.getText()
        return label

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        if p1.getX() <= point.getX() <= p2.getX() and p1.getY() <= point.getY() <= p2.getY():
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)


    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)


    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        return self.secret


    def set_secret(self, secret):
        self.secret = secret