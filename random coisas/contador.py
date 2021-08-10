# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:32:25 2020
v2. Created on Sat Aug 22 00:28:02 2020

@author: allan
"""

# importing all necessery modules 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 

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

def contador3(texto):
    tirar = ["de","a","aos","e","pelo","da","do","das","que","dos","as","quando","os","em","o","no","na","nos","nas","para","com","um","uma","uns","umas","para","que","como","se","mas","como","também","não","ao","por","sobre""qual","sobre","esse","essa","aquilo","aquela","isto", "isso","aquele","sim"]
    newwords = []
    newtext = ""
    infile = open(texto, "r")
    stopwords = set(STOPWORDS) 
      
    # iterate through the file 
    for text in infile: 
          
        # typecaste each val to string 
        text = str(text) 
      
        # split the value con
        words = text.split() 
        # Converts each token into lowercase 
        for word in words:
            word = word.lower()
        # Remove words de tirar
        newwords = [word for word in words if word not in tirar]
        
        newtext += " ".join(newwords)+" "
      
    wc = WordCloud(width = 1000, height = 1000, background_color ='white', stopwords = stopwords, contour_width=3, contour_color='steelblue').generate(newtext) 
      
    # plot the WordCloud image                        
                     
    plt.figure(figsize = (8, 8)) 
    plt.imshow(wc) 
    plt.axis("off") 
    plt.tight_layout(pad = 0)
    plt.savefig(texto + ".png", dpi = 100)
    plt.show()
if __name__ == '__main__':
    arquivo()