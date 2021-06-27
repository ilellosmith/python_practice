#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:43:57 2021

@author: isaaclello-smith
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    
    vowels = ['a', 'e', 'i', 'o', 'u', 
              'A', 'E', 'I', 'O', 'U']
    
    new_string = ''
    # iterate over string 
    # if not vowel, append to new string
    for char in s: 
        if char not in vowels:
            new_string += char
    print(new_string)
    
   
