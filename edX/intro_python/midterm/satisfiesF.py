#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:52:49 2021

@author: isaaclello-smith
"""

def satisfiesFTest(L, mysteryString):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    
    # removing all strings in list 
    # that don't match a mystery string in f
    # and returning the length of L after these 
    # strings are removed. And actually modifying 
    # L s.t. at the end, we have just that string remaining in L and in order? 
        
    # tricky though bc you don't want to mutate a list
    # you're iterating over 
    
    def f(s):
        return mysteryString in s
    
    # move through L 
    # check if each element satisfies F
    # if it does, leave it
    # if it doesn't, remove it
    
    # build a list of elements of L that satisfy F    
    satisfyF = []
    
    for i in range(len(L)): 
        print('working on: %s'%L[i])
        if f(L[i]): 
            satisfyF.append(L[i])
    
    # replace elements in L to match satisfyF
    L.clear() 
    for i in range(len(satisfyF)):
        L.append(satisfyF[i])
    print(L)
    
    return len(L)

# test cases
L = ['here', 'are', 'some', 'strings']

assert satisfiesFTest(L, 'r') == 3, 'should return length 3'
assert L == ['here', 'are', 'strings'], 'L should have three words'

L2 = ['my', 'test', 'strings'] 
assert satisfiesFTest(L2, 'my') == 1, 'should return length 1'

assert L2 == ['my'], 'List should have one word'

L3 = ['a', 'b', 'a']

assert satisfiesFTest(L3, 'a') == 2, 'should return 2'

assert L3 == ['a', 'a'], 'should return double a'


# submit the below version

# def satisfiesF(L):
#     """
#     Assumes L is a list of strings
#     Assume function f is already defined for you and it maps a string to a Boolean
#     Mutates L such that it contains all of the strings, s, originally in L such
#             that f(s) returns True, and no other elements. Remaining elements in L
#             should be in the same order.
#     Returns the length of L after mutation
#     """
#     # Your function implementation here
    
#     # build a list of elements of L that satisfy F    
#     satisfyF = []
    
#     for i in range(len(L)): 
#         if f(L[i]): 
#             satisfyF.append(L[i])
    
#     # replace elements in L to match satisfyF
#     L.clear() 
#     for i in range(len(satisfyF)):
#         L.append(satisfyF[i])
    
#     return len(L)

# run_satisfiesF(L, satisfiesF)