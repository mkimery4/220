"""
Name: Margaret Kimery
hw11.py
Problem: Use conditionals and functions
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self,file_name):
        with open(file_name, "r") as file:
            data = file.readline()
            for line in data: # loops through each line in txt file so each SalesPerson
                list_split = line.split(", ")
                employee_id = int(list_split[0])
                name = list_split[1]
                sales_person = SalesPerson(employee_id, name)
                for i in list_split[2:]: # loops through however many sales a single SalesPerson has
                    sales_person.enter_sale(float(i))
                self.sales_people.append(sales_person)


    def quota_report(self,quota):
        return_list = []
        for i in self.sales_people:
            identification = i.get_id()
            return_list.append(identification)
            i_name = i.get_name()
            return_list.append(i_name)
            i_total = i.total_sales()
            return_list.append(i_total)
            met_quota = i.met_quota()
            return_list.append(met_quota)
            hit_quota = False
            if i_total >= met_quota:
                hit_quota = True
            return_list.append(hit_quota)
        return return_list


    def top_seller(self):
        sales_person_list = []
        updated_list = []
        most_sold = 0
        counter = 0
        for sales in self.sales_people:
            sales_person_list.append(SalesPerson(sales[0], sales[1]))
            num_sales = str(sales[2])
        for seller in sales_person_list:
            if seller.total_sales() == most_sold:
                sales_person_list.append(seller)
        return sales_person_list


    def individual_sales(self,employee_id):
        for i in range(len(self.sales_people)):
            if self.sales_people[i].get_id() == employee_id:
                return self.sales_people[i]
            else:
                return None


    def get_sale_frequencies(self):
        rtn_dict = {}
        for person in self.sales_people:
            for sale in person.get_sales():
                if rtn_dict.get(sale, -1) == -1:
                    rtn_dict[sale] = 1
                else:
                    rtn_dict[sale] = rtn_dict[sale] + 1
            return rtn_dict

