#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:44:34 2021

@author: isaaclello-smith
"""

import unittest 
import io 
import sys 
from print_without_vowels import print_without_vowels

# -----------------------------------------
#
# Test print_without_vowels
#
# -----------------------------------------

class testPrintWithoutVowels(unittest.TestCase):

    def test_print(self,str_to_test): 
        ''' tests the print output from a function'''
        capturedOutput = io.StringIO() # Create StringIO obj
        sys.stdout = capturedOutput # redirect stdout
        print_without_vowels(str_to_test)
        sys.stdout = sys.__stdout__ # reset redirect
        print('Captured', capturedOutput.getvalue())
        return capturedOutput.getvalue() # return capturedOutput    

    def test_print_without_vowels_empty_string(self):
        '''
        Test print_without_vowels handles empty string
        '''
        s = ''
        self.assertEqual(self.test_print(s),'\n')
        
    def test_print_without_vowels_all_vowels(self):
        '''
        Test print_without_vowels removes all vowels lower and upper case
        '''
        s = 'aAeEiIoOuU'
        self.assertEqual(self.test_print(s),'\n')
        
    def test_print_without_vowels_normal_phrase(self):

        '''
        Test print_without_vowels retains non-vowel chars
        '''
        s = 'Isaac\'s string to test!'
        self.assertEqual(self.test_print(s),'sc\'s strng t tst!\n')

if __name__ == '__main__':
    unittest.main()