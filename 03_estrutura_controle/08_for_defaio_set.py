#!/usr/bin/python3

'''
Semelhantes aos scripts for_sem_else_v1 e for_com_else_v2
Porem usando conjunto,set
Ficando bem mais simples de entender

Explicacao das linhas 26 e 27
    Chamamos o metodo intersection do conjunto PALAVRAS_PROIBIDAS
    Ele precisa de outro conjunto para funcionar
    Usando o set, transformandomos o variavel texto em um conjunto
    Usando o lower para ficar tudo minusculo e o
    split para cortar a frase em palavras pelo espacoes em branco
    Caso a variavel intersecao nao tenha nenhum valor o python
    interpretara como Falso caso contrário vendadeiro
'''

# Criando um conjunto
PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas:', intersecao)
    else:
        print('Texto autorizado:', texto)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 84 a 86
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
