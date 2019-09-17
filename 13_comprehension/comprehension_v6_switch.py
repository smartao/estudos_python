#!/usr/bin/python3

'''
dia_escolhido = () Criando um Generator
tipo for, retornara apenas a descricao
numeros é a tupla, tipo é a string
dias.items, percorre a chave e o valor do dicionario ao mesmo tempo
if dia in numeros, validando se o dia esta dentro das duplas,
    pois o dia é um parametro que sera passado
** dia inválido ** parametros de return defaul caso nao retorno nada
'''


def get_tipo_dia(dia):
    dias = {  # Dicioinario que contem uma tupla
        (1, 7): 'Fim de semana',  # dia 1 e 7 = fim de semana
        tuple(range(2, 7)): 'Dia de semana',  # 2 a 6 = dia de semana
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** dia inválido **')


if __name__ == '__main__':
    for dia in range(0, 9):  # Criando um for simples
        # Chamando a funcao e passando os parametros (dia)
        print(f'{dia}: {get_tipo_dia(dia)}')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 108 a 113
# https://github.com/cod3rcursos/curso-python/tree/master/list_comprehension
