#!/usr/bin/python3

'''
Semelhante a versao 1 do programa
Porem utilizando o else, veja que nao é necessário a variavel de controle found
'''

PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            break
    else:
        print('Texto autorizado:', texto)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 84 a 86
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
