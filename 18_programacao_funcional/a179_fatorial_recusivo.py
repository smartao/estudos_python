#!/usr/bin/python3

'''


'''


def fatorial(n):
    return n * (fatorial(n - 1) if (n - 1) > 1 else 1)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')

    # 6 semanas em sugundos é igual a 10!
    print(6 * 7 * 24 * 60 * 60)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 179 e 180
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
