"""
Name: Margaret Kimery
<ProgramName>.py
file: hw2.py
Problem: <Brief, one or two sentence descriptioves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    user_input = eval(input("what is the upper bound?"))
    number = user_input // 3
    sum = 3 * (number * (number + 1) // 2)
    print("sum of threes is," + sum)

def multiplication_table():
    for i in range(1, 11):
        print(str(1 * i) + " " + str(2 * i) + " " + str(3 * i) + " " + str(4 * i) + " " + str(5 * i) + " " + str(6 * i) + " " + str(7 * i) + " " + str(8 + i) + " " + str(9 + i) + " " + str(10 + i))


def triangle_area():
    length_a = eval(input("Enter side a length: "))
    length_b = eval(input("Enter side b length: "))
    length_c = eval(input("Enter side c length: "))
    s = (length_a + length_b + length_c) / 2
    a = (s(s - length_a)(s - length_b)(s - length_c))**0.5
    print("area is," + a)

def sum_squares():
    lower_range = eval(input("Enter lower range: "))
    upper_range = eval(input("Enter upper range: "))
    answer = 0
    for i in range(lower_range, upper_range + 1):
        answer = answer + (i * i)
    print(answer)

def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    answer = 1
    for i in range(exponent):
        answer = answer * base
    print(answer)

if __name__ == '__main__':
    pass
