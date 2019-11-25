#!/usr/bin/python3
#
'''
Leitura via stream

Resolvendo a questao da linha em branco na impressoa

Usamos o .strip, para remover
Ele server tambem para remover caracteres nas bordas das strings

Exemplo na pasta

'''

arquivo = open('pessoas.csv')  # Abrindo o arquivo
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 97 a 107
# https://github.com/cod3rcursos/curso-python/tree/master/manipulacao_arquivos
