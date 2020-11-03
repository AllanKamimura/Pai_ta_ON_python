# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:09:45 2020

@author: allan
"""


s = input("")
l = s.split()
l.sort()
a,b = int(l[0]),int(l[1])

while True:
    r = b % a
    b = a
    a = r
    if r == 0:
        print(b)
        break
