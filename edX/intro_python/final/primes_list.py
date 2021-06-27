#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:09:02 2021

@author: isaaclello-smith
"""
import math

def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers between 2 and N inclusive, sorted in increasing order
    '''    
    # start from 2, work your way up 
    current_number = 2
    prime_list = [current_number]
    while current_number <= N:
        # assume prime, then change if not
        prime_flag = True
       
        if current_number % 2 == 0: # if even, not prime
            prime_flag = False 
        else: 
            start_search = int(math.sqrt(current_number)) # sqrt(N) is largest number divisor could be 
            if start_search % 2 == 0: # if even, change to odd
                start_search = start_search + 1
            for n in range(start_search, 2, -2): # search each odd number below to see if divisor 
                if current_number % n == 0: 
                    prime_flag = False
                    pass
        
        if prime_flag: # if prime, add to list
            prime_list.append(current_number)
        
        current_number += 1
        
    return prime_list
