# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:37:57 2024

@author: ankit.kumar
"""


def convert_mins_to_hours_mins_sec_format(mins):

    ss = mins * 60
    hh = ss // 3600
    ss %= 3600
    mm = ss // 60
    ss %= 60
    return "%02d:%02d:%02d" % (hh, mm, ss)

print(convert_mins_to_hours_mins_sec_format(74.50))



