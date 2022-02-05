"""
Name: Margaret Kimery
hw3.py
Problem: Develop simple Python programs that use for loops.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
        grade_amount = eval(input("how many grades will you enter?"))
        average = 0
        for i in range(grade_amount):
            print("Enter grade: ")
            grades = eval(input(" "))
        average = grades / grade_amount
        print("average is", average)

def tip_jar():
    donate_amount = eval(input("how much would you like to donate?"))
    donate_total = 0
    for i in range(4):
        donates = eval(input("how much would you like to donate?"))
    donate_total = donate_amount + donates
    print("total tips:", donate_total)

def newton():
    number = eval(input("What number do you want to square root? "))
    improve = eval(input("How many times should we improve the approximation? "))
    approx = ((number / improve) + improve) / 2
    print("the square root is approximately", approx)

def sequence():
    ## ????


def pi(): ## ????
    n = eval(input("how many terms in the series?"))
    ans = 2.0
    for i in range(1, n):
        left = (2.0 * i) / (2.0 * i - 1.0)
        right = (2.0 * i) / (2.0 * i + 1.0)
        ans = ans * left * right
    return ans
    print(pi(100000))


if __name__ == '__main__':
        pass


