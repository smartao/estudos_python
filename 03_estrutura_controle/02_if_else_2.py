#!/usr/bin/python3
'''
FUNCAO RANGE
Exemplo:
range(18, 65)

Nesse caso sera gerado um nomero de 18 a 64
'''


def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'idade inválida'


if __name__ == '__main__':
    for idade in (17, 0, 35, 87, 113, -2):
        print(f'{idade}: {faixa_etaria(idade)}')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 73 a a 75
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
