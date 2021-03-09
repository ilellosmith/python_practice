#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:49:53 2021

@author: isaaclello-smith
"""

def dotProduct(listA, listB):
    '''
    Returns the dot product of two lists of integers
    
    Parameters:
        listA: a list of numbers
        listB: a list of numbers of the same length as listA
    
    Returns:
        the dot product, an integer
    '''
    # Your code here
    
    def multiply(x,y):
        '''
        Parameters:
            x : int
            y : int
        
        Returns:
            x * y: int 
        '''
        return x * y
    
    return sum(map(multiply, listA, listB))
    
listA = [1,2,3]
listB = [4,5,6]
listC = [0,0,0]
listD = [1,0,0]
listE = [0,1,0]
listF = [0,0,1]

assert dotProduct(listA, listB) == 32, 'should be 32'    

assert dotProduct(listA, listC) == 0, 'should be 0'

#assert dotProduct(listA, listC) == 1, 'this should fail'

assert dotProduct(listA, listD) == 1, 'should be 1'    

assert dotProduct(listA, listE) == 2, 'should be 2'

assert dotProduct(listA, listF) == 3, 'should be 3'  