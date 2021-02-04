# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:40:46 2021

@author: Sebastien
@fileName: categorize_new_member.py
@project:
    
https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

7 kyu
    
    The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of lists containing two items each. Each list contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Note for F#: The input will be of (int list list) which is a List<List>

Example Input
[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
Output
Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example Output
["Open", "Open", "Senior", "Open", "Open", "Senior"]
    
"""

def open_or_senior(data):
    '''
    Input: List of lists where each inner list has two numbers for a single Croquet club member.
            The first number is the person's age and the second number is the person's handicap
    
    Machine: if the member is age 55 or older and has a handicap greater than 7 label that member as "Senior", otherwise the member is in the "Open" category. 
    
    Output: A List with the category for each member in the following format
    ["Open", "Open", "Senior", "Open", "Open", "Senior"]
    
    '''
    results = []
    for list in data:
        if list[0] >= 55 and list[1] > 7:
            results.append("Senior")
        else:
            results.append("Open")
    
    return results

data = [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
print(open_or_senior(data))