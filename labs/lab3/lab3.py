"""
Name: Margaret Kimery
<traffic()>.py
file: lab3.py
problem: Practice accumulations and nested loops
certification of authenticity:
I certify that this assignment is entirely my own work.

"""

def traffic():
    roads_surveyed = eval(input("How many roads were surveyed? "))
    total_cars = 0
    for i in range(roads_surveyed):
        average = 0
        print("How many days was road", i+1, "surveyed? ")
        road_1 = eval(input(""))
        for j in range(road_1):
            print("How many cars traveled on day", j+1)
            cars_traveled = eval(input(" "))
            average = average + cars_traveled
            total_cars = total_cars + cars_traveled
        average = average / road_1
        print("Road 1 average vehicles per day:", average)
    print("Total number of vehicles traveled on all roads:", total_cars)
    print("Average number of vehicles per road:", (total_cars / roads_surveyed))

traffic()




