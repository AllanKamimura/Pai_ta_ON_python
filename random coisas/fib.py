# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 10:10:02 2020

@author: allan
"""


gold =  1.6180339
numero = 1
i = input().split("\n")
t = int(i[0])

while numero < t+1:
    a = i[numero]
    b = a.split()
    b[0] = int(b[0])
    b[1] = int(b[1])
    fib = round(((gold ** b[1]) - ((1-gold) ** b[1])) / (5) ** 0.5) - round(((gold ** b[0]) - ((1-gold) ** b[0])) / (5) ** 0.5)
    print(fib)
    numero = numero + 1
    
    
    

