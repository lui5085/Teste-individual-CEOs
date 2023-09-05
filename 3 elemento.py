def ordenacao(lista, n): #O(n) no melhor caso e O(n^2) no pior caso
    for j in range(1, n):
        x = lista[j]
        i = j-1
        while i>=0 and lista[i] < x:
            lista[i+1] = lista[i]
            i = i-1
        lista[i+1] = x
    return lista

lista = []
while True: #Adição de elementos em uma lista até que ela tenha no mínimo 3 elementos O(n)
    a = input("Digite o número que você quer adicionar na lista\nSe quiser parar de adicionar digite a letra X\n") 
    if a == "x" or a == "X":
        if len(lista) < 3:
            for i in range(len(lista), 3):
                a = input("Sua lista nao tem 3 elementos digite outro numero que quer adicionar na lista\n")
                lista.append(int(a))
            while True:
                a = input("Agora sua lista tem 3 elementos.\nSe quiser parar de adicionar numeros digite x\nSe nao, digite o numero que quer adicionar na lista\n")
                if a == "x" or a == "X":
                    break
                lista.append(int(a))
        break
    lista.append(int(a)) 


lista = ordenacao(lista, len(lista))
print("O terceiro maior elemento da lista é %s" %lista[2]) #Como a lista está organizada, o 3 elemento é sempre o terceiro maior, O(1)




