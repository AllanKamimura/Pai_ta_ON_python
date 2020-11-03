# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 07:09:51 2020

@author: allan
"""
# oieeee é o Allan(Loli) tentei fazer um programa com base no seu, mas que calculasse
# para qualquer shift e para qualquer mensagem
while True:
    alfa = list(map(chr, range(97, 123))) #alfabeto
    beta = [] #alfabeto shiftado
    a = 0 #variavel qualquer
    intab = "" # Each possible letter that can appear in the message
    outtab = "" # The correspondent correct letter
    n = int(input("Numero do Caesar Shift: \n"))
    message = input("Mensagem para decodificar: \n")
    if n < 0: #conversao
        n1 = n % -26 #resto da divisao por -26
        for n1 in range(n1,len(alfa)+n1,1):
            beta.append(alfa[n1]) #isso aqui tava bugando para n > 26
    else: #convesao tambm, acho q da pra fazer de uma vez so na verdade
        n2 = n % 26 # resto da divisao por 26
        for n2 in range(n2,len(alfa)+n2,1):
            beta.append(alfa[n2-len(alfa)]) #mesma coisa para n < -26
    for a in range(0,len(alfa)): #deixando do mesmo formato
        intab = intab + alfa[a] 
        outtab = outtab + beta[a]
    trantab = str.maketrans(intab, outtab)  # maketrans is used to create a dictionary with the relations between letters
    print(message.translate(trantab)) # Printing the translated message
    retornar = input("Aperte ENTER para retornar") #voltar para o começo
    if retornar == "":
        continue
    else:
        break
