#!/usr/bin/python3
#
####### Formatando Strings ########
#
### Impressao basica ###
hello="ola mundo"
print(hello)
#
# Mostrando quantos caracteres tem a string fruit
fruit="Fruta de teste" 
print(len(fruit))
#
### Utilizando aspas ###
double = "She said, \"That's a great tasting apple!\""
single = 'She said, "That\'s a great tasting apple!"'
#
print(double) # She said, "That's a great tasting apple!"
print(single) # She said, "That's a great tasting apple!"
#
### Concatenacao ###
#
# Exemplo1 Variavies
first = 'I'
second = 'love'
third = 'Python'
sentence = first + ' ' + second + " " + third
print(sentence)
#
# Exemplo 2 string + number
# Necessario a conversao antes da impressao
version = 3
print('I love Python ' + str(version) + '.')
#
### Formatação string ###
#
# Basico
print('I {} Pyhton.'.format('love')) # I love Pyhton.
print('{} {} {}'.format("I","love","Python.")) # I love Pyhton.
print('I {0} {1}. {1} {0}s me.'.format("love","Python")) # I love Python. Python loves me.
#
# Com variaveis
first = "I"
second = "loves"
third = "Python"
print ('{} {} {}.'.format(first,second,third)) # I love Pyhton.
#
# Com variaveis numericas
version = 3
print('I love python {}.'.format(version)) # I love Pyhton 3.
#
# Criando tabelas
print('{0:8} | {1:8}'.format("Fruit","Quatity"))
print('{0:8} | {1:8}'.format("Apple","3"))
print('{0:8} | {1:8}'.format("Orange","10"))
"""
Saida
Fruit    | Quatity 
Apple    | 3       
Orange   | 10   

Alinhamentos disponíveis
< Left # Alinhamento padrao
^ Center
> Right
"""
# Alinhamento para esquerda
print('{0:8} | {1:>8}'.format("Fruit","Quatity"))
print('{0:8} | {1:>8}'.format("Apple","3"))
print('{0:8} | {1:>8}'.format("Orange","10"))
#
# Mostrando números compostos 
# Adicionar .2f, casas decimais e o floot
print('{0:8} | {1:>8}'.format("Fruit","Quatity"))
print('{0:8} | {1:>8.2f}'.format("Apple",2.3333))
print('{0:8} | {1:>8.2f}'.format("Orange",10))
#
# Recebendo entrada do usuario
fruit = input ('Enter a name of a fruit: ')
print("{} is a lovely fruit.".format(fruit))
'''
Saída
Enter a name of a fruit: apple
INPUT_USER is a lovely fruit.
'''
# Transformando as letras da frase de entrada titulo
# Primeia em maisculo restante em minusculos
titulo = input('Entre com o titulo do video: ')
print(titulo.title())
#
#Fontes: 
#Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 10 a 14