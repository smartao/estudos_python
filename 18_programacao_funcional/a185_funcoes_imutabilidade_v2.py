#!/usr/bin/python3

'''
Alterando a lista por uma tupla para os dados nao serem mutaveis

'''

from functools import reduce
from operator import add

valores = (30, 10, 25, 70, 100, 94)

print(sorted(valores))
print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(tuple(reversed(valores)))
print(valores)


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 185
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
