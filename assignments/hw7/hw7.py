"""
Name: Margaret Kimery
<greeting_card()>.py
file: hw7.py
problem: Develop a Python program that uses numeric data from a text file.
certification of authenticity:
I certify that this assignment is entirely my own work.
"""


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    in_file_text = in_file.read()
    list_in = in_file_text.split()
    print(list_in)
    out_txt = " "
    for i in range(len(list_in)):
        out_txt = out_txt + str(i+1) + " " + list_in[i] + "\n"
    out_file.write(out_txt)


def hourly_wages(in_file_name, out_file_name):
    file = open(in_file_name, "r")
    out_file = open(out_file_name, "a")
    text = file.read()
    x = text.split("\n")
    for person in x:
        data = person.split()
        hourly_wage = eval(data[2])
        hours_worked = eval(data[2])
        pay = (hours_worked * hourly_wage) + (1.65 * hours_worked)
        out = data[0] + " " + data[1] + " " + "{:.2f}" + "\n"
        out_file.write(out.format(pay))
    file.close()
    out_file.close()

def calc_check_sum(isbn):
    inputted_isbn = str(isbn).replace("-", "")
    total = 0
    for i in range(10):
       user_reverse = inputted_isbn[::-1]
       user_index = eval(user_reverse[i])
       total = total + (user_index * (1 + i))
    return(total)


def send_message(file_name, friend_name):
    file = open(file_name, "r")
    file_read = file.read()
    new_file = open(friend_name + ".txt", "a")
    new_file.write(file_read)


def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    for i in message:
        e = (ord(i) + key)
        print(chr(e), end= "")


def send_safe_message(file_name, friend_name, key):
    file = open(file_name, "r")
    content = file.read()
    info = content.split("\n")
    new_friend = open(friend_name, "a")
    for i in range(len(info)):
        encoded = encode(info[i], key)
        new_friend.write(encoded)


 ## def send_uncrackable_message(file_name, friend_name, pad_file_name):
if __name__ == '__main__':
    pass
