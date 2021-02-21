#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:09:12 2021

@author: isaaclello-smith
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    total_values = 0
    # count items in each list
    for list in aDict.keys():
        total_values += len(aDict[list])
        
    return total_values


# Test 
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

assert how_many(animals) == 6, 'Should return 6 total values'


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    
    if len(aDict) == 0:
        return None
    
    # Your Code Here
    list_lengths = {}
    # Record lengths in new dictionary
    for list in aDict.keys():
        list_lengths[list] = len(aDict[list])
    longest_list_len = max(list_lengths.values())
    # Find key with longest list length
    for list in list_lengths.keys():
        if list_lengths[list] == longest_list_len:
            longest_list_key = list
    
    return longest_list_key
            
zero_len = []
list_a = [1,2,3,4,5,6,7,8,9,10]
list_b = ['some', 'strings', 'in', 'list', 'and', 'one', 'integer', 10]
list_c = [9, 3, 10]
list_d = [10, 11, 12, 13, 14, 15, 16, ['recursion', 'for', 'nested', 'lists?']]

myDict = {
    'zero': zero_len, 
    'A': list_a,
    'B': list_b,
    'C': list_c
    } 

myDictNested = {
    'zero': zero_len, 
    'A': list_a,
    'B': list_b,
    'C': list_c,
    'D': list_d
    } 

emptyDict = {
    }

# Basic Case
assert biggest(myDict) == 'A', 'Identified wrong longest list, should be list_a'

# emptyDict
assert biggest(emptyDict) == None, 'Should return None'

# work for nested? 
assert biggest(myDictNested) == 'D', 'Identified wrong longest list, should be list_d'

