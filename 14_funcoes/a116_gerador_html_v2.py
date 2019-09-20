#!/usr/bin/python3
'''
o assert serve para validar se o retorno é verdadeiro
caso contrário gerará uma execao

classe='success' = é um parametro opcional
Se nao for passado o valor padrao sera sucesso

'''


def tag_bloco(texto, classe='success', inline=False):
    # Usando operador ternario
    # span se = inline
    # se não = div
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    #  Passando apenas o pametros obrigatorio
    print(tag_bloco('bloco'))
    # Passando todos os parametros na ordem correta
    print(tag_bloco('inline e classe', 'info', True))
    # Bulando a ordem, inline sendo o segundo parametro
    print(tag_bloco('inline', inline=True))
    # Usando parametros nomeados para ignorar a ordem
    print(tag_bloco(inline=True, texto='inline'))
    print(tag_bloco('falhou', classe='error'))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 116
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
