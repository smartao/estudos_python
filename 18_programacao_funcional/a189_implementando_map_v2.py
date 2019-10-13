#!/usr/bin/python3

'''



'''


def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == "__main__":
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(tuple(resultado))


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 189
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
