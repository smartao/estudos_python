#!/usr/bin/python3
#
# Slices sao parte de uma lista
#
animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']

some_animals = animals[1:4]  # Lembrando que irá ate o valor 3
print('Imprimindo do valor 0 ao 3 da lista')
print('Some animals:      {}'.format(some_animals))

first_two = animals[0:2]
print('\nImprimindo os dois primeiros valores da lista')
print('First two animals: {}'.format(first_two))

first_two_again = animals[:2]
print('\nImprimindo os dois primeiros valores da lista outra forma')
print('First two animals: {}'.format(first_two_again))

last_two = animals[4:6]
print('\nImprimindo os dois ultimos valores da lista')
print('Last two animals:  {}'.format(last_two))

last_two_again = animals[-2:]
print('\nImprimindo os dois ultimos valores da lista outra forma')
print('Last two animals:  {}'.format(last_two_again))


part_of_a_horse = 'horse'[1:3]
print("\ncortando parte de um elemento, saida segunda e terceira letra")
print(part_of_a_horse)

#
# Fontes:
# Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 46
