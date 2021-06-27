#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:40:13 2021

@author: isaaclello-smith
"""

import unittest 
from MITCampus import Location, Campus, MITCampus

# -----------------------------------------
#
# Test add_tent
#
# -----------------------------------------

class test_add_tent(unittest.TestCase):

    def test_add_valid(self):
        '''
        Test adding valid tent returns true and it's in tents
        '''
        campus_center = Location(0,0)
        tent_location = Location(1,1)
        test_campus = MITCampus(campus_center, tent_location)
        
        self.assertEqual(test_campus.add_tent(Location(2,2)), True)
        self.assertEqual(test_campus.tents[1], Location(2,2))
        
    def test_add_too_close(self):
        '''
        Test adding valid tent returns False and is not in tents afterwards
        '''
        campus_center = Location(0,0)
        tent_location = Location(1,1)
        test_campus = MITCampus(campus_center, tent_location)
        
        self.assertEqual(test_campus.add_tent(Location(1,1.22)), False)
        
        try:
            test_campus.tents[1]
        except IndexError:
            'New tent correctly does not exist'
        
class test_remove_tent(unittest.TestCase):

    def test_remove_valid(self):
        '''
        Test removing valid tent returns True and its no longer in tents
        '''
        campus_center = Location(0,0)
        tent_location = Location(1,1)
        test_campus = MITCampus(campus_center, tent_location)
        
        test_campus.remove_tent(Location(1,1))
        self.assertEqual(len(test_campus.tents), 0)        
        
    def test_remove_missing(self):
        '''
        Test removing missing tent returns False
        '''
        campus_center = Location(0,0)
        tent_location = Location(1,1)
        test_campus = MITCampus(campus_center, tent_location)
        
        self.assertRaises(ValueError, test_campus.remove_tent, Location(1,0))            
        
class test_get_tents(unittest.TestCase):

    def test_empty(self):
        '''
        Test get tents returns empty for empty
        '''
        campus_center = Location(0,0)
        tent_location = Location(1,1)
        test_campus = MITCampus(campus_center, tent_location)
        
        test_campus.remove_tent(Location(1,1))
        self.assertEqual(test_campus.get_tents(), [])   
        
    def test_len_1(self):
        '''
        Test get tents returns single item for single tent campus
        '''
        campus_center = Location(0,0)
        tent_location = Location(1,1)
        test_campus = MITCampus(campus_center, tent_location)
        
        self.assertEqual(test_campus.get_tents(), ['<1,1>'])
        
    def test_longer_list(self):

        '''
        Test longer list of tents sorted properly
        '''
        campus_center = Location(0,0)
        tent_location = Location(1,1)
        test_campus = MITCampus(campus_center, tent_location)
        
        test_campus.add_tent(Location(0,10))
        test_campus.add_tent(Location(10,10))
        test_campus.add_tent(Location(3,1))

        self.assertEqual(test_campus.get_tents(), ['<0,10>', '<1,1>', '<3,1>', '<10,10>'])
        
    def test_already_ordered(self):

        '''
        Test pre-ordered list stays in correct order
        '''
        campus_center = Location(0,0)
        tent_location = Location(1,1)
        test_campus = MITCampus(campus_center, tent_location)
        
        test_campus.add_tent(Location(2,1))
        test_campus.add_tent(Location(3,1))

        self.assertEqual(test_campus.get_tents(), ['<1,1>', '<2,1>', '<3,1>'])
        
class edx_tests(unittest.TestCase):
    
    def test_edx_tests(self):
        c = MITCampus(Location(1,2))
        self.assertEqual(c.add_tent(Location(2,3)), True)
        self.assertEqual(c.add_tent(Location(1,2)), True)
        self.assertEqual(c.add_tent(Location(0,0)), False)
        self.assertEqual(c.add_tent(Location(2,3)), False)
        self.assertEqual(c.get_tents(), ['<0,0>', '<1,2>', '<2,3>'])
        

if __name__ == '__main__':
    unittest.main()

