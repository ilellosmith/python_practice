#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:04:28 2021

@author: isaaclello-smith
"""
import timeit

# Checking big O of modulus
print(timeit.timeit(stmt = '10%10', number = 10000))
print(timeit.timeit(stmt = '10000000000000000000000000000%10', number = 10000))


# Testing search functions

e = 6
e2 = 0
e3 = 1
e4 = 5
sorted0 = []
sorted1 = [0]
sorted2 = [0,1]
sorted2b = [1,0]
sorted1b = [1]
sorted5 = [0,1,2,3,4,5]

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

def newSearchCorrect(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[size-i-1] < e:
            return False
    return False

# Test element not in list
assert search(sorted0,e) == newsearch(sorted0,e), 'returned diff results for empty list, absent element'

assert search(sorted5,e) == newsearch(sorted5,e), 'returned diff results for list of length %i, absent element'%len(sorted5)

assert search(sorted1,e) == newsearch(sorted1,e), 'returned diff results for list of length %i, absent element'%len(sorted1)

assert search(sorted2,e) == newsearch(sorted2,e), 'returned diff results for list of length %i, absent element'%len(sorted2)

# Test element in list, left element
assert search(sorted0,e2) == newsearch(sorted0,e2), 'returned diff results for empty list, absent element'

assert search(sorted5,e2) == newsearch(sorted5,e2), 'returned diff results for list of length %i, leftmost element'%len(sorted5)

assert search(sorted1,e2) == newsearch(sorted1,e2), 'returned diff results for list of length %i, leftmost element'%len(sorted1)

assert search(sorted2,e2) == newsearch(sorted2,e2), 'returned diff results for list of length %i, leftmost element'%len(sorted2)

# Test element in list, middle element
assert search(sorted0,e3) == newsearch(sorted0,e3), 'returned diff results for empty list, absent element'

# assert search(sorted5,e3) == newsearch(sorted5,e3), 'returned diff results for list of length %i, element in middle'%len(sorted5)

assert search(sorted1,e3) == newsearch(sorted1,e3), 'returned diff results for list of length %i, absent element'%len(sorted1)

assert search(sorted2,e3) == newsearch(sorted2,e3), 'returned diff results for list of length %i, rightmost element'%len(sorted2)

# It's an index issue 
# Test element in list, first element
assert search(sorted1b,e3) == newsearch(sorted1b,e3), 'returned diff results for list of length %i, absent element'%len(sorted1b)

assert search(sorted2b,e3) == newsearch(sorted2b,e3), 'returned diff results for list of length %i, rightmost element'%len(sorted2b)

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
    
def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)