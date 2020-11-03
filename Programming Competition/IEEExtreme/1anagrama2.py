# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 01:39:10 2020

@author: allan
"""

d = {}
n = int(input(""))

for i in range(0,n):
    a = input("")
    r = ''.join(sorted(a))
    if r not in d:
        d[r] = 0
    d[r] += 1
d = sorted(d.items(), key=lambda x: x[1], reverse = True)
print(d[0][1])