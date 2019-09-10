#!/usr/bin/python3
'''
Conjuntos

Comparando
Tupla, delimitada por virgula e parenteses ()
Dicionário, delimitado por chaves {}, usando chave valor
Conjunto é apenas valores, lembrando uma lista
    porém diferentes em alguns aspectos


Listas:
Estrutura indexada começa com zero para cada elemento tem um índice.
Aceita repetição.
Possível colocar valores iguais
Por padrao segue a ordem de inserção

Conjuntos
Não garante a ordem de inserção.
Não é indexado
    você não consegue acessar um número do conjunto pelo indice
Não aceita repetição
    ou seja os valores que são iguais quando inseridos no conjunto eles
    são ignorados se já tiver um elemento com o mesmo valor e

Casos de uso
É possível emular funcionalidades dos conjuntos usando outros tipos, porém,
    o conjunto ganhará em performance e simplicidade, exemplos de uso:
- Listas que não aceitam repetição de valores
- Diversos métodos nativos para trabalhar com conjuntos
    (diferença, interseção, união, diferença simétrica, etc)

'''

a = {1, 2, 3}  # Criando um conjunto, tipo set
print('\nA é uma variavel do tipo:\n{}'.format(type(a)))  # Mostrando o tipo
# a[0] # Ocorrerá erro, visto que conjunto nao aceita indice
a = set('cod3r')  # criando um conjunto
# Lembrando que nao tem garantia de ordenacao
print('\nImprimindo o conjunto a:\n{}'.format(a))
# Usando expressao para verificar valores
# se 3 esta dentro de a = True
# se 4 nao esta dentro de a = True
print('\nVerificando elementos dentro do conjunto:')
print('3' in a, 4 not in a)
# Comparando 2 conjuntos, sera verdadeiro
# Visto que a ordem nao é importante e elementos repetidos sera ignorados
print('\nComparando conjuntos:')
print({1, 2, 3} == {3, 2, 1, 3})  # sera True

# Operacoes de conjunto
c1 = {1, 2}  # Criando conjunto c1
c2 = {2, 3}  # Criando conjunto c2
c3 = c1.union(c2)  # Unindo conjunto c1 e c3 no conjutno c3
print('\nMembros do conjunto c3:{}'.format(c3))
print('\nValores da interseccao dos conjunto c1 e c2:')
print(c1.intersection(c2))
c1.update(c2)  # atualizando os valores de c1 com valores de c2
print('\nValores do conjunto c1 apos update:\n{}'.format(c1))

# Verificando se c2 é um subconjunto de c1, ou seja
# se c2 esta dentro de c1
# Verificando de c1 é um superconjunto de c2, ou seja
# se c1 possui o conjunto c2
print('\nsubconjuntos e superconjunto comparando:')
print(c2 <= c1)
print(c1 >= c2)

print('\nImprimindo a diferenca de dois conjuntos')
print({1, 2, 3} - {2})
print(c1 - c2)

# Atualizando os valores de um conjunto
c1 -= {2}  # Removendo 2 do conjutno c1
print('\nValores c1 sao:\n{}'.format(c1))

#
# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 53
# https://github.com/cod3rcursos/curso-python/tree/master/fundamentos
