#!/usr/bin/python3

'''
Generator = trocanco colchetes por parenteses

Utilizando o for que já entende que é um generator
'''

generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 108 a 113
# https://github.com/cod3rcursos/curso-python/tree/master/list_comprehension
