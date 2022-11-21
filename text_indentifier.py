# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:55:46 2022

@author: ankit
"""
#expected output
# Akshay:4
# Ajay:1
from collections import Counter
import pandas as pd
text1 = '''Akshay: Spark is a data processing enginee which is very fast because of its in-memory processing.The current version of spark is 3.0.0.This version of spark support the delta lake feature which support the CDC concept.'''
text2 = '''Ajay: Apache Spark is a multi-language engine for executing data engineering.'''
text3 = '''Akshay: Spark is a Big Data Engine.'''


import re
name = []
count_id = []
name_dist = {"name":name,"count":count_id}
for i in [text1,text2,text3]:
    head_name = i.split(':')[0]
    text = i.split(':')[1].lower()
    words = text.split()
    wordCount = Counter(words)
    word_count = wordCount.get('spark')
    if head_name not in name:
        name.append(head_name)
        count_id.append(word_count)
    else:
        index_id = name_dist.get('name').index(head_name)
        name_dist.get('count')[index_id] = name_dist.get('count')[index_id] + word_count
        
print(pd.DataFrame(name_dist))

        
    
        
    