#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:30:30 2021

@author: isaaclello-smith
"""
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    
    # base case
    if exp == 0:
        return 1
    # recursive call
    else:
        return base * recurPower(base, exp-1)