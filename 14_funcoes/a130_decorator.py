#!/usr/bin/python3
'''

@log usado para chamar o decorator

'''


def log(function):
    def decorator(*args, **kwargs):
        print(f'\nInicio da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5, 7))
    print(sub(5, y=7))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 130
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
