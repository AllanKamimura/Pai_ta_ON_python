# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:38:26 2020

@author: allan
"""


a,b = input("").split()
c,b = int(int(a)**0.5), int(int(b)**0.5)
if int(c**2) == int(a):
    print(b-c+1)
else:
    print(b-c)
