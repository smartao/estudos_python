#!/usr/bin/python3
#

# Numero de index de um objeto
animals = ['man', 'bear', 'pig']
print("\nRetornando o numero do index do objeto bera")
bear_index = animals.index('bear')
print(bear_index)

# Trantando uma execao, nesse caso quando nao existir o objeto gato na lista
animals = ['man', 'bear', 'pig']
try:
    cat_index = animals.index('cat')
except:
    cat_index = 'No cats found.'
print(cat_index)

#
#Fontes: 
#Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 47