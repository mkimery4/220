"""
Name: Margaret Kimery
file: lab12.py
problem: Use Python's built-in list functions, Develop while control structures, Use boolean logic
certification of authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(file_name):
    with open(file_name, "r") as file:
        data = file.readlines()
        i = 0
        empty_list = []
        while i < len(data):
            element = data[i]
            i = i + 1
            element_split = element.split()
            counter = 0
            while counter < len(element_split):
               convert = eval(element_split[counter])
               empty_list.append(convert)
               counter = counter + 1
        return data



def is_in_linear(search_val, values):
    counter = 0
    while counter < len(values):
        if search_val == values[counter]:
            return True
        counter = counter + 1
    return False