#!/usr/bin/python3
import pyperclip
'''
String puras
Podemos inserir um r antes das pastas de  inicio em uma string para
transofrmá-la em uma string pura (raw string), com isso a string
ignorará todos os caracteres de scape
'''
print('Exemplo de um string pura:')
print(r'\n\t That is Carlos \'s cat.')

'''
Strings em multiplas linhas
'''

print('''\nTeste
de
'String'
de
    Multiplas
linhas
''')


'''
Indexacao e Slices
As String usam indices e slices (Fatias) do mesmo modo que as listas
'''

print('\nTeste de slice string')
spam = 'Hello World!'
print(spam[0])  # Primeiro caractere
print(spam[4])  # Quinta caractere
print(spam[-1])  # Ultimo caractere
print(spam[0:5])  # do 0 ao 5
print(spam[:5])  # do 0 ao 5
print(spam[6:])  # do 6 até o final

'''
Operadores in e not in com strings
Os operadora in e not in podem ser usados com strings
assim como em valores de listas
'''
print('\nTeste de strings:')
print('Hello' in 'Hello World')  # True
print('Hello' in 'Hello')  # True
print('HELLO' in 'Hello World')  # False
print('' in 'spam')  # True
print('cats' not in 'cats and dogs')  # False

'''
upper(), lower(), title()
Retornam um nova string em que todas as letras da string original foram
convertidas para maiusculas ou minusculas.
Os métodos não alteram a string em si, mas retornam novos valores de strings

Os métodos upper() e lower() serão úteis caso seja necessário fazer uma
comparação sen kevar en cibta a diferença de maisculas e minusculas
'''

print('\nTeste dos métodos upper e lower')
spam = 'Hello World'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)
spam = spam.title()  # Primeira letra maisuculas
print(spam)

print('\nComparando strings:')
print('How are you?')
feeling = 'GREATE'
if feeling.lower() == 'greate':
    print('I feel greate too')

# Como os métodos retornam string,
# podemos chamar os métodos de string nesses valores
print('\nTeste de aninhamento de métodos')
print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('Hello'.upper().lower().upper().lower())


'''
isupper(), islower()
Retornarão um valor booleano True se a string tiver pelo menos uma letra
e todas as letras forem maiusculas ou minusculas, respectivalmente.
'''

print('\nTeste dos métodos isupper() e islower()')
spam = 'Hello World'
print(spam.islower())  # False
print(spam.isupper())  # False
print('HELLO'.isupper())  # True
print('abc12345'.islower())  # True
print('12345'.islower())  # False
print('12345'.isupper())  # False

'''
Métodos de string isXa
isalpha() retornará True se a string for constituida somente de letras
    e não estiver vazia
isalnum() retornará True se a string for constituida somente de letas e
    numeros e não estiver vazia
isdeciamal() retornará True se a string for constituida somente de caracteres
    numéricos e não estiver vazia
isspace() retornará True se a string for constituida somente de espaços,
    tabulações e quebras de linhas e não estiver vazia
istitle() retornará True se a string for constituida somente de palavras que
    comecer com uma letras maiuscula seguida de letas minusculas


Esse métodos são úteis para validar dados de entrada de usuúario, exemplo
'''

while True:
    print('\nEnter you age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
print('tks')

'''
startswith() endswith()
Retornarão True se o valor de string com o qual forem chamados comeceçar ou
terminar (respectivamente) com a string passada para o método
'''

print('\nTeste dos metodos startswith e endswith')
print('Hello world!'.endswith('world!'))  # True
print('abc123'.startswith('abcdef'))  # False
print('abc123'.endswith('12'))  # False
print('Hello world!'.startswith('Hello world!'))  # True
print('Hello world!'.endswith('Hello world!'))  # True

'''
join()
O método join() é útil quando temos uma lista de strings que devem ser unidas
em um único valor de string.
Esse método é interessante pois podemos usar uma separador dos itens

'''

listanimals = ['cats', 'dogs', 'bears']
stringanimals = ', '.join(listanimals)
print('\nTeste1 do metodo join:')
print(stringanimals)

stringanimals = ' '.join(listanimals)
print('Teste2 do metodo join, usando um separador')
print(stringanimals)

'''
split()
O método split faz o inverso do join.
É chamado em um valor de string e retorna uma lista de strings.

Um uso comum esta em dividir uma string de multiplas linhas nos caracteres
de quebra de linha
'''

frase = 'My name is Simon'
print('\nTeste1 do método split:')
print(frase.split())
print('\nTeste2 do método split, usando um separador')
print(frase.split('is'))

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely
Bob'''
print('\nTeste2 do método split, usando um separador\n')
print(spam.split('\n'))

'''
Justificando texto rjust(), ljust(), center()
Os métodos de string retornam uma versão preenchida da string em que
são chamadas com espeços inseridos para justificar o texto

1 - Argumemto é um inteiro referente ao tamanho da string justificada
Perceba que se o inteiro for menor que o tamanho da string, nada acontecera!

2 - Argumento opcional, especifica o caractere de preenchimento
'''

print('\nTeste dos métodos rsjust e ljust:')

hello = 'Hello world'
print(hello.rjust(20))
print(hello.ljust(30))
print(hello.rjust(15, '*'))
print(hello.ljust(25, '-'))
print(hello.center(15))
print(hello.center(25, '='))

'''
Esse métodos serão especialmente úteis quando for necessário exibir
dados tabulares que tiverem o espacámento correto, Exemplo:
'''

print('\nExemplo mais complexo do ljust, rjust e center:\n')


def printPicnic(ItemDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in ItemDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)  # Executando uma vez
printPicnic(picnicItems, 20, 7)  # Executando segunda vez

'''
strip(), rstrip(), lstrip() removendo espaços em brancos

strip()
retornará uma nova string sem caracteres de espacos em branco no inicio ou fim
lstrip() rstrip()s
Removerao caracteres de espacoes em branco das extremidades
da esquerda e direita respectivamente

Opcionalmente, um argumento do tipo string especifica quais caracteres
deverao ser removidos, nao importando a ordem
'''

print('\nTestando metodos para remover os espacos:')
spam = '   Hello World    '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpamSpam'
print(spam.strip('ampS'))

'''
Copiando e colando strings com módulo pyperclip

O modulo pyperclip tem as funcoes de copy() e paste() capazes de
enviar e receber textos do clipboard (area de tranferencia) do seu computador
Enviar a saída de seu programa para o clipboard facilitará colá em um email,
um processador de texto uo em outro software

Necessario usar o import pyperclip para funcionar
pip3 install pyperclip
'''

print('\nExemplo de pyperclip:')
pyperclip.copy('The text to be copied to the clipboard.')
print(pyperclip.paste())


# Fontes
# Livro Automatiando tarefas maçantes com python
# Capitulo 6, Manipulação de strings
