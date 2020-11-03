# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:56:59 2020

@author: allan
"""


n = int(input(""))
s = 0
for i in range(0,n):
    a,b,c = input("").split()
    if int(a)+int(b)+int(c) > 1:
        s += 1
print(s)
    