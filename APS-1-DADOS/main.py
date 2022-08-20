import numpy as np
import pandas as pd
import json


def importaArquivo(nomeArquivo): # importa o arquivo tranforma em json e retona os dados
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


def analizaNotasAlunos(notas): # analia a notas do alunos
    print('########## Notas ##########')
    print(f'Total: {np.sum(notas)}')
    print(f'Media: {np.mean(notas)}')
    print(f'Desvio Padrão: {np.sum(notas)}')
    print(f'Minimas: {np.min(notas)}')
    print(f'Maxima: {np.max(notas)}')
    print('\n')


def analizaSituacao(situacoes): # contabilida a situação dos alunos
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
    alunos = importaArquivo("arquivoJson.txt")["alunos"] # importa o arquivo e pega o conteudo a chave alunos

    print(f'Total Alunos {len(alunos)} \n')

    analizaNotasAlunos(np.array([aluno['notaFinal'] for aluno in alunos])) # seleciona dos alunos suas notas
    analizaSituacao(np.array([aluno['situacao'] for aluno in alunos])) # seleciona dos alunos suas situações


if __name__ == '__main__':
    program()
