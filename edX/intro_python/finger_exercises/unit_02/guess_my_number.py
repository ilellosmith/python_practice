#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:52:23 2021

@author: isaaclello-smith
"""

def guess_my_number():
    '''uses bisection search and user guidance of high, low or correct at each guess to identify a user determined number between 0 and 100'''
    
    print('Please think of a number between 0 and 100!', end = '\n')
    
    # initialize while loop vars
    status = ''
    high = 100
    low = 0
    guess = low+(high-low)/2
    
    while(status != 'c'):
        
        # Guess
        guess = int(low+((high-low)/2))
        
        # Check
        status = input("Is your secret number %i? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "%guess)
        
        # Verify input
        if status not in ['c', 'l', 'h']:
            print('Sorry, I did not understand your input.')
        # Update guess or finish 
        else: 
            if status == 'c':
                break
            elif status == 'h':
                high = guess
            else: 
                low = guess 
    
    print('Game over. Your secret number was: %i'%guess)             
  
  # Algorithm draft  
  # initialize input
    # while loop - user input as end condition
    # get midpoint
    # get user input 
    # if c end
    # otherwise reset values, repeat
    
        
  