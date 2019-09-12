#!/usr/bin/python3
#
'''
Leitura via stream

Usando o try finally
O finally sempre é executado mesmo quando ocorrer um erro no codigo
Mesmo se existir o except o finally sera executado posteriomente




'''

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado!')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 97 a 107
# https://github.com/cod3rcursos/curso-python/tree/master/manipulacao_arquivos
