#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:55:27 2021

@author: isaaclello-smith
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # check if string is empty 
    if aStr == '':
        return False
    
    # base case 1
    if len(aStr) == 1:
        print('reached base case 1: single letter')
        return char == aStr
    
    # get midpoint position
    midPoint = int(len(aStr)/2)
    midChar = aStr[midPoint]
    
    # base case 2
    if midChar == char :
        print('reached base case 2: mid point is char')
        return True
    
    # recursive call 
    # if char to left 
    if char < midChar:
        return isIn(char, aStr[0:midPoint])
    else:
        return isIn(char, aStr[midPoint:])
        
# Test cases
# Base case - one letter
assert(isIn('a', 'a') == True)

# Base case - center letter is it 
assert(isIn('c', 'abcde') == True)

# Letter not in string 
assert(isIn('c', 'abde') == False)

# long string 
assert(isIn('r', 'abcdejkoprst') == True)

# empty string
assert(isIn('r', '') == False)

