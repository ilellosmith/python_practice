#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:35:08 2021

@author: isaaclello-smith
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''    
    
    unique_keys = []
    
    # if empty dict, return empty list
    if len(aDict) == 0:
        return unique_keys
    
    # build a frequency dictionary for values in aDict 
    values = list(aDict.values())
    
    # for each value, count up frequency in values list
    freq_dict = {}
    values_copy = values[:] # copy of values to iterate over
    for search_value in values_copy:
        count = 0
        # count frequency
        for value in values: 
            if search_value == value:
                count += 1
        freq_dict.setdefault(count, []).append(search_value) # add to frequency dictionary
        values = [x for x in values if x != search_value] # remove all instances from dict if found
         
    # then, search for unique values in each key in aDict. If key is a unique value, add key to list of unique keys

    unique_values = freq_dict.get(1, [])
    
    for key in list(aDict.keys()):
        if aDict[key] in unique_values:
            unique_keys.append(key)
    
    unique_keys.sort()  
    return unique_keys



  # # create dict of value to key mapping 
  #   value_to_key_mapping = {}

    
  #   # iterate through keys, checking value against values already found
  #   # if not yet found, add
  #   # if found, remove
  #   keys = list(aDict.keys())
  #   values_found = []

  #   for key in keys: 
  #       if aDict[key] not in values_found:
  #           values_found.append(aDict[key])
  #       else:
  #           values_found.remove(aDict[key])
  #   # maintain a list of keys found
    