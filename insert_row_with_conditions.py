# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:10:27 2022

@author: ankit
"""
#insert the raw with a condition in a column of a dataframe
import pandas as pd
df = pd.DataFrame({"A":[3,8,10,34]}) 

for i in range(0,7):
    df.loc[len(df.index)] = [df["A"][len(df.index)-1] + 10]
print(df)


Output:-
     A
0     3
1     8
2    10
3    34
4    44
5    54
6    64
7    74
8    84
9    94
10  104
