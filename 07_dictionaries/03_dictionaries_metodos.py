#!/usr/bin/python3
#
import pprint
'''
get()
Os dicionario tem o método get() que aceita dois argumentos:
a chave do valor a ser obtido e um valor alternativo a ser retornando
    se essa chave nao existir
'''
picnicitems = {'apple': 5, 'cups': 2}
print('Exemplo do metodo get')
print('Eu trouxe ' + str(picnicitems.get('cups', 0)) + ' cups')
# Testando com item que nao existe
print('Eu trouxe ' + str(picnicitems.get('eggs', 0)) + ' eggs')

'''
setdefault()
Com frequencia, sera necessário definir um valor em um dicionário
para uma chave especifica seomente se essa chave ainda nao tiver um valor
'''
# Criando o dicionario de defirnindo um valor padrao
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print('\n Exemplo do setdefault')
print(spam)  # Imprimindo o valor

'''
pptrin() ppformat()
Se o módulo pptrint form importado em seus programas voce tera acesso
a esses dois métodos, que farão uma "Apresentacao elegante"
Isso sera conveniente quando quiser uma apresentação mais limpar dos
itens de um dicionário
'''
# Criando uma menssagem
message = 'It was a bright cold day in April,\
    and the clocks were stringking thirteen.'

count = {}  # Criando dicionario vazio, para armazenar contagem

# Usando o método setdefault para garantir que a chave existe no dicionario
# Ou seja na primeira contagem sera 0
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print('\nExemplo do metodo pprint')
pprint.pprint(count)
#
# Fontes:
# Livro Automatiza tarefas maçantes com Python Posicao 3304 a 3368
