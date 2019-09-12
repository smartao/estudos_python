#!/usr/bin/python3
#
'''
### Desafio de request de url ###
Extrair o nono e o quarto campos do arquivo CSV
sobre região de influencia das Cidades
Ignorar a primeira linha que é o cabechalho do arquivo

 dados = entrada.read().decode('latin1')
Arquivo IBGE esta no formato ISO-8859-1 (aka latin1)
Essa linha baixa o arquivo para a memoria do computador

 for cidade in csv.reader(dados.splitlines()):
Sem o uso do splitlines,
o csv.reader vai processar caracter por caracter (e não linha por linha),
desde forma a variável linhas sempre terá apenas um elemento,
e por isso linhas[8] ou linhas[3] vai levantar a exceção:
    list index out of range

9 Coluna = Indice 8
4 Coluna = Indice 3

 read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
Faz com que o python nao interprete de forma indevida os caracteres
da url exemplo de uso, imprimindo o caractere \n

print(\\n\\n\\n)  # OU
print(r'\n\n\n')
'''

import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 97 a 107
# https://github.com/cod3rcursos/curso-python/tree/master/manipulacao_arquivos
