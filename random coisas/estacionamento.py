# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:36:05 2020

@author: allan
"""

import math

#pega a hora de entrada e saida
entrada = input("Hora da entrada: ")
saida = input("Hora da saida: ")

#Separa as horas dos minutos
horain, minin = entrada.split()
horaout, minout = saida.split()

#As entradas de input estao no tipo string, trasnformar em numero inteiro
horain, minin = int(horain), int(minin)
horaout, minout = int(horaout), int(minout)

#Quanto tempo ele ficou no estacionamento? transformar as horas em minutos e subtrai saida - entrada
entrada = 60*horain + minin
saida = 60*horaout + minout
permanencia = saida - entrada

#se esse valor der negativo, quer dizer q ele virou a noite no estacionamento
if permanencia < 0:
    #adicionar mais 24 horas ou 24*60 minutos ao valor antigo
    permanencia = permanencia + 24*60

#quantas horas ele passou
horas = permanencia / 60

# arredondando para cima
horas = math.ceil(horas)
horas = int(horas)

#tempo menor ou igual a 2
if horas <= 2: 
    tarifa = horas * 1
# elif significa maior que 2 e menor ou igual a 4
elif horas <= 4: 
    tarifa = 2 + (horas-2)*1.4
# else significa maior que 4
else:
    tarifa = 2 + 2*1.4 + (horas-4)*2

#mostra o valor da tarifa
print(tarifa)



