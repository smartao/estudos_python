#!/usr/bin/python3
#
'''
Versao mais simplificada usando o 'with open' com esse recuros
o arquivo sempre sera fechado automaticamente no final da execucao

with open('pessoas.txt', 'w') as saida:
w = Abrindo em modo de escrita
as saida = escrita sera salva no arquivo com esse novo

print (.... file=saida) fazendo o print gravar em um arquivo
ao inves da tela
'''

with open('pessoas.csv') as arquivo:  # Abrindo o arquivo .csv
    with open('pessoas.txt', 'w') as saida:  # Abrindo no modo de edicao .txt
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado!')

if saida.closed:
    print('Arquivo de saída já foi fechado!')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 97 a 107
# https://github.com/cod3rcursos/curso-python/tree/master/manipulacao_arquivos
