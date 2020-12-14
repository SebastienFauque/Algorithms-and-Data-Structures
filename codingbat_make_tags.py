#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:33:03 2020

@author: sebastien
@title: make_tags
"""
def make_tags(tag, word):
    first = '<' + tag +'>'
    last = '</' + tag + '>'
    total = first + word + last
    return total

tag = 'i'
word = 'yay'
print(make_tags(tag, word))

