#!/usr/bin/python3

# Criando um dicionario
produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

# Tambem seria valido o for usando
# for chave in produto.keys():
print('\nImprimindo as chaves do diconario:')
for chave in produto:
    print(chave)

print('\nImprimindo os valores do dicionario:')
for valor in produto.values():
    print(valor)

print('\nImprimindo chaves e valores do dicionario:')
for chave, valor in produto.items():
    print(chave, '=', valor)

'''
Observação
Mesmo fora do FOR as variaves chave e valor ainda retornaram o ultimo valor
Exemplo:
'''

print('\nUltimo valor chave e estoque: ' + chave, valor)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 77 a 81
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
