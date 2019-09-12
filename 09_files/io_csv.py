#!/usr/bin/python3
#
'''
Versao de leitura de CSV

csv.reader(entrada) = dara o os dados todos mastigados
facilitando a manipulancao de arquivos





'''

import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 97 a 107
# https://github.com/cod3rcursos/curso-python/tree/master/manipulacao_arquivos
