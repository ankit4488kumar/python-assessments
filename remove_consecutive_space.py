# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:58:47 2023

@author: ankit.kumar
"""
#Remove the consecutive space(Double Space) from a string
def remove_consecutive_spaces(text):
    cleaned_string = re.sub(r'\s+', ' ', text)
    return cleaned_string



import pandas as pd
import re


# Sample DataFrame
data = {'text_column': ['Hello!  How are you?', 'I have_underscores. ', '  Testing 123','radha  rani  ','apple joy','tea  plant','hey tina ']}
df = pd.DataFrame(data)


df['updated_txt'] = df['text_column'].apply(remove_consecutive_spaces)

print(df['text_column'].values)

'''Out: 
array(['Hello!  How are you?', 'I have_underscores. ', '  Testing 123',
       'radha  rani  ', 'apple joy', 'tea  plant', 'hey tina '],
      dtype=object)
'''


print(df['updated_txt'].values)


'''
Out: 
array(['Hello! How are you?', 'I have_underscores. ', ' Testing 123',
       'radha rani ', 'apple joy', 'tea plant', 'hey tina '], dtype=object)
'''
    


