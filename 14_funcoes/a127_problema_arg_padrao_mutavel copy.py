#!/usr/bin/python3
'''
Demostração sobre problema de parametros padrao mutaveis no python

No exemplo estamos usando a sequencia de fibonacci
    usando lista ao inves da tupla para demonstrar o problema

Aviso!
Não é interessante colocar objetos mutaveis como parametro padrao de uma funcao

Na proximo aula sera mostrando como resolver essa questao
'''


def fibonacci(sequencia=[0, 1]):
    # ### Uso de mutáveis como valor default (armadilha) ####
    # Somando os dois ulitmos valores e adicionando na lista
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()  # Chamando funcao e armazenando o valor
    print(inicio, id(inicio))  # Imprimindo valo r id do objeto
    print(fibonacci(inicio))  # Chamando a segunada vez a funcao
    restart = fibonacci()  # Reexecutando a sequencia de fibonacci
    # Imprimindo o objeto gerado novamente
    # Perceba que nesse caso e o mesmo do chamado anteriormente
    print(restart, id(restart))
    assert restart == [0, 1, 1]  # A lista esperada era a 0, 1, 1


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 127
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
