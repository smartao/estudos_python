#!/usr/bin/python3
'''

Usanado parametros posicionais

passar dois parametros para a funcao, é feito o packing
retornar dois parametros para chamar a funcao unpacking


'''


def calc_preco_final(preco_bruto, calc_imposto, *params):
    return preco_bruto + preco_bruto * calc_imposto(*params)  # Unpacking


def imposto_x(importado):
    return 0.22 if importado else 0.13


def imposto_y(explosivo, fator_mult=1):
    # Se explosivo = true faça o calculo se nao valor sera 0
    return 0.11 * fator_mult if explosivo else 0


if __name__ == '__main__':
    preco_bruto = 134.98
    # Nas duas linhas sera calculado o valor do preoduto com dos 2 impostos
    preco_final = calc_preco_final(preco_bruto, imposto_x, True)
    preco_final = calc_preco_final(preco_final, imposto_y, True, 1.5)  # Packin
    print(f'Preço final R$ {preco_final}')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 122
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
