#!/usr/bin/python3

'''
While
Normalmente utilizado quando a laço deve ser executado de forma indeterminada
'''

# Whire infitino!
# while True:
#     print('Vai demorar muitooooo')

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número: '))

print('Número secreto {} foi encontrado!'.format(numero_secreto))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 76
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
