#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:28:20 2021

@author: isaaclello-smith
"""

def count7(N):
    '''
    Returns number of occurences of digit 7 in N
    
    N: a non-negative integer
    Returns: integer count of occurences of 7 in N
    '''
    # Your code here
    
    # base case: N is less than 10
    if N % 10 == N:
        if N == 7:
            return 1
        else:
            return 0 
        
    # Otherwise check rightmost, 
    # remove and call
    if N % 10 == 7:
        return 1 + count7(N // 10)
    else: 
        return 0 + count7(N // 10)




assert count7(0) == 0, 'should be 0'

assert count7(7777) == 4, 'should be 7'

assert count7(712734756) == 3, 'should be 3'

# assert count7(7237) == 3, 'this test should fail'

assert count7(717) == 2, 'should be 2'

assert count7(1237123) == 1, 'should be 1'

assert count7(8989) == 0, 'should be 0'
