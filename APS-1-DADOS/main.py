import numpy as np
import pandas as pd
import json


def importaArquivo(nomeArquivo):
    try:
        loadFile = open(nomeArquivo, "r")
        read = loadFile.read()
        jsonData = json.loads(read)
        print('arquivo carregado')
        print(jsonData)
        print('\n')
        return jsonData
    except:
        print('arquivo não carregado')


def analizaNotasAlunos(notas):
    print('########## Notas ##########')
    print(f'Total: {np.sum(notas)}')
    print(f'Media: {np.mean(notas)}')
    print(f'Desvio Padrão: {np.sum(notas)}')
    print(f'Minimas: {np.min(notas)}')
    print(f'Maxima: {np.max(notas)}')
    print('\n')


def analizaSituacao(situacoes):
    aprovado = 0
    reprovado = 0
    trancado = 0

    for situacao in situacoes:
        if situacao == "aprovado":
            aprovado += 1
        if situacao == "reprovado":
            reprovado += 1
        if situacao == "trancado":
            trancado += 1

    print('########## Situações ##########')
    print(f'Aprovados {aprovado}')
    print(f'Reprovados {reprovado}')
    print(f'Trancados {trancado}')


def program():
    alunos = importaArquivo("arquivoJson.txt")["alunos"]

    analizaNotasAlunos(np.array([aluno['notaFinal'] for aluno in alunos]))
    analizaSituacao(np.array([aluno['situacao'] for aluno in alunos]))


if __name__ == '__main__':
    program()
