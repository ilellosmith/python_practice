#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:42:58 2021

@author: isaaclello-smith
"""

def minMonthlyPayment(balance, annualInterestRate):
    '''
    Print lowest fixed monthly payment for 0 debt in 12 months

    Parameters
    ----------
    balance : float
        starting credit card balance.
    annualInterestRate : float
        annual interest rate in decimal.

    Returns
    -------
    None.

    '''
    
    # initialize variables 
    payment = 0
    monthlyInterestRate = annualInterestRate / 12.0
    originalBalance = balance
    
    # iterate through payment amounts 
    while balance > 0:
    
        # reset balance each time
        balance = originalBalance
    
        # simulate year at payment amount
        for month in range(1,13,1):
            monthlyUnpaidBalance = balance - payment
            balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
          
        if balance <= 0:
            break
        else:
           payment += 10
   
    print('Lowest Payment: %i'%payment)
    return payment
    
    # Algorithm
    # use while loop 
    # start at 0, increment by 10, check if enough, if so, end
    
# test cases

# EdX test case 1
assert(minMonthlyPayment(balance = 3329, annualInterestRate = 0.2) == 310)

# EdX test case 2
assert(minMonthlyPayment(balance = 4773, annualInterestRate = 0.2) == 440)

# EdX test case 3
assert(minMonthlyPayment(balance = 3926, annualInterestRate = 0.2) == 360)

# Remove from function for submission
balance = 3926
annualInterestRate = 0.2
# Copy below to submit

# initialize variables 
payment = 0
monthlyInterestRate = annualInterestRate / 12.0
originalBalance = balance

# iterate through increasing payment amounts 
while balance > 0:

    # reset balance each iteration
    balance = originalBalance

    # simulate year at payment amount
    for month in range(1,13,1):
        monthlyUnpaidBalance = balance - payment
        balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
      
    if balance <= 0:
        break
    else:
       payment += 10
   
print('Lowest Payment: %i'%payment)


def minMonthlyPaymentBisect(balance, annualInterestRate):
    '''
    Print lowest fixed monthly payment for 0 debt in 12 months

    Parameters
    ----------
    balance : float
        starting credit card balance.
    annualInterestRate : float
        annual interest rate in decimal.

    Returns
    -------
    None.

    '''
    
    # initialize variables 
    monthlyInterestRate = annualInterestRate / 12.0
    lowerBound = balance / 12.0
    upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
    originalBalance = balance
    payment = (lowerBound + upperBound) / 2
    
    # iterate through payment amounts 
    while abs(round(balance, 2)) >= 0.05:
    
        # reset balance each time
        balance = originalBalance
        payment = (lowerBound + upperBound) / 2
        print('Payment to test is: %.2f'%payment)
    
        # simulate year at payment amount
        for month in range(1,13,1):
            monthlyUnpaidBalance = balance - payment
            balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
       
        if abs(round(balance, 2)) <= 0.05:
            break
        elif balance < 0: 
            upperBound = payment
        else:
            lowerBound = payment
                
    print('Lowest Payment: %.2f'%payment)
    return round(payment, 2)
    
    # Algorithm
    # use while loop
    # calculate midpoint 
    # check if pays off in single year 
    # if too small, make lower, if too big, make upper
    # repeat 
    
    
# test cases

# EdX test case 1
assert(minMonthlyPaymentBisect(balance = 320000, annualInterestRate = 0.2) == 29157.09)

# EdX test case 2
assert(minMonthlyPaymentBisect(balance = 999999, annualInterestRate = 0.18) == 90325.03)

# Remove from function for submission
balance = 999999
annualInterestRate = 0.18
# Copy below to submit

# initialize variables 
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12.0
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
originalBalance = balance
payment = (lowerBound + upperBound) / 2

# iterate through payment amounts 
while abs(round(balance, 2)) >= 0.05:

    # reset balance each time
    balance = originalBalance
    payment = (lowerBound + upperBound) / 2

    # simulate year at payment amount
    for month in range(1,13,1):
        monthlyUnpaidBalance = balance - payment
        balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
   
    # update interval or exit
    if abs(round(balance, 2)) <= 0.05:
        break
    elif balance < 0: 
        upperBound = payment
    else:
        lowerBound = payment
            
print('Lowest Payment: %.2f'%payment)