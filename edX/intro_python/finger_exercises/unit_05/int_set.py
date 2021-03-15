#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:46:34 2021

@author: isaaclello-smith
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
            
    def intersect(self, other):
        """Assumes other is an intSet and returns a new intSet with elements in both self and other"""
        # check each element in self, add to new set if also in other set
        newSet = intSet()
        for i in self.vals:
            if other.member(i):
                newSet.insert(i)
        return newSet

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __len__(self):
        """Returns length of self as int"""
        return len(self.vals)
    
    
# Test
intSet1List = [1,2,3,4,5]
intSet1 = intSet()
for i in intSet1List:
    intSet1.insert(i)
    
intSet2List = [1,2,3,0,9]
intSet2 = intSet()
for i in intSet2List:
    intSet2.insert(i)
    
intSet3 = intSet()
intSet4 = intSet()

# Intersect 

# Check intersect with nonempty lists
assert str(intSet2.intersect(intSet1)) == '{1,2,3}', 'intersect method returned unexpected result ' + str(intSet2.intersect(intSet1)) + ' but expected {1,2,3}'

# Check intersect with one empty list
assert str(intSet2.intersect(intSet3)) == '{}', 'intersect method returned unexpected result ' + str(intSet2.intersect(intSet3)) + ' but expected {}'

# Check intersect with two empty lists
assert str(intSet4.intersect(intSet3)) == '{}', 'intersect method returned unexpected result ' + str(intSet4.intersect(intSet3)) + ' but expected {}'

# __len__ 
assert len(intSet4) == 0, 'len method returned %i but expected length 0'%len(intSet4)

assert len(intSet2) == 5, 'len method returned %i but expected length 5'%len(intSet2)