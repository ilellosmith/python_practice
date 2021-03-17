#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:49:46 2021

@author: isaaclello-smith
"""

import unittest 

from ps6 import Message
from ps6 import PlaintextMessage
from ps6 import CiphertextMessage

# -----------------------------------------
#
# Test Class Message
#
# -----------------------------------------

class TestBuildShiftDict(unittest.TestCase):

    def test_build_shift_dict_wrap_around(self):
        '''
        Test that build dict shifts lower case properly
        '''
        message1 = Message('isaacz')
        result = message1.build_shift_dict(1)
        self.assertEqual(result['a'],'b')
        self.assertEqual(result['z'], 'a')
        
    def test_build_shift_dict_caps(self):
        '''
        Test that build dict shifts upper case properly
        '''
        message1 = Message('isaacz')
        result = message1.build_shift_dict(1)
        self.assertEqual(result['A'],'B')
        self.assertEqual(result['Z'], 'A')
        
    def test_build_shift_dict_special(self):
        '''
        Test that build dict doesn't shift non-letters
        '''
        message1 = Message('isaacz')
        result = message1.build_shift_dict(1)
        self.assertEqual(result.get(' ', 0),0)
        self.assertEqual(result.get(',', 0),0)


class TestApplyShift(unittest.TestCase):

    def test_apply_shift_wrap_around(self):
        '''
        Test that shift wraps around alphabet properly
        '''
        message1 = Message('isaacz')
        result = message1.apply_shift(1)
        self.assertEqual(result,'jtbbda')
        
    def test_apply_shift_caps(self):
        '''
        Test that shift handles retains casing properly
        '''
        message1 = Message('IsaAcz')
        result = message1.apply_shift(1)
        self.assertEqual(result,'JtbBda')
        
    def test_apply_shift_special(self):
        '''
        Test that shift retains special characters
        '''
        message1 = Message('is,a ac.z')
        result = message1.apply_shift(1)
        self.assertEqual(result,'jt,b bd.a')
       
# -----------------------------------------
#
# Test Class PlaintextMessage
#
# -----------------------------------------
        
class Test__init__(unittest.TestCase):

    def test_init_subclass(self):
        '''
        Test that init creates subclass
        '''
        message1 = PlaintextMessage('isaacz', 3)
        self.assertIsInstance(message1, PlaintextMessage)
        self.assertIsInstance(message1, Message)
        
    def test_init_attributes(self):
        '''
        Test that init assigns attributes
        '''
        message1 = PlaintextMessage('isaacz', 1)
        self.assertEqual(message1.get_message_text(),'isaacz')
        self.assertEqual(message1.get_message_text_encrypted(),'jtbbda')
        self.assertEqual(message1.get_shift(),1)
        
class Test_change_shift(unittest.TestCase):

    def test_change_shift_does_shift(self):
        '''
        Test that change_shift changes attributes
        '''
        message1 = PlaintextMessage('isaacz', 5)
        result = message1.change_shift(2)
        self.assertEqual(message1.get_message_text(),'isaacz')
        self.assertEqual(message1.get_shift(),2)
        self.assertEqual(message1.get_message_text_encrypted(),'kucceb')
        
    def test_change_shift_updates_object(self):
        '''
        Test that change_shift modifies object
        '''
        message1 = PlaintextMessage('isaacz', 1)
        pointer_to_message1 = message1
        message1.change_shift(5)
        self.assertIs(message1, pointer_to_message1)


# -----------------------------------------
#
# Test Class CiphertextMessage
#
# -----------------------------------------
        
class Test__init__(unittest.TestCase):

    def test_init_subclass(self):
        '''
        Test that init creates subclass
        '''
        message1 = CiphertextMessage('isaacz')
        self.assertIsInstance(message1, CiphertextMessage)
        self.assertIsInstance(message1, Message)
        
    def test_init_attributes(self):
        '''
        Test that init assigns attributes
        '''
        message1 = CiphertextMessage('isaacz')
        self.assertEqual(message1.get_message_text(),'isaacz')
        
class Test_decrypt_message(unittest.TestCase):

    def test_decrypt_message_returns_tuple(self):
        '''
        Test that decrypt_message returns a tuple
        '''
        message1 = CiphertextMessage('hi there')
        result = message1.decrypt_message()
        self.assertIsInstance(result, tuple)
       
    def test_decrypt_message_returns_shift(self):
        '''
        Test that decrypt_message returns correct values
        '''
        cipher1 = PlaintextMessage('hi there', 10)
        ciphertext1 = CiphertextMessage(cipher1.get_message_text_encrypted())
        decipher1 = ciphertext1.decrypt_message()
        self.assertEqual(decipher1[0], 16)
        self.assertEqual(decipher1[1], 'hi there')
        
    def test_decrypt_message_returns_shift(self):
        '''
        Test that decrypt_message handles already decrypted
        '''
        cipher1 = PlaintextMessage('hi there', 0)
        ciphertext1 = CiphertextMessage(cipher1.get_message_text_encrypted())
        decipher1 = ciphertext1.decrypt_message()
        self.assertEqual(decipher1[0], 26)
        self.assertEqual(decipher1[1], 'hi there')

if __name__ == '__main__':
    unittest.main()