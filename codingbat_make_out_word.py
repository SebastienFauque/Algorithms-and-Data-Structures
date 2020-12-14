#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:12:37 2020

@author: sebastien
@title: codingbat_make_out_word.py
"""
def make_out_word(out, word):
    return out[:2] + word + out[2:]

out = '[[]]'
word = 'Yay'

print(make_out_word(out, word))
