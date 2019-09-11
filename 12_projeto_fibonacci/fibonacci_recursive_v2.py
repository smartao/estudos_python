#!/usr/bin/python3

'''
Sequencia de Fibonacci usando recursividade

Com operadores Ternarios possibilitando usar tudo na mesma linha
'''


# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade, sequencia=(0, 1)):
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 87 a 97
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle_projetos
