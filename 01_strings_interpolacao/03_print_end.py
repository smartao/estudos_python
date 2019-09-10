#!/usr/bin/python3

'''
O padrao do print é que no final do comando ocorra um /n
e assim sera pulado uma linha no final
Para altera o padrao basta usar: end="qualquer coisa"
Podendo usar qualquer string para ser o final da linha
, . "" (espaco) xxxx etc

Alguns exemplos:
'''

palavra = "paralelepipedo"

print('\nExemplo padrao de print imprimindo uma letra por linha')
for letras in palavra:
    print(letras)

print('\nExemplo do print usando delimitador a ,')
for letras in palavra:
    print(letras, end="FI")

print('\n\nExemplo do print usando delimitador a ,')
for letras in palavra:
    print(letras, end=",")

print('\n\nExemplo do print usando delimitador o espaco')
for letras in palavra:
    print(letras, end=" ")

print('\n\nExemplo do print usando sem delimitador')
for letras in palavra:
    print(letras, end="")

print('\n')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 78
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
