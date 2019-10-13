#!/usr/bin/python3

'''
Funcao de alta ordem (High order)
Uma funcao retorna outra funcao







'''

from a171_funcao_primeira_classe import dobro, quadrado

# Importante validar se é a funcao é um collable


def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))


if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrados de 1 a 10', range(1, 11), quadrado)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 172
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
