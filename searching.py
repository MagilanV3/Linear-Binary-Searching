# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:11:25 2020

@author: MAGIL
"""

def linear_search(l, item, issorted = False):
    for i in range (len(l)):
        if l[i] == item:
            return i
    return None

def binary_search(l, item, issorted = False):
    if (issorted == True):
        low = 0
        high = len(l) - 1
    
        while low <= high:
            mid = (low + high) // 2
    
            if l[mid] == item:
                return mid
            elif l[mid] > item:
                high = mid - 1
            else:
                low = mid + 1
    if (issorted == False):
        return linear_search(l , item, False)
    return None