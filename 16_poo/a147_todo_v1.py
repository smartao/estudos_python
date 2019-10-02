#!/usr/bin/python3
from datetime import datetime

'''








'''


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))

    # Desafio -> 'Lavar prato'
    # Marcando tarefa como concluida usando List comprehension
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']

    # Imprimindo as tarefas
    for tarefa in casa:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 147
# https://github.com/cod3rcursos/curso-python/tree/master/poo
