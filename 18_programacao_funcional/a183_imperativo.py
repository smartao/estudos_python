#!/usr/bin/python3

'''

'''
from locale import setlocale, LC_ALL
from calendar import mdays, month_name

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias
print('Meses com 31 dias:')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 183
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
