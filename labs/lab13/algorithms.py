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


def selection_sort(values):
    n = len(values)
    minimum_value = min
    for minimum_value in range(n-1):
        num = n
        for num in range(minimum_value+1, num):
            values[min], values[minimum_value] = values[minimum_value], values[min]
            if values[n] < values[minimum_value]:
                minimum_value = n


def calc_area(rect):
    length = rect.getP1().getX() - rect.getP2().getX()
    width = rect.getP1().getY() - rect.getP2().getY()
    rect_area = width * length
    return rect_area


def rect_sort(rectangles):
    rect_area = calc_area(rectangles)