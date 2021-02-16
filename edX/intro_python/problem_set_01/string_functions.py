#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:55:42 2021

@author: isaaclello-smith
"""

"""
Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
"""

def count_vowels(s):
    '''takes a string and returns the number of vowels in the string'''

    s = s.lower()
    vowel_count = 0

    for letter in s:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            vowel_count += 1
            
    return vowel_count

# Test function ----

print('\n\nProblem 1:\n')
# test example from EdX
s = 'azcbobobegghakl'
assert count_vowels(s) == 5, 'Should be 5 with string %s'%s
print('Number of vowels: %i'%count_vowels(s))

# test no vowels
s_no_vowel = 'ths strng hs n vwls'
assert count_vowels(s_no_vowel) == 0, 'Should be 0 with string %s'%s_no_vowel

# test all vowels
s_all_vowel = 'iiaoeiuuia'
assert count_vowels(s_all_vowel) == len(s_all_vowel), 'Should be 10 with string %s'%s_all_vowel

# test empty string
s_empty = ''
assert count_vowels(s_empty) == 0, 'Should be 0 with empty string %s'%s_empty

# test capital vowels
s_caps = 'AeiOulmao'
assert count_vowels(s_caps) == 7, 'Should be 7 with string %s'%s_caps

# test spaces 
s_space = 'this string has spaces'
assert count_vowels(s_space) == 5, 'Should be 5 with string %s'%s_space

# Remove function wrapper and test ---- 
s = s.lower()
vowel_count = 0

for letter in s:
    if letter in ('a', 'e', 'i', 'o', 'u'):
        vowel_count += 1
print('Number of vowels: %i'%vowel_count)


"""
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
"""

def count_bobs(s):
    '''takes a string and returns the number of bob instances in the string'''
    bob_count = 0 
    # move through string, ending a bob length from finish
    for i in range(len(s)-2):
        # if passes bob check, add to count
        if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
            bob_count += 1 
    return bob_count

# Test function ----
print('\n\nProblem 2:\n')

# test partial bob
s_part = 'bo b bo'
assert count_bobs(s_part) == 0, 'Should be 0 with string %s'%s_part

# test repeat bob
s_rep = 'bobobobsomeotherstringbob'
assert count_bobs(s_rep) == 4, 'Should be 4 with string %s'%s_rep

# test end bob
s_end = 'adbob'
assert count_bobs(s_end) == 1, 'Should be 1 with string %s'%s_end

# test empty string bob
s_empty = ''
assert count_bobs(s_empty) == 0, 'Should be 0 with empty string %s'%s_empty

# test extra b
s_b = 'bbbob'
assert count_bobs(s_b) == 1, 'Should be 1 with string %s'%s_b

# Remove function wrapper and test ---- 
s = 'azcbobobegghakl'

bob_count = 0 
# move through string, ending a bob length from finish
for i in range(len(s)-2):
    # if passes bob check, add to count
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        bob_count += 1 
print('Number of times bob occurs is: %i'%bob_count)


"""
Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
"""

def get_longest_alphabetical_substring(s):
    '''takes a string and returns the longest alphabetical
    substring. In case of tie, returns first string'''
    longest_alphabetical_string = ''
    i = 0
    while i < len(s)-1:
        # start a new string
        current_string = s[i]
        # if blank, keep moving
        if s[i] == ' ':
            i +=1
        # while in alphabetical order, add to current string
        while i < len(s)-1 and s[i] <= s[i+1]:
            current_string = current_string+s[i+1]
            i += 1
        # once current string ends, compare
        if len(longest_alphabetical_string) < len(current_string):
                longest_alphabetical_string = current_string
        # increment to start new string
        i += 1
    return longest_alphabetical_string 

# Test function ----
print('\n\nProblem 3:\n')

# test EdX's example
s = 'azcbobobegghakl'
assert get_longest_alphabetical_substring(s) == 'beggh', 'Should be beggh with string %s'%s

# test tie
s_tie = 'abcbcd'
assert get_longest_alphabetical_substring(s_tie) == 'abc', 'Should be abc with string %s'%s_tie

# test one letter string for index
s_single = 'a'
assert get_longest_alphabetical_substring(s_single) == '', 'Should be a with string %s'%s_single

# test empty string 
s_empty = ''
assert get_longest_alphabetical_substring(s_empty) == '', 'Should be '' with string %s'%s_empty

# test string with spaces 
s_space = 'abc def rtf hij'
assert get_longest_alphabetical_substring(s_space) == 'abc', 'Should be abc with string %s'%s_space

# test numbers

# Remove function wrapper and test ---- 
s = 'azcbobobegghakl'
# s = 'abcbcd'

# Initialize vars for search
longest_alphabetical_string = ''
i = 0
while i < len(s)-1:
    # start a new string
    current_string = s[i]
    # exclude if blank
    if s[i] == ' ':
        i +=1
    # while in alphabetical order, add to current string
    while i < len(s)-1 and s[i] <= s[i+1]:
        current_string = current_string+s[i+1]
        i += 1
    # once current string ends, compare
    if len(longest_alphabetical_string) < len(current_string):
            longest_alphabetical_string = current_string
    # increment to start new string
    i += 1
    
print('Longest substring in alphabetical order is: %s'%longest_alphabetical_string)