# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:52:22 2022

@author: ankit
"""
'''
input --> 
l1 = [1,2,3,4]
l2 = [2,3,3]
l3 = [3,3,3]
output --> 
[[1, 2, 3], [2, 3], [3], [4]]
'''
import itertools
l1 = [1,2,3,4]
l2 = [2,3,3]
l3 = [3,3,3]
out =[]
for i,j,k in itertools.zip_longest(l1,l2,l3):
    temp = [i,j,k]
    l = list(set(temp))
    if None in l:
        l.remove(None)
    out.append(l)
print(out)

#[[1, 2, 3], [2, 3], [3], [4]]