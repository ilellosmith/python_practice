#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:11:26 2021

@author: isaaclello-smith
"""
from hand import *
import unittest 

# -----------------------------------------
#
# Test Class Hand
#
# -----------------------------------------
        
class Test__init__(unittest.TestCase):
        
    def test_init_attributes(self):
        '''
        Test that init assigns attributes
        '''
        hand1 = Hand(9)
        self.assertEqual(hand1.HAND_SIZE, 9)
        
        hand1.setDummyHand('mystrings') 
        self.assertEqual(hand1.hand, {'m':1, 'y':1, 's':2, 't':1, 'r':1, 'i':1, 'n':1, 'g':1})
        
class Test__str__(unittest.TestCase):

    def test__str__returns_string(self):
        '''
        Test that __str__ method returns string
        '''
        hand1 = Hand(2)
        self.assertIsInstance(hand1.__str__(), str)
        
class Test_calculateLen(unittest.TestCase):

    def test_calculateLen(self):
        '''
        Test that calculateLen returns correct length
        '''
        hand1 = Hand(23)
        self.assertEqual(hand1.calculateLen(),23)
        
class Test_update(unittest.TestCase):

    def test_update(self):
        '''
        Test update removes letters
        '''
        hand1 = Hand(12)
        hand1.setDummyHand('isaacsstring')
        self.assertEqual(hand1.update('isaac'), True, 'did not return True after updating hand')
        self.assertEqual(hand1.hand, {'a':0, 'c':0,'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}, 'failed to produce dictionary with correct letters removed')
        
        '''
        Test update handles empty hand
        '''
        hand2 = Hand(0)
        self.assertEqual(hand2.update('isaac'), False, 'did not handle empty hand correctly')
        
        '''
        Test update handles empty input 
        '''
        hand3 = Hand(4)
        self.assertEqual(hand3.update(''),False, 'did not return False for empty word string')
        
        '''
        Test update handles letters not in hand
        '''
        hand4 = Hand(4)
        hand4.setDummyHand('test')
        self.assertEqual(hand4.update('zz'),False, 'did not return False for letters not in hand')
        
        '''
        Test update handles too few letters in hand
        '''
        hand5 = Hand(4)
        hand5.setDummyHand('test')
        self.assertEqual(hand5.update('ttt'),False, 'did not return False for too few of letter that is in word')
        
if __name__ == '__main__':
    unittest.main()