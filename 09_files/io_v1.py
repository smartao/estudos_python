#!/usr/bin/python3
#
'''
Leitura mais basica
*registro.split(',') Faz com que leia todo o conteudo da variavel registro
quebre a linha com split separando por, e jogue os elementos nos devidos campos

Usando o *pessoa o python entende que deve estrair cada elemento da lista




'''

arquivo = open('pessoas.csv')  # Abrindo o arquivo
dados = arquivo.read()  # Armazendo o conteudo em variavel
arquivo.close()  # Fechando o arquivo

for registro in dados.splitlines():  # Lendo linha por linha
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 97 a 107
# https://github.com/cod3rcursos/curso-python/tree/master/manipulacao_arquivos
