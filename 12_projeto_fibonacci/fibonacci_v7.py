#!/usr/bin/python3

'''
Sequencia de Fibonacci
Substituindo o laço while pelo for
2, quantidade = é necessário pois a lista já inicia com 2 elementos!

Outra forma de fazer o laço for for _ in range(quantidade - 2):
_ = significado variavel que não esta sendo usada
'''


# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):  # Começando do segundo elemento
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 87 a 97
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle_projetos
