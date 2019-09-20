#!/usr/bin/python3
'''
o assert serve para validar se o retorno é verdadeiro
caso contrário gerará uma execao

classe='success' = é um parametro opcional
Se nao for passado o valor padrao sera sucesso

'''


def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions)
    assert tag_bloco('Incluído com sucesso!') == \
        '<div class="success">Incluído com sucesso!</div>'
    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'
    print(tag_bloco('bloco'))  # Chamando a funcao

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 115
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
