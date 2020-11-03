# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:55:25 2020

@author: allan
"""


def f(x):
    y = x**2 -5*x + 6
    return y

def raiz(a,b,tolerancia):
    incremento = 0.1
    t = a 
    raiz = []
    while True:
        y1 = f(t)
        t = t + incremento
        y2 = f(t)
        if y1 * y2 < 0:
            if incremento < tolerancia:
                raiz.append(t)
                break
            else:
                incremento = incremento / 10
                t = a
                continue
        elif t < b:
            continue
        else:
            raiz = "nao tem raiz no intervalo"
            break
    return raiz
        