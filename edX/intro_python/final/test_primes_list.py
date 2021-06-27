#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:21:13 2021

@author: isaaclello-smith
"""


import unittest 
from primes_list import primes_list

# -----------------------------------------
#
# Test primes_list
#
# -----------------------------------------

class testPrimesList(unittest.TestCase):

    def test_2(self):
        '''
        Test primes_list handles case of 2
        '''
        self.assertEqual(primes_list(2), [2])
        
    def test_even(self):
        '''
        Test primes_list handles even numbers other than 2
        '''
        self.assertEqual(primes_list(6),[2,3,5])
        
    def test_sqrt(self):

        '''
        Test primes_list sqrt logic works
        '''
        self.assertEqual(primes_list(25),[2,3,5,7,11,13,17,19,23])

if __name__ == '__main__':
    unittest.main()