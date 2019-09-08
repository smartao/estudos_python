#!/usr/bin/python3
# Importando o modulo pi  e utilizando
from math import pi


# Caso precise alterar o encoding padrao use a linha a baixo
# -*- coding: ISO-8859-1 -*-
# No python3 isso já não é tão relevante

if __name__ == '__main__':
    raio = input('Informe o raio: ')  # entrando com o valor do raio
    # Calculando a area do circulo
    print('Área do círculo', pi * float(raio) ** 2)

# Mostrando o nome do modulo
# print('Nome do módulo:', __name__)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 55 a 72
# https://github.com/cod3rcursos/curso-python/tree/master/fundamentos_projetos
