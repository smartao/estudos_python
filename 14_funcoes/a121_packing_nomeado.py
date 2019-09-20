#!/usr/bin/python3
'''
Usando no gerador de html v5

**kwargs

Funcão recebe vários valores e trata como um dicionario
E também um packing recebe todos os parametos
e transforma em um dicionario para dentro da função

Criado exercicio inverso com o nome unpacking_nomeado
'''


def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 121
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
