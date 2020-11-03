# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:54:32 2020

@author: allan
"""

n = int(input(""))
L = []
d = {}
e = 0
for i in range(0,n):
    a = input("")
    for l in a:
        if l not in d:
            d[l] = 0
        d[l] += 1
        L.append(d)
        c = L.count(d)
        if c > e:
            e = c
        d = {}
print(e)


