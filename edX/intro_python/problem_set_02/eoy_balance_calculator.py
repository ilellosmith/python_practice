#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:10:51 2021

@author: isaaclello-smith
"""

def eoyBalance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Prints credit card balance after one year

    Parameters
    ----------
    balance : float
        starting credit card balance.
    annualInterestRate : float
        annual interest rate in decimal.
    monthlyPaymentRate : TYPE
        monthly payment rate in decimal.

    Returns
    -------
    Final balance at end of year.
    '''

    # initialize values 
    monthlyInterestRate = annualInterestRate / 12.0
    
    # iterate over months, calculating end of month balance
    for month in range(1,13,1):
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
        print(f'Month {month} Remaining balance:{balance:.2f}')
    
    print(f'Remaining balance: {balance:.2f}')  # EdX uses Pythonn 3.5, cannot interpret f strings which came in 3.6
    
    # remove for final
    return round(balance, 2)
    
# test cases

# EdX test case 1
assert(eoyBalance(balance = 42, annualInterestRate = 0.2, monthlyPaymentRate = 0.04) == 31.38)

# EdX test case 2
assert(eoyBalance(balance = 484, annualInterestRate = 0.2, monthlyPaymentRate = 0.04) == 361.61)

# Remove from function for submission
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# Copy below to submit

# initialize values 
monthlyInterestRate = annualInterestRate / 12.0
    
# iterate over months, calculating end of month balance
for month in range(1,13,1):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate

print('Remaining balance: %.2f'%round(balance,2))