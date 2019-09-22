#!/usr/bin/python3

'''

Acessando um unico pacote que agrupe multiplas funcionalidades

Esse tecnica se chama façade
Objetivo é simplificar o acesso aos objetos ou
até mesmo simplificar o codigo
'''

from calc import soma, subtracao

print('Soma', soma(3, 2))
print('Subtração', subtracao(3, 2))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 137
# https://github.com/cod3rcursos/curso-python/tree/master/pacotes
