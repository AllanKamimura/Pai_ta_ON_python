# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:26:12 2020

@author: allan
"""


n = int(input(""))
dinhero = 0
lucro = 0
produtos = {}
for i in range(0,n):
    a,b,c = input("").split()
    c = int(c)
    if a[0].lower() == "c":
        if b not in produtos:
            produtos[b] = []
        dinhero -= c
        produtos[b].append(c)

    if a[0].lower() == "v":
        if b in produtos:
            presos = produtos[b]
            presos.sort()
            if c > presos[-1]:
                dinhero += c
                lucro += c - presos[-1]
                produtos[b].remove(presos[-1])
        else:
            dinhero += c
            
for produto in produtos:
    for price in produtos[produto]:
        dinhero += price
    
print(dinhero)
