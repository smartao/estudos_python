#!/usr/bin/python3

'''
Sequencia de Fibonacci com limite de 20mil
e swap de varaiveis na linha 18

O swap faz o codigo ficar bem mais enxuto
visto que nao precisamos da variavel extra
porem tome cuidado para nao deixar o codigo confuso
'''


# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=',')


if __name__ == '__main__':
    fibonacci(20000)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 87 a 97
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle_projetos
