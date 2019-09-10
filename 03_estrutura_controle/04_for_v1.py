#!/usr/bin/python3

'''
FOR
Laço utilizando para quando sabemos o tamanho exato que deve ser executado
Ex:
Correr um dicionario inteiro
Percorrer um tupla
etc
'''

print('\nImprimindo de 1 a 10')
for i in range(1, 11):
    print('i = {}'.format(i))

print('\nImprimindo de 1 a 10 metodo 2')
for j in range(10):  # range inicializara do 0
    print(f'j = {j}')

print('\n\n')
for x in range(1, 11):
    print(f'\nTabulado do: {x}')
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 77 a 81
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
