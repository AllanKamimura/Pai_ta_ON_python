# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:23:12 2020

@author: allan
"""

n = input("")
li = input("").split()
d = {"0": 0,"1": 0,"2": 0}

for l in li:
    l = int(l)
    if l % 3 == 0:
        d["0"] += 1
    if l % 3 == 1:
        d["1"] += 1
    if l % 3 == 2:
        d["2"] += 1
        
if d["0"] > 1:
    print(int(d["0"]*(d["0"]-1)/2 + d["1"] * d["2"]))
else:
    print(int(d["1"] * d["2"]))