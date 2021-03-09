#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:02:36 2021

@author: isaaclello-smith
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    
    # get values to become keys
    new_keys = d.values()
    # initialize new dictionary for inverted dict
    inverted_dict = {}

    # work one new_key at a time
    for new_key in new_keys:
        # Check old dictionary for new_key as value
        new_value = []
        for old_key in d:
            if d[old_key] == new_key:
                # add old key to list of values for new_key
                new_value.append(old_key)
        # sort and add to inverted dictionary
        inverted_dict[new_key] = sorted(new_value)
                
    return inverted_dict   
        
# working one new_key at a time, 
    # move through d, checking if new_key 
    # is a value for each of the old_keys
    # if so, add it to the list that is the value 
    # for new_key. At the end sort


# Test cases 
    
initial1 = {1:10, 2:20, 3:30} 
inverted1 = {10: [1], 20: [2], 30: [3]}

initial2 = {1:10, 2:20, 3:30, 4:30} 
inverted2 = {10: [1], 20: [2], 30: [3, 4]}

initial3 = {4:True, 2:True, 0:True}
inverted3 = {True: [0, 2, 4]}

assert dict_invert(initial1) == inverted1, 'does not match test outcome 1'

assert dict_invert(initial2) == inverted2, 'does not match test outcome 2'

assert dict_invert(initial3) == inverted3, 'does not match test outcome 3'

#assert dict_invert(initial3) == 20, 'this test should fail'