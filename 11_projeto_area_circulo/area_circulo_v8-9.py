#!/usr/bin/python3
from math import pi


def circulo(raio):  # Funcao que retorna o raio
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('Área do círculo', area)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 55 a 72
# https://github.com/cod3rcursos/curso-python/tree/master/fundamentos_projetos
