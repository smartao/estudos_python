#!/usr/bin/python3

'''
Verificando se o dia passado é fim de semana ou dia de seman
Observacao
Nas aulas posteriores sera mostrando como otimizar esse dicionario
Nao precisando digitar os dias do 2 ao 6
'''


def get_tipo_dia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana',
    }
    return dias.get(dia, '** inválido **')


if __name__ == '__main__':
    for dia in range(8):  # range de 1 a 7
        print(f'{dia}: {get_tipo_dia(dia)}')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 82 a 83
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
