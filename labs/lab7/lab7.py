"""
Name: Margaret Kimery
<greeting_card()>.py
file: lab7.py
problem: Develop a Python program that uses numeric data from a text file.
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
  in_file = open(in_file_name, "r")
  out_file = open(out_file_name, "w")
  in_file_strings = in_file.readlines()
  string_count = len(in_file_strings)
  class_average = 0
  for i in range(string_count):
    string_index = in_file_strings[i]
    colon = string_index.find(":")
    first_half = string_index[:colon]
    second_half = string_index[colon + 2:]
    second_list = second_half.split()
    second_length = len(second_list)
    denominator = second_length / 2
    total_weight = 0
    total_grade = 0
    class_average = 0
    for j in range(0, second_length, 2):
      weight = eval(second_list[j])
      grade = eval(second_list[j + 1])
      total_weight = total_weight + weight
      total_grade = total_grade + grade
      class_average = class_average + (weight + grade)
    if total_weight == 100:
      print(first_half + "'s average:", round((total_grade / denominator), 1))
    elif total_weight < 100:
      print(first_half + "'s average: Error: The weights are less than 100.")
    else:
      print(first_half + "'s average: Error: The weights are more than 100.")
  print("Class average:", class_average / 100)
  out_file.close()
  in_file.close()
