# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:07:05 2020

@author: allan
"""

#mesma coisa do outro, mas usando um dicionario
while True:
    a = 0
    alfa = list(map(chr, range(97, 123))) #alfabeto
    beta = [] #alfabeto shiftado
    n = int(input("Numero do Caesar Shift: \n"))
    message = input("Mensagem para decodificar: \n")
    tradutor = {}
    texto = ""
    if n < 0: #conversao
        n1 = n % -26 #resto da divisao por -26
        for n1 in range(n1,len(alfa)+n1,1):
            beta.append(alfa[n1]) #isso aqui tava bugando para n > 26
    else: #convesao tambm, acho q da pra fazer de uma vez so na verdade
        n2 = n % 26 # resto da divisao por 26
        for n2 in range(n2,len(alfa)+n2,1):
            beta.append(alfa[n2-len(alfa)]) #mesma coisa para n < -26
    for a in range(0,len(alfa)): #tabela de conversao
        tradutor[alfa[a]] = beta[a]
    for letra in message: #traduzindo cada letra pela letra shiftada
        if letra in alfa:
            letra = tradutor[letra]
        else: #nao traduzir oq nao é letra
            pass
        texto = texto + letra #montando o texto de volta
    print(texto)
    retornar = input("Aperte ENTER para retornar") #voltar para o começo
    if retornar == "":
        continue
    else:
        break