#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:22:10 2021

@author: isaaclello-smith
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # for each value in exp, multiply by itself
    power = 1
    if exp == 0:
        return power
    while exp > 0:
        power *= base
        exp -= 1
    return power