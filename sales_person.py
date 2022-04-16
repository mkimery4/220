"""
Name: Margaret Kimery
hw11.py
Problem: Use conditionals and functions
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

class SalesPerson:
    def __init__(self,employee_id,name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for i in self.sales:
            total += i
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self,quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self,other):
        if other.total_sales() > self.total_sales():
            return -1
        elif other.total_sales() > self.total_sales():
            return 1
        else:
            return 0

    def __str__(self):
        return "[" + self.employee_id + self.name + self.total_sales() + "]"





