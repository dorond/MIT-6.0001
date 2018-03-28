# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:38:54 2018

@author: doron
"""
#What is the optimal savings rate to obtain a 25% down payment on a $1M house in 36 months

annual_salary = float(input("Enter the starting salary: "))

total_months = 36
total_cost = 1000000.0
semi_annual_raise = 0.07
portion_down_payment = 0.25
annual_return = 0.04
monthly_salary = annual_salary / 12.0
monthly_return = annual_return / 12.0
down_payment_required = total_cost * portion_down_payment
epsilon = 100   #required down payment within this range
num_guesses = 0
current_savings = 0.0

low_rate = 0
high_rate = 10000

guess_rate = (low + high) / 2

while abs(current_savings - down_payment_required) > epilson:
     



