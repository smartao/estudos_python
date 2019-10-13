#!/usr/bin/python3

'''
O map é uma função interna do Python
que serve para você aplicar uma função em todos os elementos de uma lista,

A funcao map aboserver um for, um append de uma lista

Fornece uma facilidade muito grande em transformar uma lista em outra lista ou
uma tupla em outra tupla e vise versa, sempre trabalhando com dados imutaveis

'''

lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]
so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

so_idades = map(lambda p: p['idade'], lista_2)
print(sum(so_idades))

# Desafio: usando map retorne frases '<Nome> tem <idade> anos.'
frases = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', lista_2)
print(list(frases))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 176
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
# https://pythonhelp.wordpress.com/2012/05/13/map-reduce-filter-e-lambda/
