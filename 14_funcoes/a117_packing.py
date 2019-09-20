#!/usr/bin/python3
'''
Usando no gerador de html v3

Packing
def soma_n(*numeros): = Usando essa opcao a funcao pode aceitar
uma quantidade indevinida de argumentos
Tranformando em uma tupla
ou seja
Empacotando os parametros e passando como tupla

Unpacking
Desempacotando uma tupla ou lista e passando como parametros

'''


def soma_2(a, b):  # Funcao que aceita dois argumentos
    return a + b


def soma_3(a, b, c):  # Funcao que aceita tres argumentos
    return a + b + c


def soma_n(*numeros):  # Quantidade indefinida de argumentos
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 4, 6))

    # packing
    print(soma_n(1))
    print(soma_n(1, 1))
    print(soma_n(1, 1, 1, 1, 1, 1, 1))

    # unpacking
    tupla_nums = (1, 2, 3)
    print(soma_3(*tupla_nums))
    lista_nums = [1, 2, 3]
    print(soma_3(*lista_nums))


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 117
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
