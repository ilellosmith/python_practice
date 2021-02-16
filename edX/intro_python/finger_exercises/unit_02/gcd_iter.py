#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:56:17 2021

@author: isaaclello-smith
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # identify larger and smaller values
    smaller = min(a,b)
    larger = max(a,b)
    test = smaller
    
    # decrement until you find the gcd
    while larger%test != 0 or smaller%test != 0:
        print('test is: %i'%test)
        test -= 1 
    
    return test
  
    