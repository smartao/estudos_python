#!/usr/bin/python3
'''

from pacote2 import modulo1 as modulo1_sub

o as significa que estamos dando um apelido para o modulo1, assim
nao causando o conflito com o nome do pacote


'''

from pacote1 import modulo1
from pacote2 import modulo1 as modulo1_sub

print('Soma', modulo1.soma(3, 2))
print('Subtração', modulo1_sub.subtracao(3, 2))


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 135
# https://github.com/cod3rcursos/curso-python/tree/master/pacotes
