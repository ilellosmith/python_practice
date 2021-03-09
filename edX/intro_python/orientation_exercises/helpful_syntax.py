#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:14:05 2021

@author: isaaclello-smith
"""
# -*- coding: utf-8 -*-
"""
Created on 2021-02-01

@author: ILS
"""

# STRING MANIPULATION
my_string = 'isaac'

# get every second letter from start to finish
my_string[0::2]

# get every third letter from start to letter 4
my_string[0:4:3]

# reverse the string (i.e. get every letter start to finish backwards)
my_string[::-1]


# ASSIGNMENT
x = 1
y = 2

# swap values without an intermediate variable
x,y = y,x
print('x post swap: %i' % x)
print('y post swap: %i' % y)

# assign multiple values at once 
a,b,c = 1,2,3
print('a = %i, b = %i, c = %i' % (a,b,c))

# * gets anything that's left
d,e,*f = 1,'a name',50,60,70
print('d = %i, e = %s' % (d,e), ', f =', f)

# Concepts to review:
    # binary 
    # tuple 
    
# Tricky tuple items
x = (1, 2 , (3, 'John' ,  4), 'Hi')
x[-1][-1] # second index is within string
x[0:-1] # this is the same as 0:len(x)-1
x[0:len(x)-1]
x[0] = 8

# Map
my_list = []
nums = [1,2,3,4,-5]
for num in map(abs, nums):
    my_list.append(num)
    
list1 = [1,2,3,4,5]
list2 = [10,25,0,3]
for smaller_num in map(min, list1, list2):
    print(smaller_num)
    
# Dict
my_dict = {'some':1, 'dict':3, 4:'here'}
list(my_dict.values())
list(my_dict.keys())

# Get
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}    
try: 
    print("testing hand['e'] a key that does not exist in the dictionary:")
    hand['e']
except KeyError: 
    print('this throws a key error because e is not in the hand.')
    
print("testing hand.get('e',0) a key that does not exist in the dictionary, but with a function that returns a default value of 0:")
hand.get('e', 0)
print('this does not throw a key error because the function returns the specified default 0.')