"""
Name: Margaret Kimery
Lab6.py
Problem: Practice processing string data
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

def vigenere():
    win = GraphWin("Vigenere", 500, 500)
    text = Text(Point(80, 80), "Message to code")
    text.draw(win)

    text2 = Text(Point(80, 115), "Enter Keyword")
    text2.draw(win)

    messageBox = Entry(Point(300, 80), 50)
    messageBox.draw(win)
    messageBox.setFill("gray")

    messageBox2 = Entry(Point(240, 115), 30)
    messageBox2.draw(win)
    messageBox2.setFill("gray")

    rect = Rectangle(Point(200,260), Point(300,180))
    rect.draw(win)

    text3 = Text(Point(250, 220), "Encode")
    text3.draw(win)

    text4 = Text(Point(250, 450), "Click Anywhere to Close Window")
    text4.draw(win)

    win.getMouse()
    rect.undraw()
    text3.undraw()

    text5 = Text(Point(250, 220), "Resulting Message")
    text5.draw(win)
    result = messageBox.getText()
    result = result.upper()
    result = result.replace(" ","")
    result2 = messageBox2.getText()
    result2 = result2.upper()
    result2 = result2.replace(" ","")
    print(result)
    print(result2)
    ret = ""
    for i in range(len(result)):
        e = (ord(result[i]) - 65)
        a = (ord(result2[i%len(result2)]) - 65)
        c = ((e + a) %26) + 65
        ret += (chr(c))

    text6 = Text(Point(250, 245), ret)
    text6.draw(win)

    win.getMouse()
    win.close()



