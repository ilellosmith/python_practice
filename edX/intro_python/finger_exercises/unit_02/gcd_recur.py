#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:43:36 2021

@author: isaaclello-smith
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    # base case
    if b == 0:
        return a
    
    # recursive call
    return gcdRecur(b, a % b)