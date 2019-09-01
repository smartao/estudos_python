#!/usr/bin/python3
#
# Funcao com parametro opcional
def say_hi1(name = 'there'):
    print('Hi {}!'.format(name))

say_hi1() # Sem parametro
say_hi1('Jason') # com parametro

# Funcao com multiplus parametros
def say_hi2(first, last):
    print('Hi {} {}!'.format(first, last))

say_hi2('Jane', 'Doe')

# Definindo a ordem dos parametros manualmente
def say_hi3(first, last):
    print('Hi {} {}!'.format(first, last))

say_hi3(first = 'Jane', last = 'Doe')
say_hi3(last = 'Doe', first = 'John')

# Funcao com parametros opcionais e obrigatorios
def say_hi4(first, last='Doe'): # last sem opcianal
    print('Hi {} {}!'.format(first, last))

say_hi4('Jane')
say_hi4('John', 'Coltrane')

# Usando 3 aspas nas primeiras linhas para criar um minidocumentacao da funcao
# quando clicar na funcao sera mostrando a documentacao pelo IDE
def say_hi5(first, last='Doe'):
    """Funcao say hello
    Exemplo de documentacao
    """
    print('Hi {} {}!'.format(first, last))

help(say_hi5)

# Funcao impar ou par usando o retorno
def odd_or_even(number):
    """Determine if a number is odd or even."""
    if number % 2 == 0: # se o resto da divicao for zero
        return 'Even' # Par
    else:
        return 'Odd' # Impar

odd_or_even_string = odd_or_even(7) # Passando o n 7 como parametro da funcao
print(odd_or_even_string) # Imprimindo o resultado

# Similar a funcao anterior, porém verificar se o numero é impar ou nao
def is_odd(number):
    """Determine if a number is odd."""
    if number % 2 == 0:
        return False
    else:
        return True

print("Number is odd = "+ str(is_odd(7))) # imprimindo diretamente a saida

# Usando funcao que chamam outras funcoes
def get_name(): 
    """Funcao get and return a name"""
    name = input('What is your name? ')
    return name

def say_name(name):
    """Funcao Say a name"""
    print('Your name is {}.'.format(name))

def get_and_say_name(): # Funcao principal
    """Get and display name"""
    name = get_name()
    say_name(name)

get_and_say_name()

#######################
#
# Exemplo mais complexo usando várias funcoes 

def get_word(word_type):
    """Get a word from a user and return that word."""

    # The lower() function converts the string to lowercase before testing it
    if word_type.lower() == 'adjective':
        # Use 'an' in front of 'adjective'
        a_or_an = 'an'
    else:
        # Otherwise, use 'a' in front of 'noun' or 'verb'
        a_or_an = 'a'
    return input('Enter a word that is {0} {1}: '.format(a_or_an, word_type))


def fill_in_the_blanks(noun, verb, adjective):
    """Fills in the blanks and returns a completed story."""

    # The \ lets the string continue on the next line to make the code easier to read
    story = "In this course you will learn how to {1}.  " \
            "It's so easy even a {0} can do it.  " \
            "Trust me, it will be very {2}.".format(noun, verb, adjective)
    return story


def display_story(story):
    """Displays a story."""
    print()
    print('Here is the story you created.  Enjoy!')
    print()
    print(story)


def create_story():
    """Creates a story by capturing the input and displaying a finished story."""
    noun = get_word('noun')
    verb = get_word('verb')
    adjective = get_word('adjective')

    the_story = fill_in_the_blanks(noun, verb, adjective)
    display_story(the_story)

create_story() # Funcao principal
#
#Fontes: 
#Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 38 a 42