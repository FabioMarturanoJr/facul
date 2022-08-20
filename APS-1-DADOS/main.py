import numpy as np
import pandas as pd
import json


def program():
    # name = input("nome ? >>>")
    # print("seu nome" + name)

    matriz = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)
    print(matriz)
    print("\n")

    soma = np.sum(matriz[:, 0])  # parametro da matriz [todas as linhas : coluna 0]
    print(soma)
    print("\n")

    idades = np.array([12, 23, 32, 45, 56, 63, 75, 82, 91]).reshape(3, 3)
    mediaIdades = np.mean(idades[:, :])
    print(mediaIdades)
    print("\n")

    if mediaIdades <= 18:
        print("Pessoas novas")
    elif 18 < mediaIdades < 40:
        print("Pessoas Maduras")
    else:
        print("Pessoas Velhas")

    sequencial = np.arange(10)
    print(sequencial)
    print("\n")

    matrizSequencial = np.arange(9).reshape(3, 3)
    print(matrizSequencial)
    print("\n")

    matrizUm = np.ones((3, 3))
    matrizZero = np.zeros((3, 3))

    print(matrizUm)
    print(matrizZero)
    print("\n")

    try:
        file = np.genfromtxt('arquivo.txt', delimiter=',')
        print('arquivo carregado')
        print(file)
        print(np.sum(file[:, :]))
    except:
        print('arquivo não carregado')

    print("\n")

    try:
        loadFile = open("arquivoJson.txt", "r")
        read = loadFile.read()
        jsonData = json.loads(read)
        print('arquivo carregado')
        print(jsonData)
    except:
        print('arquivo não carregado')

    # importa json
    # abrir
    # analisar (soma, media, minimo, maximo ou contagem) 
    # analisar (if, else)
    # tirar conclusão

if __name__ == '__main__':
    program()
