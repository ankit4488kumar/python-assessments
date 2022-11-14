# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:26:55 2022

@author: ankit
"""
'''
Have the function FirstFactorial(num) take the num parameter being passed 
and return the factorial of it. For example: 
if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. 
For the test cases, the range will be between 1 and 18 and the input will always be an integer.
Examples
Input: 4
Output: 24
Input: 8
Output: 40320
'''

def FirstFactorial(num):
  output = 1
  for i in range(2,num+1):
    output = output*i
  # code goes here
  return output

# keep this function call here 
print(FirstFactorial(int(input("Enter the number: "))))