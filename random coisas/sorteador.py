# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 19:27:49 2020

@author: allan
"""
while True:
    import random
    verbos = ["comeu ","tomou ","pulou ","entrou n","pintou ","estudou ","vendeu ",
             "assistiu ","olhou ","desconfiou d","deu em cima d","mordeu ",
             "lambeu ","chamou ","abriu ","estudou ","conheceu ","brincou com ",
             "mexeu n","recebeu ","achou ","acordou ","pegou ","bateu n",
             "apanhou d","matou ","mandou ","desejou ","lavou ","mudou ",
             "sonhou com ","pagou ","fechou ","permitiu ","sentou em cima d",
             "sentou em cima d","sentou em cima d","sentou em cima d","sentou em cima d",
             "encheu ","ligou ","agradeceu ","convidou ","entregou ","beijou ",
             "apresentou ","ensinou para ","perguntou sobre ","penteou ","escovou ",
             "passou a mão n","apagou ","amou ","viu ","escutou ","escreveu sobre ",
             "andou em cima d","dormiu em cima d","vomitou em cima d","pensou n","jogou ","trabalhou ",
             "subiu n","construiu ","tirou ","gostou d","prendeu ","roeu ",
             "varreu ","limpou ","plantou ","regou ","acompanhou ","aumentou ",
             "distraiu ","defendeu ","lutou com ","amassou ","quebrou ","cozinhou ",
             "virou ","cobriu ","varreu ","maquiou ","escondeu ","trocou ",
             "desenhou ","engoliu ","invadiu ","scaneou ","cheirou ","lambuzou ",
             "cuspiu n","encarou ","abaixou ","hidratou ","celebrou ",
             "calculou ","xingou ","sugou ","apontou para ","tatuou ","navegou ",
             "entupiu ","hackeou ","furou ","esculpiu ","fotografou ","chupou ",
             "arrastou ","encaixou ","rodeou ","espantou ","imitou ","remou ",
             "ressucitou ","estranhou ","curtiu","gritou com ","espalhou ",
             "buzinou para ","sorriu para ","babou n","seduziu ","manchou ",
             "enfiou ","cavalgou ","absorveu ","afundou ","alinhou ","dirigiu ",
             "flagrou ","infectou ","arrotou ","enterrou ","encostou n",
             "deu banho n","levou ","traficou ","desenterrou ","bombardeou ",
             "fincou ","pediu para ","ateou fogo n","defenestrou ",
             "maquiou ","secou ","molhou ","enxaguou ","espirrou n","acenou para ",
             "pissoteou ","escravizou ","clonou ","pirateou ","chifrou ",
             "desembrulhou ","refletiu sobre ","converteu ","plantou ", "envenenou ",
             "cabeceou ","chutou ","sentiu ","acorrentou ","amarrou ",
             "enfeitissou ","entristeceu ","colocou fralda n","urinou n",
             "queimou ","resgatou ","deitou n","deu um tapa n"]
    
    substantivos = ["a pedra","o pepino","a goiaba","o chinelo","a banana",
                    "a bola","a arvore","o vizinho","o menino","o mendigo",
                    "o rei leao","o professor","o pirata","o sniper",
                    "o bob esponja","o patrick","o pikachu","o naruto",
                    "o barney","o hulk","o goku","o cebolinha",
                    "a caixa","o piano","a lanterna","a privada","a garrafa",
                    "o pernilongo","o biscoito","o pastel","a raquete",
                    "a cadeira","o Harry Potter","o neymar","o scooby-doo",
                    "o ninja","o cachorro","a galinha","a batata","a espada",
                    "o cafe da manha","o avatar aang","o Ash Ketchun da cidade de Pallet",
                    "o para-quedas","o batman","o homem aranha","a flor",
                    "o abajour","o desodorante","a lampada","o pato Donald",
                    "o coco","o celular","o pasteleiro","o vampiro",
                    "a maionese","o lapis","o cabelereiro","a lata de lixo",
                    "o pescador","o jardineiro","a peruca","o careca",
                    "o peixinho dourado","o avestruz","o ornitorrinco",
                    "o padre","o palhasso","a lingua","o sapato","a massaneta",
                    "o caderno","o surfador","a tarantula","o espelho",
                    "a tartaruga","o golfinho","o papelão","a canetinha",
                    "o bife","o copo","o mergulhador","o foguete",
                    "o beija-flor","o paralelepipedo","o cubão","o cachimbo",
                    "o papel higienico","o queijo","o presunto","a salsicha",
                    "a girafa","o ralador de queijo", "o Michael Jackson", "o fautao",
                    "a beterraba", "a melancia", "o ben 10", "a turma da monica", "o pica-pau",
                    "a dora aventureira", "a galinha pintadinha", "a branca de neve",
                    "a bruxa do 71", "o gato de botas","o dinossauro", "o camelo",
                    "a bisnaguinha","o berimbau","a azeitona verde", "o porco espinho",
                    "a almondega"]
    
    complemento = [" de pijama", " sem calça"," na floresta"," no banheiro", " na fazenda", " na igreja", " no quintal",
                   " em cima do telhado", " na batcaverna", " no milharal", " na caverna do dragao", " na disney",
                   " no parquinho", " em cima da goiabeira", " no busao", " na estaçao de trem", " num pais da europa",
                   " na lua", " no hospital", " no bueiro", " na cozinha", " no sofa", " na montanha russa",
                   " em cima da montanha", " na academia", " no mercado", " na fabrica de chocolate",
                   " no quarto de hospedes", " na geladeira", " na feira", " na biblioteca",
                   " no quarto dos fundos", " no castelo", " em hogwarts", " no bandeco"," no hospicio",
                   " na reunião geral", " no aquario", " na sala da EESC jr"," debaixo da mesa",
                   " dentro do armario"," debaixo da pia"," no palquinho", " no zoologico",
                   " debaixo da cama", " no pais das maravilhas"," no digimundo",
                   " no navio"," no carro"," no trem"," na casa"," no predio"]
    
    print(random.choice(verbos)+random.choice(substantivos)+random.choice(complemento))
    para = input("")
    if para != "":
        break