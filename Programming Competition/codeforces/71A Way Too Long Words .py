# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 08:53:48 2020

@author: allan
"""


n = int(input(""))
for i in range(0,n):
    w = input("")
    if len(w) > 10:
        print(w[0]+str(len(w)-2)+w[-1])
    else:
        print(w)