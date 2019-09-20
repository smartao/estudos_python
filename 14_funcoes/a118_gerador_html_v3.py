#!/usr/bin/python3
'''
lista = ''.join(f'<li>{item}</li>' for item in itens)

''.join serve para concatenar o conteudo de uma string


'''


def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    # Chamando uma funcao dentro da outra
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 118
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
