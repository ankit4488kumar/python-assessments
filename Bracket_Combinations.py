# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:23:12 2022

@author: ankit
"""
'''
Have the function BracketCombinations(num) read num which will be an integer 
greater than or equal to zero, and return the number of valid combinations 
that can be formed with num pairs of parentheses. For example, 
if the input is 3, then the possible combinations of 3 pairs of parenthesis, 
namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). 
There are 5 total combinations when the input is 3, so your program should return 5.
Examples
Input: 3
Output: 5
Input: 2
Output: 2
'''

def BracketCombinations(num):
  a = num**2
  if a%2 == 0:
    out = a//2
  else:
    out = a//2 + 1
  # code goes here
  return out

# keep this function call here 
print(BracketCombinations(int(input())))