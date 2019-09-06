#!/usr/bin/python3
#
'''Conversao de bloco de código
4 espacoes para o bloco de codigo
no entanto o python pode aceitar qualquer outro número

Exemplo
Block One
    Block Two
    Block Two
        Bloco Three
    Block Two
Block One
Block One

'''
# Exemplo de if com elif e else
age = 99
if age >= 35:
    print('You are old enough to be a Representative, Senator, or the President.')
elif age >= 30:
    print('You are old enough to be a Senator.')
elif age >= 25:
    print('You are old enough to be a Representative.')
else:
    print('You are not old enough to be a Representative, Senator, or the President.')
print('Have a nice day!')

# Programa sugere o meio de transporte baseado na distancia informada
# Ask for the distance.
distance = input('How far would you like to travel in miles? ')
# Convert the distance to an integer.
distance = int(distance)
# Determine what mode of transport to use.
if distance < 3:
    mode_of_transport = 'walking'
elif distance < 300:
    mode_of_transport = 'driving'
else:
    mode_of_transport = 'flying'
# Display the result.
print('I suggest {} to your destination.'.format(mode_of_transport))

#
# Fontes:
# Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 32 a 36
