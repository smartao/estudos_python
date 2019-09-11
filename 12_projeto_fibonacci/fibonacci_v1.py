#!/usr/bin/python3

'''
Sequencia de Fibonacci simples que executa em um laco infinito
'''


# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 87 a 97
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle_projetos
