# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:10:37 2021

@author: Sebastien
@fileName: find_the_capitals.py
@project:
    
    Write a function that takes a single string (word) as argument.
    The function must return an ordered list containing the indexes
    of all capital letters in the "string.
    
"""

def capitals(word):
    """
    My function to return the index of capital letters in a word.
    
    Parameters
    ----------
    word : A word with capital and lowercase letters.

    Returns : A list of indexes.
    -------
    None.

    """
    return [ind for ind, letter in enumerate(word) if letter.isupper()]
        
print(capitals('DVFircwBSnaotYiyjrfDEXfcxcMLuBx'))