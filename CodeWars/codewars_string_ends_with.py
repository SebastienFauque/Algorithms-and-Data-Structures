# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:57:02 2020

@author: Sebastien
@fileName: string_ends_with.py
@project: codewars problem 

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

"""

def solution(string, ending):
    end_len = len(ending)
    if string[-end_len:] == ending:
        return True
    elif end_len == 0 & len(string) >= 0:
        return True        
    else:
        return False