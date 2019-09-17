#!/usr/bin/python3

'''
i * 2 - expressao
for i in range(10) - laço
if i % 2 == 0 - condicional

Mostrará o dobro do valores do range 1 A 9
Apenas de valores pares
'''

# [ expressão for item in list if condicional ]
dobros_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobros_dos_pares)

# Versão "normal"
dobros_dos_pares = []
for i in range(10):
    if i % 2 == 0:
        dobros_dos_pares.append(i * 2)
print(dobros_dos_pares)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 108 a 113
# https://github.com/cod3rcursos/curso-python/tree/master/list_comprehension
