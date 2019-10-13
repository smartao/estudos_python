#!/usr/bin/python3

'''
Clousure = fechamento
Significad que a funcao tem conciencia do seu proprio escopo além do escopo
ao seu redor o local que a funcao foi definida
a funcao calcula consegue identificar o x que foi passado como
parametro para assim fazer os calculos
Escopo interno (inter scope) e escopo externo (alter escope)

No exemplo de multiplar também contem o conceito de avaliacao tardia.
O carculo só sera retornando, quando passarmos os 2 parametros
    dobro = multiplicar(2)
A linha em cima em si nao faz nada apenas retorna a funcao calcular mas
ainda depende da segundo parametro
'''


def multiplicar(x):
    def calcular(y):  # nao possui o x, mas ele esta armazenado
        return x * y
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro)
    print(triplo)
    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 7 é {dobro(7)}')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 173
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
