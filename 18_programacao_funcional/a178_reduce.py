#!/usr/bin/python3

'''
O Filter sempre para filtrar os elementos no paradigame funcional

'''
pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

# Filtrando apenas as pessoas maiores de idade
# Esse lampda sempre retornar verdadeiro ou falso, se true entra na lista nova
menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

# Filtrando as pessoas que tem o nome maior que 6 caracteres
nomes_grandes = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(tuple(nomes_grandes))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 178
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
