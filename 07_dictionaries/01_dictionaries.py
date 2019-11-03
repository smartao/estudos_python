#!/usr/bin/python3
#
"""
Dicionário é um dipo de dados que contem pares de valores-chaves
que sao chamados itens, ou também hashes arrays ou  tambem hash tables

dictionary_name = {key_1: value1, key_N: valueN}
dictionary_name = {}
dictionary_name[key]
"""

# Criando dicionario, atualizando valor e imprimidno
pessoa = {'nome': 'Prof. Albert', 'idade': 43, 'curso': ['React', 'Python']}
pessoa['idade'] = 44  # Atualizando valor idade
pessoa['curso'].append('Angular')
print('\nImprimindo dicionario pessoa:\n{}'.format(pessoa))

# Lendo o atributo idade e removendo do dicionario, metodo pop
print('\nImprimindo a idade e removendo:\n{}'.format(pessoa.pop('idade')))
pessoa.update({'idade': 40, 'Sexo': 'M'})  # Atualizando valores do dicionario
print('\nImprimindo dicionario pessoa atualizado:\n{}'.format(pessoa))

# Deletando e limpando um dicionario
del pessoa['curso']  # Deletando a chave curso
print('\nImprimindo dicionario pessoa sem curso:\n{}'.format(pessoa))
pessoa.clear()  # Limpando o dicionario

# ### Atribuindo valores a varaiveis por um dicionario
# Criando dicionarios com dois valores
contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
jasons_phone = contacts['Jason']
carls_phone = contacts['Carl']
print("\nExemplo de dicionário")
print('Dial {} to call Jason.'.format(jasons_phone))
print('Dial {} to call Carl.'.format(contacts['Carl']))

# Atualizando valores de um dicionarios
contacts = {'Jason': '555-0123', 'Carl': '555-0987'}  # Criando um dicionario
contacts['Jason'] = '555-0000'  # Atualizando valor da chave Jason
jasons_phone = contacts['Jason']  # Armazenando valor da chave em uma variavel
print('\nAtualizando valores de um dicionario')
print('Dial {} to call Jason.'.format(jasons_phone))  # Imprimindo variavel

# Adicionando itens a um dicionariso
contacts = {'Jason': '555-0123', 'Carl': '555-0987'}  # Criando um dicionarios
contacts['Tony'] = '555-0570'  # Adicionando novo item
print('\nAdicionando itens a um dicionario')
print(contacts)  # Imprimindo o dicionario
print(len(contacts))  # Imprimindo quantidade de itens do dicionarios

# Removendo um item do dicionario
contacts = {'Jason': '555-0123', 'Carl': '555-0987'}  # Criando o dicionario
del contacts['Jason']  # Deletando o item Jason
print('\nDeletando um item do dicionario')
print(contacts)  # Imprimindo o dicionario

# Criando dicionario com valores diferentes, usando string e lista
contacts = {
    'Jason': ['555-0123', '555-0000'],
    'Carl': '555-0987'
}
print('\nCriando dicionario com diferente tipos de valores')
print('Jason: {}'.format(contacts['Jason']))
print('Carl:{}'.format(contacts['Carl']))

# Crinado um dicionario e imprimindo a lista dentro dele
contacts = {
    'Jason': ['555-0123', '555-0000', '111-2222'],
    'Carl': '555-0987'
}
print('\nImprimindo todos os telefones de Jason')
for number in contacts['Jason']:
    print('Phone: {}'.format(number))

# Verificando se um valor existe dentro do dicionario usando if
contacts = {
    'Jason': ['555-0123', '555-0000'],
    'Carl': '555-0987'
}
if 'Jason' in contacts.keys():  # Se a chave Jason existir
    print("\nJason's phone number is:")
    print(contacts['Jason'][0])  # Imprimindo o primeiro telefone de Jason

if 'Tony' in contacts.keys():  # Se a chave Tony existir
    print("Tony's phone number is:")
    print(contacts['Tony'][0])

# Verificando um se um chave existe a partir de um determinado valor
contacts = {
    'Jason': ['555-0123', '555-0000'],
    'Carl': '555-0987'
}
print('\nVerificando se o numero existe dentro do dicionario')
print('555-0987' in contacts.values())  # Se existe o retorno é True

#
# Fontes:
# Curso Python for Beginners: Learn Python Programming Udemy Aula 54 e 55
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 51 e 52
# https://github.com/cod3rcursos/curso-python/tree/master/fundamentos
