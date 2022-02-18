"""
Name: Margaret Kimery
<greeting_card()>.py
file: lab5.py
problem: Develop a Python program that uses the author's graphics package
certification of authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

def triangle():
    win = GraphWin("Triangle", 500, 500)
    text = Text(Point(80, 80), "Click 3 times to draw a triangle")
    text.draw(win)
    p1 = win.getMouse() 
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)
    length1 = (((p1.getX() - p2.getX()) ** 2) + ((p1.getY() - p2.getY()) ** 2)) ** 0.5
    length2 = (((p1.getX() - p3.getX()) ** 2) + ((p1.getY() - p3.getY()) ** 2)) ** 0.5
    length3 = (((p3.getX() - p2.getX()) ** 2) + ((p3.getY() - p2.getY()) ** 2)) ** 0.5
    perimeter = length1 + length2 + length3
    text2 = Text(Point(250, 350), "Perimeter: " + str(perimeter))
    text2.draw(win)
    s = (length1 + length2 + length3) / 2
    area = (s*(s - length1)*(s - length2)*(s - length3)) ** 0.5
    text3 = Text(Point(250, 400), "Area:" + str(area))
    text3.draw(win)
    text4 = Text(Point(250, 450), "Click again to close")
    text4.draw(win)
    win.getMouse()
    win.close()


def color_shape():
 # # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")
    
    r = Entry(Point(win_width / 2 - 25, win_height / 2 + 40), 3)
    r.draw(win)
    g = Entry(Point(win_width / 2 - 25, win_height / 2 + 70), 3)
    g.draw(win)
    b = Entry(Point(win_width / 2 - 25, win_height / 2 + 100), 3)
    b.draw(win)

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        red = eval(r.getText())
        blue = eval(b.getText())
        green = eval(g.getText())
        shape.setFill(color_rgb(red, green, blue))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
     string = (input("Enter a string: "))
     print(string[0])
     print(len(string) - 1)
     print(string[2] + string[5])
     for i in range(3):
         print(string[3], end="")
     print()
     for i in string:
         print(i)
     print(len(string))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    print("x: ", values[1] + values[3])
    print("x: ", values[0] + values[2])
    print("x: ", values[1] * 5)
    print("x: ", values[2:5])
    print("x: ", [values[3:4], values[0]])
    print("x: ", [values[3], values[0], values[5]])
    print("x: ", values[0] + values[2] + float(values[5]))
    print("x: ", len(values))

def another_series():
    num_terms = eval(input("enter number of terms: "))
    sum = 0
    for i in range(int(((num_terms - 1) + 3) / 3)):
        sum = sum + 2
    for i in range(int(((num_terms - 2) + 3) / 3)):
        sum = sum + 4
    for i in range(int(((num_terms - 3) + 3) / 3)):
        sum = sum + 6

    print(sum)


def target():
  win = GraphWin("Circle", 500, 500)
  center = Point(250, 250)
  radius = 250
  circle = Circle(center, radius)
  circle.draw(win)
  circle.setFill("white")
  center2 = Point(250, 250)
  radius2 = 200
  circle2 = Circle(center2, radius2)
  circle2.draw(win)
  circle2.setFill("black")
  center3 = Point(250, 250)
  radius3 = 150
  circle3 = Circle(center3, radius3)
  circle3.draw(win)
  circle3.setFill("blue")
  center4 = Point(250, 250)
  radius4 = 100
  circle4 = Circle(center4, radius4)
  circle4.draw(win)
  circle4.setFill("red")
  center5 = Point(250, 250)
  radius5 = 50
  circle5 = Circle(center5, radius5)
  circle5.draw(win)                 
  circle5.setFill("yellow")
  text = Text(Point(250, 250), "Click again to close")
  text.draw(win)
  win.getMouse()
  win.close()