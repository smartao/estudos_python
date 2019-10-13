#!/usr/bin/python3

'''


'''

from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

print(sorted(valores))
print(valores)

# valores.sort()
# print(valores)
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(list(reversed(valores)))
print(valores)

# valores.reverse()
# print(valores)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 184
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
