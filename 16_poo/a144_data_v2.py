#!/usr/bin/python3

'''

def __init__(self, dia=1, mes=1, ano=1970):
é um construtor da classe, e python nao permite que tenha mais do
que um por classe, contudo pode-se usar parametro padrao no chamada
do objeto

'''


class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2019
print(d1)

d2 = Data(ano=2022, mes=12)
d2.dia = 12
# d2.mes = 11
# d2.ano = 2020
print(d2)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 144
# https://github.com/cod3rcursos/curso-python/tree/master/poo
