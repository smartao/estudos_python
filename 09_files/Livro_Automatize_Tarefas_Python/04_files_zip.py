#!/usr/bin/python3

import zipfile

'''
Lendo arquivos ZIP
Observer que zipfile é o nome do módulo Python e ZipFile() é o nome da funcao
'''

print('Compactando arquivos:')
exampleZip = zipfile.ZipFile('bacon.zip')
print(exampleZip.namelist())  # Imprimindo conteudo do arquivo

spamInfo = exampleZip.getinfo('hello.txt')  # Recebendo informacoes do arquivo
print(spamInfo.file_size)  # Imprimindo tamanho do arquivo
print(spamInfo.compress_size)  # Imprimindo tamanho do arquivo comprimido
print('Compressed file is %sx smaller' %
      (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()

'''
Extraindo itens de arquivos ZIP
A string passada para extract() deve coincidir com uma das string da lista
retornada por namelist()
'''

print('\nExtraindo arquivos:')
# os.chdir('/usr/local') Mudando a pasta de trabalho atual
exampleZip = zipfile.ZipFile('bacon.zip')
exampleZip.extractall()
exampleZip.close()

exampleZip = zipfile.ZipFile('bacon.zip')
exampleZip.extractall('/tmp')  # Extraindo tudo na pasta /tmp
exampleZip.extract('hello.txt')  # Extraindo apenas o arq hello
exampleZip.extract('hello.txt', '/tmp')  # Extrando para um dir
exampleZip.close()

'''
Criando arquivos ZIP e adicionando itens
'''

print('\nCriando arquivos zip:')
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('hello.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

print('\nAdicionando arquivo a um zip já existente:')
newZip = zipfile.ZipFile('new.zip', 'a')
newZip.write('frases.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 9 pos 6000
