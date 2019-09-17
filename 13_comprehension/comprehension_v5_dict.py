#!/usr/bin/python3

'''
Dicionarios = trocar parenteses por chaves
i: é a chave do dicionario
i * 2 = É o valor da chave de i

'''

# Exemplo mais complexo
dicionario = {f'Item {i}': i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)

# Exemplo mais simples
dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)


for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 108 a 113
# https://github.com/cod3rcursos/curso-python/tree/master/list_comprehension
