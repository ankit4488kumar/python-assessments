# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 11:38:25 2022

@author: ankit
"""

'''
Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
Original Tuple:
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:
[10.5, 44.0, 58.0, 2.5]
'''
tuples = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
final = []
for i in list(tuples):
    sublist = list(i)
    sum = 0
    for ele in sublist:
        sum = sum+ele
        avg = sum/len(sublist)
    final.append(avg)
    
print(final)

'''
ouput
[10.5, 44.0, 58.0, 2.5]
'''       
    