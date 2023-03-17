#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:24:34 2020

@author: sebastien
@title: codingbat_string_match.py
"""

def string_match(a, b):
    """
    Given 2 strings, a and b, return the number of the positions where
    they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields
    3, since the "xx", "aa", and "az" substrings appear in the same place in
    both strings.
    
    Example: 
        string_match('xxcaazz', 'xxbaaz') → 3
        string_match('abc', 'abc') → 2
        string_match('abc', 'axc') → 0
    
    input: two strings.
    purpose: match substrings of length two in the same positon from either string.
    output: count of the number of matching substrings.
    """
    
    #  Select the shorter string
    shorter = ''
    if len(a) < len(b):
        shorter = a
    elif len(a) == 0:
        return 0
    elif len(b) == 0:
        return 0
    else:
        shorter = b
        

    #  Initialize a substring for each string and a counter for matching substrs
    subA = ''
    subB = ''
    ctr = 0
     
    #  Make the substring
    for i in range(len(shorter)):
        subA = a[i:i+2]
        subB = b[i:i+2]

        #  check if the length of the substring is 2 or greater
        if len(subA) == 2:
            #  check for substring matching, ctr + 1
            if subA == subB:
                ctr += 1
               
    return ctr

a = 'xxc  aazz'  
b = 'xxb  aaz'
print(string_match(a,b))

