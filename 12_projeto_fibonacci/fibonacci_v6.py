#!/usr/bin/python3

'''
Sequencia de Fibonacci mostrando uma quantidade X
de elemeentos da sequencia

Substituindo utilizando o break como parada


'''


# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 87 a 97
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle_projetos
