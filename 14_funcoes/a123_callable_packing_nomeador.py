#!/usr/bin/python3
'''

Usando **kargs = **params, deveremos passsar parametros nomeados
Linhas 25 e 26
Nesse caso o código fica mais legivel do que usando parametros posicionais
como no arquivo callable_packing.py
'''


def calc_preco_final(preco_bruto, calc_imposto, **params):
    return preco_bruto + preco_bruto * calc_imposto(**params)


def imposto_x(importado):
    return 0.22 if importado else 0.13


def imposto_y(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0


if __name__ == '__main__':
    preco_bruto = 134.98
    preco_final = calc_preco_final(preco_bruto, imposto_x, importado=True)
    preco_final = calc_preco_final(preco_final, imposto_y,
                                   explosivo=True, fator_mult=1.5)
    print(f'Preço final R$ {preco_final}')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 123
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
