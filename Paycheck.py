'''
Paycheck
Pawelski
3/9/2023
Python II
'''

import colorama

name = input("What is your name? >> ")
hours_worked = int(input("How many hours did you work this week? >> "))
hourly_wage = float(input("How much do you make per hour? >> "))
paycheck = hourly_wage * hours_worked
print(name + " should get paid $" + str(paycheck)) # Is there another way to write this line?