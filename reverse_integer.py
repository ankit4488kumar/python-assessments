# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:49:27 2022

@author: ankit
"""

def reverseint(n):
    abs_number = abs(n)
    abs_number = str(abs_number)
    reverse = abs_number[::-1]
    if n < 0:
        output = int("-"+reverse)
    else:
        output = int(reverse)
    return output
print(reverseint(0))