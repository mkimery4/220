"""
Name: Margaret Kimery
<monthly_interest()>.py
file: lab1.py
problem: creating a python program using a given algorithm
certification of authenticity:
I certify that this assignment is entirely my own work.

"""
def monthly_interest():
    annual_interest = eval(input("Enter the annual interest: "))
    billing_cycle = eval(input("Enter the billing cycle days: "))
    previous_amount = eval(input("Enter previous amount before payment: "))
    payment_amount = eval(input("Enter payment amount: "))
    payment_day = eval(input("Enter day of payment: "))

    step_1 = previous_amount * billing_cycle
    step_2 = payment_amount * (billing_cycle - payment_day)
    step_3 = step_1 - step_2
    average_daily = step_3 / billing_cycle
    monthly_interest = average_daily * (annual_interest / 12) / 100
    print("Your Monthly Interest is: $", monthly_interest)

monthly_interest()






