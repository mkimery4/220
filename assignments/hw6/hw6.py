"""
Name: Margaret Kimery
hw6.py
Problem: Writing functions and strings that accept arguments and return values
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def cash_converter():
    integer = eval(input("enter an integer: "))
    answer = "That is ${price:.2f}"
    answer = answer.format(price = integer)
    print(answer)

def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    for i in message:
        e = (ord(i) + key)
        print(chr(e), end="")

def sphere_area(radius):
    return 4 * math.pi * (radius**2)

def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius**3)

def sum_n(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum

def sum_n_cubes(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i**3
    return sum

def encode_better():
    message = str(input("enter a message: "))
    key = str(input("enter a key: "))
    ret = ""
    for i in range(len(message)):
        charval = ord(message[i]) - 65
        keyval = ord(key[i % len(key)]) - 65
        cipherval = ((charval + keyval) % 58) + 65
        ciphertext = chr(cipherval)
        ret += ciphertext
        print(ret)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
