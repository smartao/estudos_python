#!/usr/bin/python3

'''
'''


def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


spam()

'''
Exemplo de saida, leia-se de cima para baixo!
Execao ocorreu na linha 12, mostrando o tipo que foi
que foi chamado na linha 8, pela funcao bacon()
que foi chamado pela linha 15 pela funcao spam()

Traceback (most recent call last):
  File "03_errorExample.py", line 15, in <module>
    spam()
  File "03_errorExample.py", line 8, in spam
    bacon()
  File "03_errorExample.py", line 12, in bacon
    raise Exception('This is the error message.')
Exception: This is the error message.
'''

# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 10
