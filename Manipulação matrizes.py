def leitura_matriz(nome): #Leitura das matrizes
    matriz = []
    arquivo = open(nome, "r")
    for linha in arquivo:
        elementos = linha.split()
        linha_matriz = []
        for elemento in elementos:
            linha_matriz.append(int(elemento))
        matriz.append(linha_matriz)
    arquivo.close()
        
    return matriz

def repeticoes(matriz): #Verificar as repetições das linhas das matrizes utilizando dicionário para armazenar a quantidade de vezes que ele se repete em toda a matriz
    numeros_repetidos = {} 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] in numeros_repetidos:
                numeros_repetidos[matriz[i][j]] += 1
            else:
                numeros_repetidos[matriz[i][j]] = 1    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numeros_repetidos[matriz[i][j]] > 1:
                matriz[i][j] = 0
    return matriz

def imprimir_matriz(matriz): #imprimir a matriz linha por linha 
    for linha in matriz:
        print(linha)





a = leitura_matriz("matriz.txt")
matriz = repeticoes(a)
imprimir_matriz(matriz)




    