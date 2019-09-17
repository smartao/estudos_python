#!/usr/bin/python3

'''
List Comprehension
Nada mais é em resumo criar listas de uma forma mais concisa
Usando sintaxe do python para criar lista de uma forma muito rapida
a partir de uma única linha


Exemplo
Método tradiciona
Criar um lista com elementos especificos
1 - Criar a lista vazio
2 - Criar um laço + append para adiconar elementos a essa lista
3 - Demais passos para criar a lista

Método list Comprehension
Criar uma lista em uma única linha

[ ] = criando o list comprehension
funciona igual o for

i * 2 = expressao
for i in range(10) = laço

Mostrará o dobro do valores do range 1 A 9
'''

# [ expressão for item in list ]
dobros = [i * 2 for i in range(10)]
print(dobros)

# Versão "normal"
dobros = []
for i in range(10):
    dobros.append(i * 2)
print(dobros)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 108 a 113
# https://github.com/cod3rcursos/curso-python/tree/master/list_comprehension
