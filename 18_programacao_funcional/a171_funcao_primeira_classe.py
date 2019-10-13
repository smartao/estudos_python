#!/usr/bin/python3

'''
Funcao que armazena uma variavel, é uma funcao de primeira ordem
ou first class

No inicio da aula é explicado os conceitos da funcao zip

O Python permite trabalhar com duas funcoes como se fosse dados


funcs = [dobro, quadrado] * 5 = Armazenando as duas funcoes dentro lista
e * 5 sera remetido os elementos 5 vezes, total 10 elementos


'''


def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


if __name__ == '__main__':
    d = dobro
    print(d(5))

    q = quadrado
    print(q(5))

    # Retornar alternadamente o dobro ou quadrado nos números de 1 a 10
    funcs = [dobro, quadrado] * 5
    for func, numero in zip(funcs, range(1, 11)):
        print(f'O {func.__name__} de {numero} é {func(numero)}')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 171
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
