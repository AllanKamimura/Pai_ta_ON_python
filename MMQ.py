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

print("   1) Uma célula de cada vez")
print("   2) Uma coluna de cada vez")
escolha = input("Escolha: ")

if escolha == 1:
    print("Digite um valor de x, quando acabar, insira o valor 0")
    print("exemplo para escrever: 0.66 ou 66e-2")
    print("Se você inserir um valor errado, escreva denovo, mas com valor certo") 
    print("No final só da pra tirar o que está errado")
    while True:  
        a = input("valor de x= ")
        af = float(a) #isso aqui é proposital, com efeitos esteticos
        if a == "0":
            print("Os valores estão corretos? 1SIM, 2NAO")
            certo = input("")
            if certo == "1":
                break
            elif certo == "2":
                while True: #tirar valor errado
                    print("Qual valor você quer tirar?")
                    tirar = input("")
                    xlista.remove(tirar)
                    xflista.remove(float(tirar))
                    print("Ficou assim: \n x =",xlista)
                    print("Ta certo agora? 1SIM, 2NAO")
                    certo1 = input("")
                    if certo1 == "1":
                        break
                    elif certo1 == "2":
                        continue
                    else:
                        break
            break
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
            print("Os valores estão corretos? 1SIM, 2NAO")
            certo = input("")
            if certo == "1":
                break
            elif certo == "2":
                while True: #tirar valor errado
                    print("Qual valor você quer tirar?")
                    tirar = input("")
                    ylista.remove(tirar)
                    yflista.remove(float(tirar))
                    print("Ficou assim: \n x =",ylista)
                    print("Ta certo agora? 1SIM, 2NAO")
                    certo1 = input("")
                    if certo1 == "1":
                        break
                    elif certo1 == "2":
                        continue
                    else:
                        break
            break 
        ylista.append(b)
        yflista.append(bf)
        print(ylista)

if escolha == 2:
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
