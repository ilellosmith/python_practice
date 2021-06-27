#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 22:19:23 2021

@author: isaaclello-smith
"""

def genPrimes():
    '''
    Returns sequence of prime numbers on successive calls to next() method
    
    This is very inefficient (could check starting at int(math.sqrt(current_number)), but you then need to decrement by 1)
    '''
    # initialize smallest prime number
    current_number = 2
    prime_flag = True # track if current_number is prime
    yield current_number
    # next move to 3, after which we can count up by 2, so only checking odd numbers
    current_number = 3
    # check larger odd numbers
    while True:
        prime_flag = True # base assumption is prime
        # if the number is even, negate flag
        if current_number%2 == 0:
            prime_flag = False
            pass
        else: 
            # otherwise, check all odd numbers less than current number but greater than 2, to see if any are divisors
            # if find a divisor, negate flag
            for n in range(current_number-2, 2, -2):
                if current_number%n == 0:
                    prime_flag = False
                    pass
        # if prime, yield
        if prime_flag:
            yield current_number
        # move to next odd number
        current_number += 2

# Demo that a yeild statement in a function, even if never executed, makes a generator object
def isGenerator():
        
    if False:
        yield 1
    else:
        pass
