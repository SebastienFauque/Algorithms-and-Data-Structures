#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:21:25 2020

@author: sebastien
@title: codingbat_sum13.py

Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that 
come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

"""

def sum13(nums):
  for i in range(len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if len(nums) > (i+1):
        nums[i+1] = 0
      
  return sum(nums)

nums = [13, 1, 2, 13, 2, 1, 13]

print(sum13(nums))