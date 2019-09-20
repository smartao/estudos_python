#!/usr/bin/python3
'''
Pegando todos os parametros

Um argumento pocisional sempre deve estar antes de parametros nomeados

def todos_params(*args, **kwargs):
    Significa que quer pegar os argumentos de uma forma genérica
    tanto pocisionais quanto os nomeados
'''


def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    # 3 parametros posicionais
    todos_params('a', 'b', 'c')
    # 3 parametros pocisinais + 2 nomeados
    todos_params(1, 2, 3, legal=True, valor=12.99)
    # 3 parametros posicionais + 2 nomeados
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    # 2 parametros nomeados
    todos_params(primeiro='João', segundo='Maria')
    # 1 parametro pociaional + 1 nomeados
    todos_params('Maria', primeiro='João')
    # Forma incorreto, passando parametro pocional depois do nomeado
    # todos_params(primeiro='João', 'Maria')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 124
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
