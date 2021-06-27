#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:35:34 2021

@author: isaaclello-smith
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:21:13 2021

@author: isaaclello-smith
"""

import unittest 
from uniqueValues import uniqueValues

# -----------------------------------------
#
# Test uniqueValues
#
# -----------------------------------------

class test_uniqueValues(unittest.TestCase):

    def test_empty(self):
        '''
        Test empty dict returns empty list
        '''
        self.assertEqual(uniqueValues({}), [])
        
    def test_no_unique(self):
        '''
        Test case of no uniques
        '''
        self.assertEqual(uniqueValues({1: 1, 2: 1, 3: 1}), [])
        
    def test_some_unique(self):
        '''
        Test case of some uniques
        '''
        self.assertEqual(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}), [1,3,8])

if __name__ == '__main__':
    unittest.main()