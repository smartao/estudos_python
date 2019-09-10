#!/usr/bin/python3


PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:  # Correndo o dicionario pegando linha a linha
    found = False
    # Por padrao o split separa a frase por espacoes em branco
    for palavra in texto.lower().split():  # Pegando cada palavra da linha
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado:', texto)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 84 a 86
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
