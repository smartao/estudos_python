#!/usr/bin/python3
#
'''
Leitura via stream

Versao mais simpleificado usando o 'with open' com esse recuros
o arquivo sempre sera fechado automaticamente no final da execucao





'''

with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado!')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 97 a 107
# https://github.com/cod3rcursos/curso-python/tree/master/manipulacao_arquivos
