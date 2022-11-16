# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:51:02 2022

@author: ankit
"""

'''
Write a code to get input numbers from users and print sum of the input numbers

Example:

Input: 1,6,9,10

Output: 26
'''
def Sumofnumbers(InputStr):
    sum_number = 0
    for i in InputStr.split(','):
        sum_number = sum_number+int(i)
    return sum_number	

print(Sumofnumbers("1,6,9,10"))
