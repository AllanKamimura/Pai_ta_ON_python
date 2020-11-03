# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:06:04 2020

@author: allan
"""

def soma():
    x = input()
    y = x.split()
    try:
        res = int(y[0]) + int(y[1])
    except:
        return soma()
    print (res)
soma()