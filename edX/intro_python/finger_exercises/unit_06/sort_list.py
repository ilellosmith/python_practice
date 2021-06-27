#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:37:36 2021

@author: isaaclello-smith
"""

# These should be equivalent efficiency-wise except for swapping the for and while loop
# both would be O(n^2)

def mySort(L):
    """ L, list with unique elements """
    clear = False
    iter_outer = 0
    iter_inner = 0
    while not clear:
        iter_outer += 1
        clear = True
        for j in range(1, len(L)):
            iter_inner += 1
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return(L, iter_outer, iter_inner)
                
L1 = [0,7,2,1]
L2 = []
print(mySort(L1))
print(mySort(L2))

def newSort(L):
    """ L, list with unique elements """
    iter_outer = 0
    iter_inner = 0
    for i in range(len(L) - 1):
        iter_outer += 1
        j=i+1
        while j < len(L):
            iter_inner += 1
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
    return(L, iter_outer, iter_inner)

L3 = [0,7,2,1]
L4 = []    
print(newSort(L3))
print(newSort(L4))