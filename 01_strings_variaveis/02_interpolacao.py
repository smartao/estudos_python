#!/usr/bin/python3

'''
Interpolarção
É substituir valores dentro da string
'''

# Criando duas variaveis
from string import Template
nome, idade = 'Ana Paula', 30.98761

# Método mais antigo, menos recomendado!
#
# %s = sequencia de caracteres que sera interpretado pelo python
# para substuir elementos do tipo string
# %d = usado para substituir valores inteiros
# %f = usando para substiuir valores float
print('\nSubstituindo valores variaveis, método antigo:')
print('Nome: %s, Idade: %d' % (nome, idade))
print('\nSubstitindo valores float e limitando as casas deciamais:')
print('Nome: %s, Idade: %.2f' % (nome, idade))

# Método utilizado no Python 3.6 ou inferior
print('\nMetodo de interpolacao python 3.6 ou inferior:')
print('Nome: {0} Idade: {1}'.format(nome, idade))

# Método mais novo de todos, suporta apenas Python 3.6 ou superior
# Chamando f-string
print('\nMetodo de interpolacao python 3.6 ou superior:')
print(f'Nome: {nome} Idade: {idade}')
# Adicioando valores e formatando mostrando apenas duas casas deciamias
print(f'Idade de {nome} daqui 10 anos = {idade+10:.2f}')

# Método usando template, necessário configurar o import

print('\nMetodo usando template:')
s = Template('Nome: $n Idade: $ida')
print(s.substitute(n=nome, ida=idade))

#
# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 54
# https://github.com/cod3rcursos/curso-python/tree/master/fundamentos
# https://realpython.com/python-f-strings/
# https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
