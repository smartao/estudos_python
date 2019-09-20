#!/usr/bin/python3
'''
Resolvendo problema de parametros defaul mutaveis

A sulucao foi aplicada na seguinte linha
sequencia = sequencia or [0, 1]

Ou entao voltar a usar a tupla



'''


def fibonacci(sequencia=None):
    # Se a sequencia for nulo (none) sequencia recebera 0 e 1
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()  # Chamando funcao e armazenando o valor
    print(inicio, id(inicio))  # Imprimindo valo r id do objeto
    print(fibonacci(inicio))  # Chamando a segunada vez a funcao
    restart = fibonacci()  # Reexecutando a sequencia de fibonacci
    # Imprimindo o objeto gerado novamente
    # Perceba que nesse agora o ID esta diferente
    print(restart, id(restart))
    assert restart == [0, 1, 1]  # A lista esperada era a 0, 1, 1


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 127
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
