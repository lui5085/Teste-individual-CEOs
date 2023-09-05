def ordenacao(lista, n): #Ordenação dos elementos usando insertion sort
    for j in range(1, n):
        x = lista[j]
        i = j-1
        while i>=0 and lista[i] > x:
            lista[i+1] = lista[i]
            i = i-1
        lista[i+1] = x
    return lista

l1 = [5, 7, 8, 3, 4]
l2 = [4, 3, 0, 9, 8]
l1f = []
for i in range(len(l2)): #Adição dos elementos da lista 2 na lista 1
    l1.append(l2[i]) 
x = 0
l1 = ordenacao(l1, len(l1)) #Ordenação da lista com todos os elementos 
for i in range(len(l2), len(l1)): #Adição dos elementos com indice maior que n(tamanho das listas originais)
    l2[x] = l1[i]
    x += 1
for i in range(0, len(l2)): #criar uma nova lista sem os n ultimos elementos que estão agora na lista 2 
    l1f.append(l1[i])

print(l1f, l2)

