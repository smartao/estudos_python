#!/usr/bin/python3

'''
Recursao
Nada mais é um método que chama ele mesmo.
Por isso é muito importante que exista em algum momento uma condição de parada!
No exemplo o máximo de recursividade que o python suporta é 997

Muitas vezes podemos subistuir um laço por uma implementação recursiva
'''


def imprimir(maximo, atual):
    # condição de parada!
    if atual < maximo:
        print(atual)
        imprimir(maximo, atual + 1)


imprimir(990, 1)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 87 a 97
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle_projetos
