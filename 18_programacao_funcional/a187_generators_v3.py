#!/usr/bin/python3

'''



'''


def sequence():
    num = 0
    while True:
        num += 1
        yield num


if __name__ == '__main__':
    seq = sequence()

    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 187
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
