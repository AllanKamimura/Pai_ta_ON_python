prod, que = input("").split()
prod, que = map(int, [prod,que])
price = {}
rel= {}
L = []
for a in range(0,prod):
    i,p,r = input("").split()
    price[int(p)] = i
    rel[int(r)] = i
    
L = list(price.values())
    
for b in range(0,que):
    query = input("")
    if query[0] == "i":
        coisa,num = query.split()
        num = int(num)
        if len(L[num-1][1]) == 1:
            print(L[num-1])
        else:
            print(L[num-1][1])
    elif query == "ordenar_maior_preco":
        L = sorted(price.items(), key=lambda x: x[0], reverse = True)
    elif query == "ordenar_menor_preco":
        L = sorted(price.items(), key=lambda x: x[0])
    else:
        L = sorted(rel.items(), key=lambda x: x[0], reverse = True)