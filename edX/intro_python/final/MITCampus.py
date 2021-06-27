#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:01:08 2021

@author: isaaclello-smith
"""

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
    
class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        
        Campus.__init__(self, center_loc)
        self.tents = []
        self.tents.append(tent_loc)
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """

        all_tents = self.tents[:]
        for tent in all_tents:
            if new_tent_loc.dist_from(tent) < 0.5:
                return False

        self.tents.append(new_tent_loc)
        return True
        
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        tent_found = False
        
        for tent in self.tents[:]:
            if tent_loc.__eq__(tent):
                tent_found = True
                self.tents.remove(tent)
        
        if not tent_found: 
            raise ValueError('Tent at location %s does not exist'%(tent_loc.__str__()))
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        
        all_tents = self.tents[:]
        
        if len(all_tents) == 0:
            return []
        elif len(all_tents) == 1:
            return [all_tents[0].__str__()]
        else:
            i = 0
            while i < len(all_tents): # iterate over all values from i up 
                for j in range(i,len(all_tents)):
                    if all_tents[i].getX() > all_tents[j].getX(): # if i > j, swap
                        temp = all_tents[j]
                        all_tents[j] = all_tents[i]
                        all_tents[i] = temp
                i += 1
        
        coord_out = []
        for tent in all_tents: 
            coord_out.append(tent.__str__())
            
        return coord_out
            