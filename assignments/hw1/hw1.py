"""
Name: Margaret Kimery
<Program name>.py
file: hw1.py
problem: Understanding the editing and execution phases of a computer program using Python
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)



def calc_volume():
    length = eval(input("Enter the length"))
    width = eval(input("Enter the width"))
    height = eval(input("Enter the height"))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    shots = eval(input("Enter player's total shots: "))
    made = eval(input("Enter how many shots the player made: "))
    percentage = made / shots * 100
    print("Shooting percentage =", percentage)


def coffee():
    coffee = eval(input("How many pounds of coffee would you like? "))
    pound = 10.50
    total = pound - 0.86 - 1.50
    print("You're total is:", total)


def kilometers_to_miles():
    miles = eval(input("How many kilometers did you travel? "))
    total = miles + 0.61
    print("That's", total, "miles!")


if __name__ == '__main__':
    pass



