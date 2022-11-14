# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:15:33 2022

@author: ankit
"""

#Write a program to Reverse words in a given String
# Input ="This is from Vertexblue"

# # Output ="Vertexblue from is This"
word = "This is from Vertexblue"
w = word.split()[::-1]
print(w)
y = []
for i in w:
    y.append(i)
    print(y)

print(" ".join(y))