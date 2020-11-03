# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:46:20 2020

@author: allan
"""


n = input("")
li = input("").split()
d = {"0": 0,"1": 0,}

for l in li:
    l = int(l)
    if l % 2 == 0:
        d["0"] += 1
    if l % 2 == 1:
        d["1"] += 1

# if d["0"]*(d["0"]-1)/2 < 0:
#     d["0"] = 1
# if d["1"]*(d["1"]-1)/2 < 0:
#     d["1"] = 1
print(int(d["0"]*(d["1"])))