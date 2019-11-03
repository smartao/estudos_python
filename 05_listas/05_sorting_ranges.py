#!/usr/bin/python3
#

# Ordenando uma lista
animals = ['man', 'bear', 'pig']  # Criando uma lista com nomes de animais
# Ordenando a lista e armazenando na variavel sorted_animals
sorted_animals = sorted(animals)
print('\nAnimals list:              {}'.format(
    animals))  # Imprimindo a lista de nomes

# Imprimindo a variavel com a lista ordenada
print('Sorted animals list:       {}'.format(sorted_animals))
animals.sort()  # Usanod o método de ordenandar do objeto animals
print('Animals after sort method: {}'.format(
    animals))  # Imprimindo a lista ordenada


# Adicionando valores a uma lista
animals = ['man', 'bear', 'pig']  # Criando uma lista
more_animals = ['cow', 'duck', 'horse']  # Criando a segunda lista
# Armazenando os valores das duas lista em uma variavel
all_animals = animals + more_animals
print("\nImprimindo as duas listas armazenada na variavel all_animals")
print(all_animals)  # Imprimindo variavel com valores das duas listas


# Determinando o tamanho da lista
animals = ['man', 'bear', 'pig']  # Criando lista com 3 objetos
# Imprimindo tamanho da lista
print("\ntamanho da lista: {}".format(len(animals)))
animals.append('cow')  # Adicionando mais um objeto
# Imprimindo tamanho da lista
print("tamanho da lista: {}".format(len(animals)))


print("\nExemplo da funcao range")
for number in range(3):  # laço que conta de 0 a 2, utilizando a funcao range
    print(number)  # Imprimindo os valores gerado pelo range

print("\nFuncao range com difinicao de inicio e fim")
for number in range(1, 3):
    print(number)  # Sera impresso os numeros 1 e 2

print("\nFuncao range com incremento de 2 em 2")
for number in range(1, 10, 2):
    print(number)

print("\nFuncao range com listas, imprimindo de 2 em 2 itens")
animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse', 'dog']
# range, começa no 0, vai até o final da lista len(animals), incremento de 2
for number in range(0, len(animals), 2):
    print(animals[number])

'''
3 aspectors sobre o método sort
1 O método ordena a lista in place, ou seja alterando o valor da lista
2 Não podemos ordenar uma lista que contenha valores numeros e strings
3 Utiliza a ordem ASCII, em ver de ordem alfabética
Isso quer dizer que as letras maisculas vem antes das letas minusculas
'''

print('\nOrdenando uma lista, não retorna valor')
animals.sort()  # Ordenando
print(animals)

print('\nOrdenando de forma inversa')
animals.sort(reverse=True)  # Ordenando
print(animals)

print('\nOrdenando a lista e ignorado maisculas e minusculas')
animals.sort(key=str.lower)  # Ordenando
print(animals)
print('Criando uma duplicada de uma lista ou dicionadio')

#
# Fontes:
# Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 49
