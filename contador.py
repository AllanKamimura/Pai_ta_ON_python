# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:32:25 2020

@author: allan
"""

def arquivo():
    texto = input("Arquivo:")
    prep = input("Contar preposiçoes e artigos? S ou N\n")
    if prep.lower() == "s":
        return contador(texto)
    if prep.lower() == "n":
        return contador2(texto)

def contador(texto):
    infile = open(texto, "r")
    words_dic = {}
    word_ct = 0
    for line in infile:
        for word in line.lower().split():
            word = word.strip("'?,.;!-/\"“”()")
            if word not in words_dic:
                words_dic[word] = 0      # add word to words with 0 count
            words_dic[word] = words_dic[word] + 1
            word_ct = word_ct +1
    top = sorted(words_dic.items(), key=lambda x: x[1])
    for i in top:
        print(i[0],i[1])
    print("Total=",word_ct)
    input("Aperte ENTER para fechar")
    infile.close()

def contador2(texto):
    desprep = []
    words_dic = {}
    word_ct = 0
    tirar = ["de","a","e","da","do","as","os","em","o","no","na","nos","nas","para","com","um","uma","uns","umas","com","para","esse","essa","isso","aquele","aquilo","aquela","este","esta","isto","para","se","que","para"]
    infile = open(texto, "r")
    for line in infile:
        for word in line.lower().split():
            word = word.strip("'?,.;!-/\"“”()")
            if word not in tirar:
                desprep.append(word)
                word_ct = word_ct + 1
    for word in desprep:
        if word not in words_dic:
            words_dic[word] = 0      # add word to words with 0 count
        words_dic[word] = words_dic[word] + 1
    top = sorted(words_dic.items(), key=lambda x: x[1], reverse = True)
    print("Total=",word_ct)
    for i in top:
        print(i[0],i[1])
    input("Aperte ENTER para fechar")
    infile.close()
    
if __name__ == '__main__':
    arquivo()