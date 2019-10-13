#!/usr/bin/python3

'''
Lampada = funcoes anonimas
Sintaxe
Lambda <parâmetros>: <função>(argumentos)
A função já processa os argumentos e retorna o resultado. Exemplos:

(lambda a: a)(5)
5
(lambda a, b: a * b)(5, 3)
15
(lambda a, b: '{} * {} é {}'.format(a, b, a * b))(5, 3)
'5 * 3 é 15'
A função anônima teve que ficar entre parênteses pra permitir
que os argumentos sejam passados pra ela,
e não pro último termo da função (a e b, nos 2 primeiros casos).

Com essa experiência, agora deu pra entender como a função lambda funciona,
e o que ela faz dentro do map, no exemplo da lição.
'''

compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)

print('Preços totais:', totais)
print('Total geral:', sum(totais))

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 174
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
# https://is.gd/JHvlrb Python Lambda
