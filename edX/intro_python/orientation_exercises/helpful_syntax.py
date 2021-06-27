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

import io 
import sys

# STRING MANIPULATION
# -------------------
my_string = 'isaac'

# get every second letter from start to finish
my_string[0::2]

# get every third letter from start to letter 4
my_string[0:4:3]

# reverse the string (i.e. get every letter start to finish backwards)
my_string[::-1]


# ASSIGNMENT
# -------------------
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

# TUPLES
# -------------------
    
# Tricky tuple items
x = (1, 2 , (3, 'John' ,  4), 'Hi')
x[-1][-1] # second index is within string
x[0:-1] # this is the same as 0:len(x)-1
x[0:len(x)-1]
x[0] = 8

# MAP
# -------------------

# Map
my_list = []
nums = [1,2,3,4,-5]
for num in map(abs, nums):
    my_list.append(num)
    
list1 = [1,2,3,4,5]
list2 = [10,25,0,3]
for smaller_num in map(min, list1, list2):
    print(smaller_num)

# DICTIONARIES
# -------------------

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
 
# CLASSES AND OOP
# -------------------

# PROPERTIES
# Properties for class definitions 
# Helpful additional resource is here: https://www.python-course.eu/python3_properties.php
# Useful if you want to QA input
class SpeakerSettings(object):
    def __init__(self, volume, bass, treble):
        self.volume = volume
        self.bass = bass
        self.treble = treble

    # this property caps the maximum allowable volume when you make a new SpeakerSettings object
    @property
    def volume(self):
        if self.__volume > 100:
            return 100
        return self.__volume

    # the setter method for volume similarly checks for volumes over 100 or under 0 and alters values accordingly. 
    @volume.setter
    def volume(self, volume):
        if volume > 100:
            self.__volume = 100
        elif volume <= 0:
            self.__volume = 0
        else:
            self.__volume = volume
            
            
    def __str__(self):
        return 'Sound settings are: \n - Volume: %i \n - Bass: %i \n - Treble: %i'%(self.volume, self.bass, self.treble)
    
# INHERITANCE
# Limited form of multiple inheritance in python
# "Parents give the DNA (attributes), children decide the activities (methods)"

# I.e., when evaluating a class definition that calls parent classes / superclasses, the init methods run in order (for class D here, first does Cs init, then does Bs init, which itself runs As init). Thus, the lowest subclass gets the highest level attribute connected by init calls. 

# By contrast, with methods, the lowest subclass gets the closest version of that method. If it has one defined for it, it uses that one. If not, looks one class up, if not there, another class up etc. etc. 

class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

obj = D()
assert str(obj.a) == '2', 'should print 2 but prints%s'%str(obj.a) # should print 2. Why? First calls C.__init__, which would set a to 4, then calls B.__init__ which calls A.__init__ which would set a to 1, but then the B.__init__ sets a to 2, which is what it prints

# Interesting workaround here for testing string  output. Based on https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print 
def test_method(method_to_test, object_instance): 
    ''' tests the print output from object_instance.method_to_test'''
    capturedOutput = io.StringIO() # Create StringIO obj
    sys.stdout = capturedOutput # redirect stdout
    if method_to_test == 'x':
        obj.x() # call function
    elif method_to_test == 'y':
        obj.y()
    else:
        raise Exception('attempting to test a method that has not been built into test_x logic. Please add and try again')
    sys.stdout = sys.__stdout__ # reset redirect
    print('Captured', capturedOutput.getvalue())
    return capturedOutput.getvalue() # return capturedOutput

assert test_method('x', obj) == 'A.x\n', 'Expected obj.x() to return A.x, but returned %s'%test_method('x', obj)

# ^This prints A.x because the only x() function is in the highest superclass linked by B

assert test_method('y', obj) == 'C.y\n', 'Expected obj.y() to return C.y, but returned %s'%test_method('y', obj)

# ^ this prints C.y because the C class gets initialized first, and that has the y method, so will use the first method it finds, i.e. C.

# CLASS VARIABLES

class Animal(object):
    
    def __init__(self, name, age, animal_type):
        self.age = age 
        self.name = name
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def __str__(self):
        return str('%s is a %i year old %s')%(self.name, self.age, self.animal_type)
    
class Rabbit(Animal):
    tag = 1 # Tag is used to give a unique ID to each new rabbit instance
    def __init__(self, age, name = '', parent1 = None, parent2 = None):
        Animal.__init__(self, age, name, 'Rabbit')
        self.parent1 = parent1
        self.parent2 = parent2 
        self.rid = Rabbit.tag
        Rabbit.tag += 1

# Range
# ------------------
# This outputs a single iteration. [start,stop)
for i in range(0,1):
    print(i)
    
    