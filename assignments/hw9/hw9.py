"""
Name: Margaret Kimery
hw9.py
Problem: Use conditionals and functions
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import random
from graphics import *


def get_words(file_name):
    words = open(file_name, "r")
    words_file = words.read()
    return words_file.split("\n")


def get_random_word(words):
    return words[random.randint(0,len(words))]


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False


def already_guessed(letter, guesses):
    for i in range(len(guesses)):
        if letter == guesses[i]:
            return True
    return False


def make_hidden_secret(secret_word, guesses):
    word_guess = "_ "*len(secret_word)
    split_word_guess = word_guess.split(" ")
    for i in range(len(guesses)):
        if letter_in_secret_word(guesses[i], secret_word):
            split_word_guess[secret_word.find(guesses[i])] = guesses[i]
    join = " ".join(split_word_guess)
    return join


def won(guessed):
    for i in range(0,len(guessed), 2):
        if "_" == guessed[i]:
            return True
    return False


def play_graphics(secret_word):
    win = GraphWin("Hangman", 500, 500)
    GraphWin.draw(win)
    post1 = Line(Point(125,75), Point(125,25))
    post2 = Line(Point(125, 25), Point(220,25))
    post3 = Line(Point(220, 25), Point(220, 425))
    post4 = Line(Point(260, 425), Point(180, 425))

    head = Circle(Point(125, 125), 50)
    body = Line(Point(125, head.getCenter().getY() + head.getRadius()), Point(125, 305))
    left_arm = Line(Point(125,240), Point(80,240))
    right_arm = Line(Point(170,240), Point(125,240))
    left_leg = Line(Point(125,305), Point(80,370))
    right_leg = Line(Point(125,305), Point(170,370))





def play_command_line(secret_word):
    guesses_left = 6
    guesses = []
    guessed = make_hidden_secret(secret_word, guesses)
    while not(won(guessed) or guesses_left == 0):
        print("already guessed: ", guesses)
        print("guesses remaining: ", guesses_left)
        print(guessed)
        letter = input("guess a letter: ")
        while already_guessed(letter, guesses):
            letter = input("already guessed, go again: ")
        guesses.append(letter)
        if letter_in_secret_word(letter, secret_word):
            guessed = make_hidden_secret(secret_word, guesses)
        else:
            guesses_left -= 1
    if won(guesses):
        print("winner!" + "\n" + secret_word)
    else:
        print("sorry, you did not guess the word." + "\n" + "the secret word was " + secret_word)



if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
