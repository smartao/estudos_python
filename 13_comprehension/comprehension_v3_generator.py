#!/usr/bin/python3

'''
Trocanco colchetes por parentes
Deve ver sera o valor ao quadrado

o next mostra o próximo valor do generator

Vantagem que consome menos memoria,
Pois os dados são geradods sob demanda
'''

generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))  # Saída 0
print(next(generator))  # Saída 4
print(next(generator))  # Saída 16
print(next(generator))  # Saída 36
print(next(generator))  # Saída 64
# print(next(generator))  # Erro!

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 108 a 113
# https://github.com/cod3rcursos/curso-python/tree/master/list_comprehension
