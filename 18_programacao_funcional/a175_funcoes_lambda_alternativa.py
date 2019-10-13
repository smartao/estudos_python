#!/usr/bin/python3

'''
Semelhante ao exemplo anterior

Porem sem usar uma funcao anonima usando lampada
E sim usando uma funcao comum













'''

compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)


def calc_preco_total(compra):
    return compra['quantidade'] * compra['preco']


totais = tuple(map(calc_preco_total, compras))

print('Preços totais:', totais)
print('Total geral:', sum(totais))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 175
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
# https://is.gd/JHvlrb Python Lambda
