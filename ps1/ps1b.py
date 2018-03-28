# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:01:28 2018

@author: doron
"""

total_months = 0
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0.0
annual_return = 0.04
monthly_return = annual_return / 12.0
monthly_salary = annual_salary / 12.0

down_payment_required = total_cost * portion_down_payment

while current_savings < down_payment_required:
    
    if total_months % 6 == 0 and total_months != 0:   
        monthly_salary = monthly_salary + monthly_salary * semi_annual_raise
    current_savings = current_savings + (monthly_salary * portion_saved) + \
    (current_savings * monthly_return)
    total_months += 1
    

print("In order to save", down_payment_required, "it will take you", total_months, "months.")