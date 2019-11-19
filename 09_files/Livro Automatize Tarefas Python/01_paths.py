#!/usr/bin/python3

'''
Barra invertida no windows e barra para frnete no OSX e Linux

No Windows os paths são escritos com barra investidas (\)
No Mac e Linux utiliza barra para frente (/)

Para que um script funcione em ambos os OS, basta usar a funcao
os.path.join().
Obs: No Windows as barras serao duplicadas, pois cada barra investida,
deve ser escapada por outra caractere de barra invertida.
Ex:
'''

import os  # Todos os exemplos dependem desse modulo!

print(os.path.join('usr', 'bin', 'spam'))

'''
A Funcao os.path.join() sera útill se houve necessidade de criar strings para
os nomes de arquivos. Ex:
'''

print('\nTeste os.path com o for:')
myFiles = ['accoutns.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/usr/local/bin', filename))

'''
Diretorio de trabalho atual
Supõe-se que qualquer nome de arquivo ou path que não comece com a pasta-raiz
esteja no diretório de trabalho atual
Obetendo o diretorio atual com os.getcwd()
Alterar o diretorio atual com os.chdir()
'''

print('\nImprimindo e alterando o diretorio atual')
print(os.getcwd())
os.chdir('/usr/local/bin')
print(os.getcwd())

'''
Criando novas pastas com os.makedirs()
Pode criar pastas e subpastas, ex
'''

print('\nValidando se um diretorio existe')
if os.path.exists('/tmp/python/automatize/tarefas'):
    print('diretorio existe')
else:
    os.makedirs('/tmp/python/automatize/tarefas')
    print('diretorio criado')

'''
Lidando com paths absolutos e relativos

os.path.abspath(path)
Retornará uma strings como o path absolutos referente ao argumento.
Maneira fácil de converter um path relativo em um path absoluto
os.path.isabs(path)
Retornará True se o argumento for um path absoluto, caso contrário false
os.path.relpath(path, inicio)
Retornará uma string contendo um path relativo ao path inicio para path
Exemplo
'''

# Lembre-se que o diretorio de trabalho foi alterado anteriormente
print('\nLidando com paths absolutos e relativos')
print(os.path.abspath('.'))
print(os.path.abspath('./teste'))
print(os.path.isabs('.'))  # False
print(os.path.isabs(os.path.abspath('.')))  # True

print('\nCaminhos relativos')
print(os.path.relpath('/etc', '/'))
print(os.path.relpath('/etc', '/usr/local'))  # Caminho relativo
print(os.getcwd())

'''
Diretorio e nome de arquivo
os.path.dirname(path)
Retornará uma string contendo tudo que estiver antes da última barra.
os.path.basename(path)
Retornará uma string contendo tudo que estiver após a última barra.
os.path.split(path)
Retornará uma tupla contendo o caminho completo + o nome do arquivo
os.path.sep
Retorna o tipo de separador que o OS tuiliza
'''

print('\nDiretorio e nome de arquivo')
path = '/usr/local/bin/lazyvert.py'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(path.split(os.path.sep))  # No linux o primeiro valor sempre sera vazio

'''
Obtendo so tamanhos dos arquivos e o conteúdo das pastas
os.path.getsize(path)
Retornará o tamanho em bytes do arquivo do argumento path
os.listdir(path)
Retornará uma lista de strings com nomes de arquivo para cada arquivo
no argumento path.
'''

print('\nTamanho e lista de arquivos')
print(str(os.path.getsize('/usr/local/bin/apt')) + ' bytes')
print(os.listdir('/usr/local/bin'))

# Descobrindo o tamanho total de todos os arquivos no diretorio
caminho = '/usr/local/bin'
totalSize = 0
for filename in os.listdir(caminho):
    totalSize += os.path.getsize(os.path.join(caminho, filename))
print('\nTamanho total do diretorio: ' + str(totalSize))

'''
Verificando a validade de um path
os.path.exists(path)
Retornará True se o arquivo ou a pasta existir
os.path.isfile(path)
Retornará True se o arquivo existir
os.path.isdir(path)
Retornará True se a pasta existir
'''

print('\nVlidando se um path ou arquivo existi:')
print(os.path.exists('/usr/local/bin'))  # True
print(os.path.exists('/usr/local/bin/apt'))  # True
print(os.path.isdir('/usr/local/bin'))  # True
print(os.path.isdir('/usr/local/bin/apt'))  # False
print(os.path.isfile('/usr/local/bin'))  # False
print(os.path.isfile('/usr/local/bin/apt'))  # True


# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 8
