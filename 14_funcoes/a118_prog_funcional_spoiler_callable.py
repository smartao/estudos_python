#!/usr/bin/python3
'''
def executar(funcao): = Criando a funcao executar
if callable(funcao): = Validando se o objeto é tipo de uma funcao
funcao() = Executando a funcoa recebida
'''


def executar(funcao):
    if callable(funcao):  # server para ingorar o parametro (1)
        funcao()


def bom_dia():
    print('Bom dia!')


def boa_tarde():
    print('Boa tarde!')


if __name__ == '__main__':
    executar(bom_dia)  # Passando como parametro a funcao bom_dia
    executar(boa_tarde)
    executar(1)  # Sera ignorado pois nao existe uma funcao com 1

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 118
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
