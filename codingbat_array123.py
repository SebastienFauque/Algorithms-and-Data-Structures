#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:13:19 2020

@author: sebastien
@title: codingbat_array123.py
"""

def array123(nums):
    """
    input: an array of integers, "nums".
    purpose: to return a boolean True if the sequence 1, 2, 3 appears in "nums".
    Output: a boolean True or False.
    """
    i = 0
    for i in range(len(nums)):
        if nums[i:i+3] == [1, 2, 3]:
            return True
        
    return False
        
nums = [1, 2, 3]
print(array123(nums))