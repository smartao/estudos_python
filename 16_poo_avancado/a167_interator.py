#!/usr/bin/python3

'''



'''


class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    def __iter__(self):  # Transformando em um interetor
        return self  # Permiti adicionar no for

    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:  # Opcional
            raise StopIteration()


if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

    try:
        print(next(cores))
    except StopIteration:
        print('Acabou!')

    for cor in RGB():
        print(cor)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 167
# https://github.com/cod3rcursos/curso-python/tree/master/poo_avancada
