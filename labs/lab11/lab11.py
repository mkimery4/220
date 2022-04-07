"""
Name: Margaret Kimery
<ThreeDoorGame>.py
file: lab10.py
problem: Use Python's built-in list functions, Develop while control structures, Use boolean logic
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import randint


def three_door_game():
    win = GraphWin("Three Door Game", 500, 500)
    door1 = Rectangle(Point(100, 100), Point(170, 400))
    door1.setFill("Yellow")
    door1 = Door(door1, "Door 1")
    door1.draw(win)

    door2 = Rectangle(Point(200, 100), Point(270, 400))
    door2.setFill("Yellow")
    door2 = Door(door2, "Door 2")
    door2.draw(win)

    door3 = Rectangle(Point(300, 100), Point(370, 400))
    door3.setFill("Yellow")
    door3 = Door(door3, "Door 3")
    door3.draw(win)

    quit = Rectangle(Point(390, 30), Point(450, 70))
    quit.setFill("Gray")
    quit = Button(quit, "Quit")
    quit.draw(win)

    score = Rectangle(Point(50, 70), Point(90, 30))
    score.setFill("Gray")
    score.draw(win)
    score2 = Rectangle(Point(70, 70), Point(90, 30))
    score2.setFill("Gray")
    score2.draw(win)
    text7 = Text(Point(70, 20), "Win  Lose")
    text7.draw(win)
    wins = 0
    wins_label = Text(Point(60, 50), "0")
    wins_label.draw(win)
    lose = 0
    lose_label = Text(Point(80, 50), "0")
    lose_label.draw(win)

    text1 = Text(Point(250, 450), "Click to guess the secret door!")
    text1.draw(win)

    text5 = Text(Point(250, 80), "I have a secret door")
    text5.draw(win)

    random_door = randint(1, 3)

    if random_door == 1:
        door1.set_secret(True)

    elif random_door == 2:
        door2.set_secret(True)

    elif random_door == 3:
        door3.set_secret(True)

    clicked = win.getMouse()

    while not quit.is_clicked(clicked):
        if door1.is_clicked(clicked):
            if door1.is_secret():
                door1.color_door("Green")
                text5.setText("you win!")
                wins = wins + 1
                wins_label.setText(wins)
                wins_label.setText(wins)
                text1.setText("click anywhere to play again")
            else:
                door1.color_door("Red")
                text5.setText("sorry, incorrect.")
                lose = lose + 1
                lose_label.setText(lose)
                text1.setText("click anywhere to play again")

        if door2.is_clicked(clicked):
            if door2.is_secret():
                door2.color_door("Green")
                text5.setText("you win!")
                wins = wins + 1
                wins_label.setText(wins)
                text1.setText("click anywhere to play again")
            else:
                door2.color_door("Red")
                text5.setText("sorry, incorrect.")
                lose = lose + 1
                lose_label.setText(lose)
                text1.setText("click anywhere to play again")

        if door3.is_clicked(clicked):
            if door3.is_secret():
                door3.color_door("Green")
                text5.setText("you win!")
                wins = wins + 1
                wins_label.setText(wins)
                text1.setText("click anywhere to play again")
            else:
                door3.color_door("Red")
                text5.setText("sorry, incorrect.")
                lose = lose + 1
                lose_label.setText(lose)
                text1.setText("click anywhere to play again")
        clicked = win.getMouse()

        if quit.is_clicked(clicked):
            win.close()
        else:
            text1.setText("Click to guess which is the secret door!")
            text5.setText("I have a secret door")
            door1.color_door("Yellow")
            door2.color_door("Yellow")
            door3.color_door("Yellow")
            random_door = randint(1, 3)

    win.close()

# setText/color_door
# implement colors/text resetting (getting next 'guess' click)
# implement 'exit' during the reset click
