#!/usr/bin/python3
from math import pi
import sys  # Importando funcao para ler argumento direto do terminal
import errno


'''
ARGUMENTOS import sys
O primeiro argumento [0] sempre o nome do script,
    nesse caso ./area_circulo_v10-14.py
O segundo argumento [1] sera o digitado no terminal
    apos chamar o programa

Mensagem de erros import errno
errno.EPERM = Operacao nao permitida
errno.ENOENT = Diretorio ou arquivo nao encontrado
errno.EINVAL = Argumento invalido

Sobre:
https://docs.python.org/2/library/errno.html
'''

'''
Criado a classe TerminalColor
Apenas para as cores nao ficarem no escopo global
'''


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print("É necessário informar o raio do círculo.")
    # [2:] = Cortando os dois primeiros (./) caracteres do argumento
    print("Sintaxe: {} <raio>".format(sys.argv[0]))


def circulo(raio):  # Funcao que retorna o raio
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:  # Se o numero de argumentos for menor que 2
        help()
        sys.exit(errno.EPERM)  # saindo do programa com mensagem

    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO +
              'O Raio deve ser uma valor numerico' +
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo', area)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 55 a 72
# https://github.com/cod3rcursos/curso-python/tree/master/fundamentos_projetos
