# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:57:01 2022

@author: ankit
"""
'''
Have the function LongestWord(sen) take the sen parameter being passed and 
return the longest word in the string. If there are two or more words 
that are the same length, return the first word from the string with that length. 
Ignore punctuation and assume sen will not be empty. Words may also contain numbers, 
for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
'''
def LongestWord(sen):
  import re
  sen = re.sub(r'[^\w\s]', '', sen)
  words = sen.split()
  letter = []
  length = []
  for i in words:
    letter.append(i)
    length.append(len(i))
  dist = {"letter":letter,"length":length}
  max_val = max(length)
  position = length.index(max_val)
  out = letter[position]
  return out

# keep this function call here 
print(LongestWord(input("Enter the sentence: ")))