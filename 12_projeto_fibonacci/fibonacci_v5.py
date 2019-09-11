#!/usr/bin/python3

'''
Sequencia de Fibonacci com limite de 20mil

Utilizando a funcao soma
-2: = somara os dois ultimos elmentos da lista


'''


# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 87 a 97
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle_projetos
