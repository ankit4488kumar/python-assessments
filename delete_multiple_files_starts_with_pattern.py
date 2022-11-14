# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:04:09 2022

@author: ankit
"""

import os, re

def delete_files(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))
delete_files('anonymous_ip/','anonymous*')