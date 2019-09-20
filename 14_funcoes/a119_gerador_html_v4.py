#!/usr/bin/python3
'''
def tag_bloco(conteudo, *args, classe='success', inline=False):
A partir do momento que utilizamos argumentos, or argumentos posicionais nao
funcionaram mais deveram ser utilizados argumentos nomeados!
DE  : print(tag_bloco('inline e classe', 'info', True))
PARA: print(tag_bloco('inline e classe', classe='info', inline=True))

html = conteudo if not callable(conteudo) else conteudo(*args)
Conforme visto no callable
html recebe conteudo se nao for um callable, ou seja uma funcao
se for uma callable, entao executara a funcao conteudo

'''


def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    # Utilizando o callable, taglista
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo',
                    classe='info', inline=True))


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 119
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
