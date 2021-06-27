#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:31:52 2021

@author: isaaclello-smith
"""

def search(L, e):
    '''
    returns whether item in list, searching by index 

    Parameters
    ----------
    L : List
    e : item to find in list

    Returns
    -------
    bool - item in list

    '''
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def search1(L, e):
    '''
    returns whether item in list, searching by item 

    Parameters
    ----------
    L : List
    e : item to find in list

    Returns
    -------
    bool - item in list
    ''' 
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

# Should operate the same except possibly empty list or search
assert search([], 'a') == search1([], 'a'), 'functions did not return same outcome for empty list'

assert search(['a'], '') == search1(['a'], ''), 'functions did not return same outcome for empty search item'

assert search(['a', 'b', 'c', 'd', 'h'], 'f') == search1(['a', 'b', 'c', 'd', 'h'], 'f'), 'functions did not return same outcome for missing item'

assert search(['a', 'b', 'c', 'd', 'h'], 'h') == search1(['a', 'b', 'c', 'd', 'h'], 'h'), 'functions did not return same outcome for item in list'

def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False

assert search([], 'a') == search2([], 'a'), 'functions did not return same outcome for empty list'

assert search(['a'], '') == search2(['a'], ''), 'functions did not return same outcome for empty search item'

assert search(['a', 'b', 'c', 'd', 'h'], 'f') == search2(['a', 'b', 'c', 'd', 'h'], 'f'), 'functions did not return same outcome for missing item'

assert search(['a', 'b', 'c', 'd', 'h'], 'h') == search2(['a', 'b', 'c', 'd', 'h'], 'h'), 'functions did not return same outcome for item in list'

def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)

try:
    search3([], 'a')
except IndexError:
    print('search3 throws index out of range error for empty list')    

assert search(['a'], '') == search3(['a'], ''), 'functions did not return same outcome for empty search item'

try: 
    search3(['a'], 'c')
except IndexError:
    print('search3 throws index out of range error for list of length 1 for which search item is not first element and is larger than first element')

# interesting - this test case missed the case of e not in L but larger than largest element
assert search(['a', 'b', 'c', 'd', 'h'], 'f') == search3(['a', 'b', 'c', 'd', 'h'], 'f'), 'functions did not return same outcome for missing item'

# this test case covers case of e not in L but larger than largest element
try:
    search(['a', 'b', 'c', 'd', 'h'], 'i') == search3(['a', 'b', 'c', 'd', 'h'], 'i')
except IndexError: 
    print('search3 throws index out of range error for list with search item larger than all items in list')   

assert search(['a', 'b', 'c', 'd', 'h'], 'h') == search3(['a', 'b', 'c', 'd', 'h'], 'h'), 'functions did not return same outcome for item in list'