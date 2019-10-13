#!/usr/bin/python3

'''



'''


def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'índigo'
    yield 'violeta'


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:
        print(next(generator))


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 186
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
