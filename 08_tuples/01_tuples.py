#!/usr/bin/python3
#

"""
A tuple is an immutable list
Tuple are ordered
Values accessed by index
Iteration, looping, concatenation
Use when data should not change!

Sintaxe:
tuple_name = (item_1, item_2, item_N)
tuple_name = (item_1,) # Exemplo de um tuple com um unico valor

Comparacao com uma lista
list_name = [item_1, item_2, item_N]

Observação
Um tupla pode ser definida sem os parenteses (), usando apenas virgula
tuple_name = 1, 2, 3
"""

# Exemplo tuples funcionan como lista
# Na linha de baixo exemplo da touple sem os paretentes
# days_of_the_week = 'Monday', 'Tuesday', 'Wednesday',
#   'Thursday', 'Friday', 'Saturday', 'Sunday'
# tupla normal
days_of_the_week = ('Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday')
monday = days_of_the_week[0]
print("\nImprimindo os dias da semana")
print(monday)
print()

'''
Usando laço em um tuple, é semelhando a lista, sintae
for item_variable in tuple_name:
     # Code block
'''
for day in days_of_the_week:
    print(day)

# Não é possível modificar um tuple isso causara uma execao
# days_of_the_week[0] = 'New Monday'

# Deletando um tuple
del days_of_the_week

'''
Alterando entre Tuples and Lists
list() - Built-in function returns a list.
tuple() - Built-in function returns a tuple.
type() - Built-in function returns an object's type.
'''

# Convertendo tuple em list e vise versar
print("\nTestando funcoes de conversao de tuple para list e verificando tipo")
days_of_the_week_tuple = ('Monday', 'Tuesday', 'Wednesday',
                          'Thursday', 'Friday', 'Saturday', 'Sunday')
# convertendo um tuple para uma lista
days_of_the_week_list = list(days_of_the_week_tuple)
print('days_of_the_week_tuple is {}.'.format(type(days_of_the_week_tuple)))
print('days_of_the_week_list is {}.'.format(type(days_of_the_week_list)))

print("\nTestando funcoes de conversao de tuple para list e verificando tipo")
animals_list = ['man', 'bear', 'pig']
animals_tuple = tuple(animals_list)  # convertendo uma lista para um tuple
print('animals_list is {}.'.format(type(animals_list)))
print('animals_tuple is {}.'.format(type(animals_tuple)))

# Utilizando o tuple para atruibuir valores a varias variaveis de uma vez
# Sintaxe:
# (var_1, var_N) = (value_1, value_N)
print("\nAtruibuindo valores a varia variaveis")
days_of_the_week = ('Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday')
(mon, tue, wed, thr, fri, sat, sun) = days_of_the_week
print(mon)
print(fri)

# Utilizar o tuple para receber valores de uma lista
print("\nTuple recebendo valores de uma lista")
contact_info = ['555-0123', 'jason@example.com']
(phone, email) = contact_info
print(phone)
print(email)

# Utilizando o tuple junto com funcoes


def high_and_low(numbers):
    """Determine the highest and lowest number"""
    highest = max(numbers)
    lowest = min(numbers)
    return (highest, lowest)


lottery_numbers = [16, 4, 42, 15, 23, 8]  # Crinado uma lista de numeros
# variaveis recebendo os valores que a funcao retornou em formato de tuple
(highest, lowest) = high_and_low(lottery_numbers)
print('Utilizando tuple junto com funcoes')
print('The highest number is: {}'.format(highest))  # Imprimindo o maior numero
print('The lowest number is: {}'.format(lowest))  # Imprimindo o menor numero

# Utilizando touple junto com um for
print('')
contacts = [('Jason', '555-0123'), ('Carl', '555-0987')]
for (name, phone) in contacts:
    print("{}'s phone number is {}.".format(name, phone))


# Fontes:
# Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 60
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 50
# https://github.com/cod3rcursos/curso-python/tree/master/fundamentos
