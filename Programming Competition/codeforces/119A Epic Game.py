# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:05:53 2020

@author: allan
"""
x,y,z = input("").split()
x,y,z = int(x),int(y),int(z)

def mdc(a,b):
    while True:
        r = b % a
        b = a
        a = r
        if r == 0:
            break
    return b

while True:
    b = mdc(x,z)
    z = z - b
    if z < 0:
        print("1")
        break
    b = mdc(y,z)
    z = z - b
    if z < 0:
        print("0")
        break
    

        