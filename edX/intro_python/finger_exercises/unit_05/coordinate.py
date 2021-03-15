#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:33:02 2021

@author: isaaclello-smith
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()
        
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' +  str(self.getY()) + ')'
        

# Test 
myCoord = Coordinate(1,2)
origin = Coordinate(0,0)
otherCoord = Coordinate(1,2)

# Check repr method returns expected string
assert repr(myCoord) == 'Coordinate(1,2)', 'Returned %s, should have returned Coordinate(1,2)'

# Check eq method with different coordinates
assert not myCoord == origin, 'Returned true when comparing '+ str(myCoord) + ' and ' + str(origin) + '. Should have returned False' 

# Check eq method with same coordinates
assert myCoord == otherCoord, 'Returned true when comparing '+ str(myCoord) + ' and ' + str(otherCoord) + '. Should have returned False'