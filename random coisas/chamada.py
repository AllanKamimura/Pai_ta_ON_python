# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 01:55:49 2020

@author: allan
"""
def arquivo():
    arquivo = input("Colocar o arquivo .txt na mesma pasta e escrever o nome:")
    return contador(arquivo)
    
def contador(arquivo):
    dic = {}
    infile = open(arquivo, "r") 
    outfile = open(arquivo + " alfabetico", "w")
    # iterate through the file 
    for line in infile: 
        # typecaste each text to string 
        line = str(line) 
        # split the value text
        if line.isupper():
            if line not in dic:
                dic[line] = 0
            dic[line] += 1
    top = sorted(dic.items(), key=lambda x: x[1])
    for nome in top:
        outfile.write(nome)
    infile.close()
    outfile.close()
if __name__ == '__main__':
    arquivo()

