# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:46:49 2020

@author: Sebastien
@fileName: codewars_vowel_count.py
@project: Count the number of vowels not including the letter y
"""

def get_count(input_str):
    num_vowels = 0
    # your code here
    vowels = ["a", "e", "i", "o", "u"]
    
    for letter in input_str:
        if letter in vowels:
            num_vowels += 1
    return num_vowels
