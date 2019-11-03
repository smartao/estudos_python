#!/usr/bin/python3
#

'''
três métodos para dicionarios
dicionario.keys() Para retornar apenas as chaves
dicionario.values() Para retornar apenas os valores
dicionario.items() Para retornar chave e valor


Loop usando dicionarios, sintaxe:
for key_variable in dictionary_name:
    # Code Block
    # dictionary_name[key_variable]

Exemplos
for contact in contacts:
    # Code block
for person in peoplo:
    # Code block

Obs: O laço nem sempre percorrerá o dicionário na ordem exata dos elementos

Laço com dois valores
for key_variable, value_variable in dictionary_name.items():
    # Code block
'''

# Laço para um dicionario, verificando a ordem dos elementos
contacts = {
    'Jason': '555-0123',
    'Carl': '555-0987'
}
# Funcionar semelhante ao dicionario de cima
# contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
print('\nUsando for para percorrer um dicionario')
for contact in contacts:
    print('The number for {0} is {1}.'.format(contact, contacts[contact]))

# Exemplo de laço com dois valores, a saida é igual a laço anterior
# Porém a sintaxe fica mais simples de utilizar
print("\nExemplo de laço com dois valores")
for person, phone_number in contacts.items():
    print('The number for {0} is {1}.'.format(person, phone_number))

# Exemplo de dicionario de dados mais complexo junto com o laço
contacts = {
    'Jason': {
        'phone': '555-0123',
        'email': 'jason@example.com'
    },
    'Carl': {
        'phone': '555-0987',
        'email': 'carl@example.com'
    }
}

print("\nExemplo de dicionario mais complexos")
for contact in contacts:
    print("{}'s contact info:".format(contact))
    print(contacts[contact]['phone'])
    print(contacts[contact]['email'])

#
# Fontes:
# Curso Python for Beginners: Learn Python Programming Udemy Aula 54 e 55
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 51 e 52
# https://github.com/cod3rcursos/curso-python/tree/master/fundamentos
