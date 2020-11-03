# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:16:01 2020

@author: allan
"""


n = int(input(""))
L = {}
R = {}
par = 0
for a in range(0,n):
    s = input("")
    l = s.strip()
    print(l[0],l[1],l[-1])
    if l[-1] == "R":
        if l[0] not in R:
            R[l[0]] = 0
        R[l[0]] += 1
    if l[-1] == "L":
        if l[0] not in L:
            L[l[0]] = 0
        L[l[0]] += 1
r = sorted(R)
l = sorted(L)
for num in l:
    if num in r:
        par = par + min(L[num],R[num])
print(par)        
