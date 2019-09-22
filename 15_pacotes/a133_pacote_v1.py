#!/usr/bin/python3

'''
Para a importacao de pacotes funcionar, deve exsitir o arquivo
__init__.py que faz o python entender o que é o pacote

Sobre a pasta __pycache__ que é gerada

ao importar um módulo pela primeira vez, o Python compila-o automaticamente
e grava neste diretório, acessos futuros serão mais rápidos,
a não ser que o .py original tenha sido modificado,
exigindo nova compilação (que também será automática).

'''

from pacote1 import modulo1

print(type(modulo1))
print(modulo1.soma(2, 3))


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 133
# https://github.com/cod3rcursos/curso-python/tree/master/pacotes
