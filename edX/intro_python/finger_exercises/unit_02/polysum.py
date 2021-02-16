#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:31:56 2021

@author: isaaclello-smith
"""

import math

def polysum(n, s):
    '''
    Calculate the polysum for a regular polygon.
    
    Input: 
        n (int) -- number of sides in the regular polygon
        s (int or float) -- length of each side
        
    Output: 
        polysum (float) -- the sum of the area and the square of the perimeter for the regular polygon
    '''
    
    area = (0.25*n*s**2) / math.tan(math.pi/n)
    perimeter_square = (n*s)**2
    return round(area + perimeter_square, 4)