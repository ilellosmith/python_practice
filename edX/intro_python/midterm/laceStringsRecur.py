#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:39:14 2021

@author: isaaclello-smith
"""

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[0] + s2[0] + helpLaceStrings(s1[1:],s2[1:], out)
    return helpLaceStrings(s1, s2, '')

# test cases
s1 = 'abc'
s2 = 'def'

assert laceStringsRecur(s1,s2) == 'adbecf', 'should be adbecf with string 1 = abc and string 2 = def'

#assert laceStringsRecur(s1,s2) == 'aecf', 'this test should fail'

s3 = 'aaaaa'
s4 = 'zyx'

assert laceStringsRecur(s3,s4) == 'azayaxaa', 'should be azayaxaa with string 1 = %s and string 2 = %s'%(s3,s4)
