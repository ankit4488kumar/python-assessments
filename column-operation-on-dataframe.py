# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:54:29 2022

@author: ankit
"""
#Create a column with condition
#if difference of column A 2nd row and 1st row multiply with difference with column B 2nd row and column A 1st row is grater than 0
#then value = 1 else 0

 
import pandas as pd
df = pd.DataFrame({"A":[2,3,5,7,9],"B":[12,23,45,76,89]})
df_len = len(df)
val = []
for i in range(0,df_len):
    print(i)
    print(df.iloc[i,0])
    print(df.iloc[i-1,0])
    print(df.iloc[i,1])
    
    if i == 0:
        val.append(0)
    else:
        if ((df.iloc[i,0]-df.iloc[i-1,0])*(df.iloc[i,1]-df.iloc[i-1,0]))>0:
            
            val.append(1)
        else:
            val.append(0)
            
df['DA'] = val


Output:-
  A   B  DA
0  2  12   0
1  3  23   1
2  5  45   1
3  7  76   1
4  9  89   1
