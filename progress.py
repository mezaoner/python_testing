#Fil 
from math import ceil as goup

def split_check(total,number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    cost_per_person = total / number_of_people
    return goup(cost_per_person)

try:
    total_due = float(input("What is total due? "))
    num_peeps = int(input("How many are you? "))
    amount_due = split_check(total_due, num_peeps)
except ValueError as err:
    print("Please enter a valid value, try again")
    print("{}".format(err))
else:
    amount_due = split_check(total_due, num_peeps)
    print("each person owes {}".format(amount_due))