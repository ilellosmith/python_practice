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
