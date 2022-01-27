"""
Name: Margaret Kimery
<means()>.py
file: lab2.py
problem: developing a simple python program that asks for input, does arithmetic, and provides output
certification of authenticity:
I certify that this assignment is entirely my own work.

"""

def means():
    value_amount = eval(input("enter the values to be entered: "))
    rms_accumulator = 0
    harmonica_accumulator = 0
    geometric_accumulator = 1
    for i in range(value_amount):
        user_input = eval(input("enter the values to be entered: "))
        rms_accumulator = rms_accumulator + user_input**2
        harmonica_accumulator = harmonica_accumulator + (1/user_input)
        geometric_accumulator = geometric_accumulator * user_input
    rms_mean = (rms_accumulator / value_amount)**0.5
    harmonica_mean = (value_amount / harmonica_accumulator)
    geometric_mean = (geometric_accumulator) ** (1/value_amount)
    print("The root-mean-square is", rms_mean)
    print("The harmonica mean is", harmonica_mean)
    print("The geometric mean is", geometric_mean)

means()
