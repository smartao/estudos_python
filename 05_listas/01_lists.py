#!/usr/bin/python3
import copy
'''
Sintaxe
list_name = [item_1, item_2, item_N]
list_name = []
list_name[index]
'''

# Exemplo basico de lista
animals = ['man', 'bear', 'pig']
print("Imprimindo cada elemento de uma lista")
print(animals[0])
print(animals[1])
print(animals[2])

# Alterando um dos valores
animals[0] = 'cat'
print("\nAlterando um elemetndo da lista")
print(animals[0])

# Acessando uma lista de forma inverteida
print("\nAcessando uma lista de forma invertida")
print(animals[-1])  # Ultimo elemento da lista
print(animals[-2])  # Penultimo elemento da lista
print(animals[-3])  # Antipenultimo elemento da lista

print("\nadicionando um elemento no final da lista")
animals.append('cow')
print(animals[-1])

# Extendendo uma lista, metodo extend
print("\nExtendendo uma lista com multiplus elementos usando o método exted")
animals.extend(['cow', 'duck'])
print(animals)

more_animals = ["horse", "dog"]
animals.extend(more_animals)
print(animals)

# Limpando a lista
animals = []

# Inserindo na lista, metodo insert
print("\nInserindo um elemento na lista em uma posicao especifica")
animals = ['Man', 'bear', 'pig']
animals.insert(0, 'horse')  # horse na posicao 0
animals.insert(2, 'duck')  # pato na posicao 2
print(animals)

print('\nValidando se um elemento esta na lista')
print('duck' in animals)  # Verdadeiro
print('ducks' in animals)  # Falso
if 'duck' in animals:
    print('Animal encontrado!!')

newanimals = copy.copy(animals)
newanimals[1] = 'dog'
print(animals)
print(newanimals)

'''
Oara copiar um lista que contenha outras listas utiliza o método copy.deepcopy
'''
#
# Fontes:
# Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 45
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 41 a 44
# https://github.com/cod3rcursos/curso-python/tree/master/fundamentos
