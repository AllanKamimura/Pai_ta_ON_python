# -*- coding: utf-8 -*-
"""

Created on Fri Jul  3 05:09:05 2020
v2 Created on Tue Jul 28 02:14:04 2020

@author: Allan Henrique Kamimura
"""

import matplotlib.pyplot as plt
import numpy as np

xlista=[]
xflista=[]#x em float
ylista=[]#fiz isso pra testar uma coisa
yflista=[]#y em float


def intro():
    print(" ")
    intro = "O proposito desse programa é fazer uma regressão linear utilizando o Método dos Mínimos Quadrados"
    print("|{0:^100}|".format(intro))
    return Menu()

def Menu(): #menu principal
    while True:
        print("Escolha uma das opções abaixo:")
        print("   MMQ) Regreção Linear com Método dos Mínimos Quadrados")
        print("   ANT) Utilizar a vesão antiga do programa")
        print("   LOG) Acessar o change log")
        print("   SAIR) Fecha o programa")
        Escolha = input("Escolha: ")
        Escolha1 = Escolha.lower()
        if Escolha1 in ["mmq","ant","log","sair"]:
            break
        else:
            print(Escolha1 + " não é uma escolha válida. Escolha novamente\n")
            continue #apenas escolhas validas
    if Escolha1 == "mmq":
        return Menu2()
    if Escolha1 == "sair":  
        input("Aperte ENTER para sair")

def Menu2():
    while True:
        print("Você escolheu Regreção linear com MMQ")
        print("Agora escolha como inserir os valores:")
        print("   1) Uma célula de cada vez")
        print("   2) Uma coluna de cada vez")
        print("   3) Copiar e colar do google sheets")
        print("   4) Voltar para o menu anterior")
        escolha2 = input("Escolha: ")
        if escolha2 in ["1","2","3","4","5"]:
            break
        else:
            print("\nApenas as opções abaixo: ")
            continue
    if escolha2 == "1":
        return y1()
    if escolha2 == "2":
        return xy()
    if escolha2 == "3":
        return sheets()
    if escolha2 == "4":
        return Menu()
    
def x1():
    print("Digite um valor de x, quando acabar, insira o valor 0")
    print("Exemplo de escrita: 0,66 ou 0.66 ou 66e-2")
    print("Se você inserir um valor errado, escreva denovo, mas com valor certo") 
    print("No final só da pra tirar o que está errado")
    while True:  
        a = input("valor de x = ")
        try: #com isso, o valor x = 0 é permitido
            if a == "":
                break
            af = float(a.replace(',','.')) #isso aqui é proposital, com efeitos esteticos
            xlista.append(a)
            xflista.append(af)
            print("|| {0:^20} ||".format("x"))
            for numerox in xlista:
                print("|| {0:^20} ||".format(numerox))
            continue
        except:
            print("Apenas números e digite dessa forma: 0.66 ou 66e-2")
            continue
    while True:
        print("|| {0:^20} ||".format("x"))
        for numerox in xlista:
            print("|| {0:^20} ||".format(numerox))
        certo1 = input("Os valores estão corretos? S ou N? ")
        if certo1.lower() in ["s","n"]:
            break
        else:
            print("Apenas S ou N")
            continue
    if certo1.lower() == "s":
        return final()
    if certo1.lower() == "n":      
        return corrigirx1()
    
def corrigirx1():
    print("|| {0:^20} ||".format("x"))
    while True: #tirar valor errado
        for numero in xlista:
            print("|| {0:^20} ||".format(numero))
        print("Qual valor você quer tirar?")
        tirar = input("x = ")
        try:
            xlista.remove(tirar)
            xflista.remove(float(tirar.replace(',','.')))
            print("Ficou assim:\n|| {0:^20} ||".format("x"))
            for numero in xlista:
                print("|| {0:^20} ||".format(numero))
            certo1 = input("Ta certo agora? S ou N ")
            if certo1.lower() == "s":
                break
            if certo1.lower() == "n":
                continue
            else:
                print("Apenas S ou N")
                continue
        except:
            print("Apenas números da lista \n")
            continue
    return final()
        
def y1():
    print("")
    print("Digite um valor de y ou digite 0 para prosseguir")
    print("Exemplo de escrita: 0,66 ou 0.66 ou 66e-2")
    print("Se você inserir um valor errado, escreva denovo, mas com valor certo") 
    print("No final só da pra tirar o que está errado")
    while True:
        a = input("valor de y = ")
        if a == "":
            break
        try: #com isso, o valor y = 0 é permitido
            af = float(a.replace(',','.')) #isso aqui é proposital, com efeitos esteticos
            ylista.append(a)
            yflista.append(af)
            print("|| {0:^20} ||".format("y"))
            for numero in ylista:
                print("|| {0:^20} ||".format(numero))
            continue
        except:
            print("Apenas números e digite dessa forma: 0.66 ou 66e-2")
            continue      
    while True:
        print("Ficou assim:\n|| {0:^20} ||".format("y"))
        for numeroy in ylista:
            print("|| {0:^20} ||".format(numeroy))
        certo1 = input("Os valores estão corretos? S ou N? ")
        if certo1.lower() in ["s","n"]:
            break
        else:
            print("Apenas S ou N")
            continue
    if certo1.lower() == "s":
        return x1()
    if certo1.lower() == "n":      
        return corrigiry1()
    
def corrigiry1():
    while True: #tirar valor errado
        print("Ficou assim:\n|| {0:^20} ||".format("y"))
        for numero in ylista:
            print("|| {0:^20} ||".format(numero))
        print("Qual valor você quer tirar?")
        tirar = input("y = ")
        try:
            ylista.remove(tirar)
            yflista.remove(float(tirar.replace(',','.')))
            print("Ficou assim:\n|| {0:^20} ||".format("y"))
            for numeroy in ylista:
                print("|| {0:^20} ||".format(numeroy))
            certo1 = input("Ta certo agora? S ou N ")
            if certo1.lower() == "s":
                break
            if certo1.lower() == "n":
                continue
            else:
                print("Apenas S ou N")
                continue
        except:
            print("Apenas números da lista \n")
            continue
    return x1()

def xy():
    while True:
        print("")
        print("Insira os valores com o seguinte formato: ")
        print("ex: 5,7 2.2222 5e-9")
        print("usando espaço para separar cada valor, e=10 elevado a")
        ylista = input("y = ")
        print("")
        xlista = input("x = ")
        y = ylista.split()
        x = xlista.split()
        #criando a lista com floats
        try:
            for o in x:
                xflista.append(float(o.replace(',','.')))
            for p in y:
                yflista.append(float(p.replace(',','.')))
            break
        except:
            x = []
            y = []
            print(ylista,"\n",xlista)
            print("Os valores foram corretamente digitados?")
            continue
        
def sheets():
    while True:
        print("")
        print("No Google sheets, selecione toda a coluna com valores e copie")
        print("No programa, apenas cole, notação cientifica funciona")
        print('OBS: se o programa "fechar sozinho" tente fazer a mesma coisa, mas na parte de uma celula de cada vez')
        ylista = input("y = ")
        print("")
        xlista = input("x = ")
        y = ylista.split("\n")
        x = xlista.split("\n")
        #criando a lista com floats
        try:
            for p in y:
                yflista.append(float(p.replace(',','.')))
            for o in x:
                xflista.append(float(o.replace(',','.')))
            break
        except:
            x = []
            y = []
            print(ylista,"\n",xlista)
            print("Os valores foram corretamente digitados?")
            continue
    return final()

#vale pros 2 casos
def final():
    sumx = 0
    vertn = 0
    sumy = 0
    alfad = 0
    alfan = 0
    xx = 0
    alfan = 0
    
    for i in range(0,len(xflista)):#calculo das medias
        sumx = sumx + xflista[i]
        sumy = sumy + yflista[i]
    averagex = sumx/len(xflista)
    averagey = sumy/len(yflista)
    for m in range(0,len(xflista)):
        #coef angular
        alfan = alfan + (xflista[m]-averagex)*(yflista[m])
        alfad = alfad + (xflista[m]-averagex)**2
    alfa = alfan/alfad
    beta = averagey - alfa*averagex 
    #coef linear
    for n in range(0,len(xflista)): 
        #calculo dos erros
        xx = xx + xflista[n]**2
        vertn = vertn + (alfa*xflista[n]+beta-yflista[n])**2
    vert = (vertn/(len(xflista)-2))**.5 #dispersao media do ajuste
    ialfa = vert/(alfad)**.5 #erro angular
    ibeta = vert*(xx/(len(xflista)*alfad))**.5 #erro linear
    print("") #resultado
    print("Foram inseridos:")
    print("||{0:^3}||  {1:^20} ||  {2:^20} ||".format("i","y","x"))
    for a in range(0,len(xflista)):
        print("||{0:^3}||  {1:^20} ||  {2:^20} ||".format(a+1,yflista[a],xflista[a]))
    print("")
    print("O coeficiente angular(a ± Δa) é:",alfa,"±",ialfa)
    print("O coeficiente linear(b ± Δb) é:",beta,"±",ibeta)
    print("Dispersão média do ajuste:",vert)
    print("Não se esqueça de truncar os valores quando colocar no relatório")
    print("")
