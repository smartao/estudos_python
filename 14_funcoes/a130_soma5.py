#!/usr/bin/python3
'''
def soma(a, b):
    Funcao que recebe dois parametros
    No entanto o retorna dela é a funcao soma_c! (return soma_c)
dev soma_c(c)
    funcao que recebe 1 parametro
    e faz o calculado dos dois parametros anteriores + o novo passado
        funcao tera acesso devido a heranca

soma_5 = soma(2, 3)
    Executa a funcao soma e o retorno sera a funcao soma_c
    nesse caso soma_5 =  a funcao soma_c
soma_5(5)
    Executando a funcao soma_c passando parametro 5, totalizando 10

print(soma(2, 3)(5))
    Forma otimizado de executar as duas funcoes sequenciamente

'''


def soma(a, b):
    def soma_c(c):
        return a + b + c
    return soma_c


soma_5 = soma(2, 3)
print(soma_5(5))  # Forma detalhada
print(soma(2, 3)(5))  # Forma resumida


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 130
# https://github.com/cod3rcursos/curso-python/tree/master/funcoes
