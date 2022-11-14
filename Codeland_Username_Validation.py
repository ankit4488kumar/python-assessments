# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:54:12 2022

@author: ankit
"""
'''
Codeland Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter 
being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, 
otherwise return the string false.
Examples
Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true
'''

def CodelandUsernameValidation(strParam):
  import re
  pattern = "^[A-Za-z0-9_]*$"
  startwith = '^[A-Za-z]'
  if len(strParam) >4 and len(strParam)<25 and bool(re.match(pattern, strParam)) == True and bool(strParam.endswith('_'))==False and bool(re.match(startwith, strParam)) == True:
    out = "true"
  else:
    out = 'false'


  # code goes here
  return out

# keep this function call here 
print(CodelandUsernameValidation(input("Enter the string: ")))