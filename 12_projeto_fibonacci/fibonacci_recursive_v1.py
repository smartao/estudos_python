#!/usr/bin/python3

'''
Sequencia de Fibonacci usando recursividade


'''


# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:  # Importante: Condição de parada
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):  # Listar os 20 primeiros números da sequência
        print(fib)

'''
Explicacoes
equencia=(0, 1) = é o parametro padrao na funcao
Sera utilizado caso nao seja passado nenhum valor

if len(sequencia) == quantidade: # Condicao de parada
comparando a quantidade de elementos da tupla com a quantidade

Na tupla podemos somar normalmente os valores entre tuplas
(sum(sequencia[-2:]),)) = Somando os dois ultimos elementos da tuplas
na primeira execucao sera 1, na segunda, 2, na terceira 3, na quarta 5
E somando esse valor com a tupla "sequencia"
A virgula entre os parenteses é importante para definir a tupla

É usado tuplas, pois segundo o instrutor:
"Uso de lista como argumentos mutáveis é extremamente desaconselhavel"

Essa técnica de somar dois elementos tipos listas e tuplas chama-se
sobrecarga de operadores
'''

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 87 a 97
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle_projetos
