"""
Name: Margaret Kimery
hw5.py
Problem: manipulating strings and lists
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("enter a name (first and last name): ")
    name_split = str.split(name)
    first = name_split[0]
    last = name_split[1]
    print(last + "," + " " + first)

def company_name():
    domain = input("enter a domain")
    domain_split = str.split(domain,".")
    print(domain_split[1])

def initials():
    student_amount = eval(input("how many students are in the class?"))
    for i in range(student_amount):
        name = input("what is the name of student " + str(i+1) + "?")
        print(name.split()[0][0:1] + name.split()[1][0:1])

def names():
    name_list = input("enter a list of names:")
    for i in name_list.split(", "):
        print(i.split()[0][0:1] + i.split()[1][0:1], end=" ")


def thirds():
    num = eval(input("enter the number of sentences: "))
    sentences = []
    for i in range(num):
        sent = input("enter sentence " + str(i+1) + ":")
        sentences.append(sent)
    for i in sentences:
        output = ""
        for j in range(0, len(i), 3):
            output += i[j]
        print(output)

def word_average():
    sentence = input("enter a sentence: ")




def pig_latin():

if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
