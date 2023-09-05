def ordenacao(lista, n): 
    for j in range(1, n):
        x = lista[j]
        i = j-1
        while i>=0 and lista[i] < x:
            lista[i+1] = lista[i]
            i = i-1
        lista[i+1] = x
    return lista
l1 = [1, 3, 3, 4, 5]
l2 = [4, 3, 0, 5, 8]
if len(l1) != len(l2):
    print("As listas não são permutações")
else:
    l1 = ordenacao(l1, len(l1))
    l2 = ordenacao(l2, len(l2))
    contador = 0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            contador += 1
    if contador == len(l1):
        print("As listas são permutações")
    else:
        print("As listas não são permutações")


        
