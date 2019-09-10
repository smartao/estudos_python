#!/usr/bin/python3


from random import randint

numero_teste = -1
numero_secreto = randint(0, 9)

while numero_teste != numero_secreto:
    numero_teste += 1
    print(f'Testando o numero {numero_teste}')

print('Número secreto {} foi encontrado!'.format(numero_secreto))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 76
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
