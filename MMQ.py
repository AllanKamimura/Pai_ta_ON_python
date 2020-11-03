# -*- coding: utf-8 -*-
"""

Created on Fri Jul  3 05:09:05 2020

@author: Allan Henrique Kamimura
"""


xlista=[]
xflista=[]#x em float
ylista=[]#fiz isso pra testar uma coisa
yflista=[]#y em float
sumx = 0
vertn = 0
sumy = 0
alfad = 0
alfan = 0
xx = 0
alfan = 0

print(" ")
print("O proposito desse programa é fazer uma regressão linear utilizando o Método dos Mínimos Quadrados")
print("Para cálculos laboratoriais com erro experimental\n")
print("")
print("Digite um valor de x, quando acabar, insira o valor 0")
print("exemplo para escrever: 0.66 ou 66e-2")

while True:  
    a = input("valor de x= ")
    af = float(a) #isso aqui é proposital, com efeitos esteticos
    if a == "0":
        break
    xlista.append(a)
    xflista.append(af)
    print(xlista)
print("Digite um valor de y ou digite 0 para prosseguir")
while True:
    b = input("valor de y= ")
    bf = float(b)
    if b == "0":
        break 
    ylista.append(b)
    yflista.append(bf)
    print(ylista)

#vale pros 2 casos
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
print(len(xflista),"valores para x: ",xflista)
print(len(yflista),"valores para y: ",yflista)
print("")
print("O coeficiente angular(a ± Δa) é:",alfa,"±",ialfa)
print("O coeficiente linear(b ± Δb) é:",beta,"±",ibeta)
print("Dispersão média do ajuste:",vert)
print("Não se esqueça de truncar os valores quando colocar no relatório")
print("")
