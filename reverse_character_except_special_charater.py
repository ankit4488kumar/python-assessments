# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:31:57 2024

@author: ankit.kumar
"""

'''
Reverse the string characters without affacting special characters.
inpput = "ab,cld.e,f"
required_output = "fe,dlc.b,a"
'''

inp = "ab,cld.e,f"
spec_char =[',','.',';',':']
temp = [j for j in inp[::-1] if j not in spec_char]

for pos, char in enumerate(inp):
    if char in spec_char:
        temp.insert(pos, char) 
      
out = ''.join(temp)
print(out)
