#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:25:00 2020

@author: sebastien
@title: codingbat_sum67.py

"""
def sum67(nums):
    input = True
    total = 0
    for num in nums:
        if input:
            if num == 6:
                input = False
            else:
                total += num
        else:
            if num == 7:
                input = True
    return total
nums = [2, 7, 6, 2, 6, 7, 7] # sum = 37
#16
print(sum67(nums))