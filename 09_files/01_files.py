#!/usr/bin/python3
#
### Lendo arquivos ###
'''
open() Built-in Function that opens a file and returns a file object

open(path_to_file)
path_to_file - Can be absolute or relative.

open('/var/log/messages')
open('log/messages')
'''

# Exemplo de leitura
hosts = open('/etc/hostname')
hosts_file_contents = hosts.read()
print('\nimprimindo o conteudo do arquivo hosts')
print(hosts_file_contents)

'''
File Position Métodos disponíveis
read() - Returns the entire file.
seek(offset) - Change the current position to offset.
seek(0) - Go to the beginning of the file.
seek(5) - Go to the 5th byte of the file.
tell() - Determine the current position in the file.

Observacao
Importante notar que mandar ler um arquivos duas vezes na segunda sera,
retornando uma string vazia, pois não há mais dados para retornar à sua posição 
atual do arquivo

'''

# Exemplo para mostrar a posicao atual e altera-la
hosts = open('/etc/hostname')
print('\nLendo e relendo um arquivo voltando a posicao inicial')
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())

print('Current position: {}'.format(hosts.tell()))
print(hosts.read())

hosts.seek(0)  # Alterando a posicao atual para o inicio do arquivo
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())

# Lendo apenas os 3 primeiros bytes do arquivo
hosts = open('/etc/hostname')
print('\nLendo os 3 primeiros bytes do arquivo e mostrando a posicao')
print(hosts.read(3))
print(hosts.tell())

# Fechando arquivos após leitura
'''
Boa pratica, visto que um programa pode precisar ler muitos arquivos
Ao longo da execucao e caso não feche pode ocorrer erros de leitura

Após finalizar leitura utilize
hosts.close() 
'''

# Verificando se o arquivo foi fechado
'''
Utilizando o método objeto.closed verificar se o objeto esta fechado
'''
print('\nVerificar se o arquivo esta aberto o fechado')
hosts = open('/etc/hostname')
hosts_file_contents = hosts.read()
print('File closed? {}'.format(hosts.closed))
if not hosts.closed:  # Caso esteja aberto, feche o arquivo
    hosts.close()  # Fechando o arquivo
print('File closed? {}'.format(hosts.closed))

# Fechando automáticamente arquivos
'''
with open(file_path) as file_object_variable_name:
    # Code block
Obs: Mesmo se ocorrer uma excecao o arquivo sera fechado
'''
print('\nExemplo para fechar automáticamente arquivos')
print('Started reading the file.')
with open('/etc/hostname') as hosts:
    print('File closed? {}'.format(hosts.closed))
    print(hosts.read())
print('Finished reading the file.')
print('File closed? {}'.format(hosts.closed))

# Lendo linha por linha de um arquivo
# O resultando padrao é uma linha branca entre cada linha do arquivo
# Isso porque a linha completa contem o caractere de quebra de linha
print('\nImprimindo um arquio linha por linha')
with open('08_files/file.txt') as the_file:
    for line in the_file:
        print(line)

print('\nImprimindo um arquio linha por linha sem linhas em branco!')
with open('08_files/file.txt') as the_file:
    for line in the_file:
        print(line.rstrip())

'''
Quando abrir podemos especifiar o modo

open(path_to_file, mode)
mode - Description
r = Open for read (default)
w = Open writing, truncating first
x = Create a new file and open it for writing < Utiliza para nao correr o risco de sobreescrever arquivos
a = Open writing, appending to file
+ = Open a file for updating (read/write)
b = Binary mode # Contem serie de binarios, ex, imagens, videos, arquivos comprimidos e etc
t = Text mode (default) # Contem serie de strings

'''
print('\nVerificando o modo do arquivo')
with open('08_files/file.txt') as the_file:
    print(the_file.mode)

# Escrevendo dentro de um arquivo, usando o método write
print('\nEscrevendo dentro de arquivos e imprimindo o que foi escrito')
with open('08_files/file2.txt', 'w') as the_file:
    the_file.write('This text will be written to the file.\n')
    the_file.write('Here is more text.\n')

with open('08_files/file2.txt') as the_file:
    print(the_file.read())

'''
Iniciando uma nova linha, termo em inglê
Carriage Returns and Line Feeds

\r   Carriage Return
\n   New Line

\n   Unix/Linux/Mac Line endings
\r\n Windows style line endings
'''

# Trabalhando com arquivos binarios
print('\nLendo caracteres de arquivos binarios como imagens')
with open('08_files/cat.jpg', 'rb') as cat_picture:  # Abrindo o arquivos
    cat_picture.seek(2)  # Indo para o 2 byte do arquivo
    cat_picture.read(4)  # Lendo 4 byte do arquivo
    print(cat_picture.tell())  # Imprimindo a posicao corrent do arquivos
    print(cat_picture.mode)  # Modo que o arquivos esta, rb

# Criando uma excecao caso o arquivo nao exista
print('\nTrabalhando com excecao em arquivos')
# Open a file and assign its contents to a variable.
# If the file is unavailable, create an empty variable.
try:
    contacts = open('contacts.txt').read()
except:
    contacts = []  # Caso nao exista sera criando a variavel
print(len(contacts))

#
# Fontes:
# Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 65 e 66
