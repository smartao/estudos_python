#!/usr/bin/python3
'''
Usando no gerador de html v5

**kwargs

Unpacking de dicionario, passando o dicionario e
desempacotanto ele

Criado exercicio inverso com o nome packing_nomeado
'''


def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == '__main__':
    podium = {'segundo': 'M. Verstappen',
              'primeiro': 'L. Hamilton',
              'terceiro': 'S. Vettel'}
    resultado_f1(**podium)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 121
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
