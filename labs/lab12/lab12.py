"""
Name: Margaret Kimery
file: lab12.py
problem: Use Python's built-in list functions, Develop while control structures, Use boolean logic
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint

def find_and_remove_first(list, value):
    # value_variable = list[value]
    value_index = list.index(value)
    list.remove(value)
    list.replace(value_index, "Margaret")



def good_input():
    user_input = eval(input("Input a number"))
    while not 1 <= user_input <= 10:
        if user_input > 10:
            print("Wrong, input another number")
        if user_input < 1:
            print("Wrong, input another number")
        user_input = eval(input("Input a number"))
    print("Valid")
    return user_input


def num_digits():
    user_num = eval(input("Input a number"))
    while 0 < user_num > -1:
        counter = 0
        while 0 < user_num > -1:
            user_num = user_num // 10
            counter = counter + 1
        print("this input has this many numbers,", counter)
        user_num = eval(input("Input a number"))



def hi_lo_game():
    random_number = randint(1, 100)
    user_random_num = eval(input("Input a number"))
    guesses = 7
    while guesses > 0:
        if user_random_num > random_number:
            guesses = guesses - 1
            user_random_num = eval(input("Too high, Input a number"))
        if user_random_num < random_number:
            guesses = guesses - 1
            user_random_num = eval(input("Too low, Input a number"))
        if user_random_num == random_number:
            guesses = 7 - guesses
            print("You win! it took", guesses, "guesses")
            guesses = -1
    if guesses == 0:
        print("You lost.")













