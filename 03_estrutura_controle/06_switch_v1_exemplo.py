#!/usr/bin/python3

'''
No python nao existe por padrao a estrutura de switch!
Contudo podemos simular essa estrutura criando uma funcao e um dicionario

get_dia_semana é uma funcao
dias é um dicionario com chave numero, e valor os os dias da semana

veja que no return caso o dia nao esteja no dicionario
retornamos o valor ** inválido **

O for da linha 34 percorerra 0 a 8
e passara esses valores na linha 35 para essa funcao
a funcao retornara os valores e sera impresso

'''


def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    return dias.get(dia, '** inválido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 82 a 83
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
