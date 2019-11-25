#!/usr/bin/python3

import shutil
import os
import send2trash

'''
O modulo shutil (shell utilities), contem funcoes que permite copiar, mover
renomear e apagar arquivos. Para utiliza-lo basta usar import shutil

Copiando arquivo shutil.copy()
shutil.copy(origem, destino) copiará o arquivo no path origem para a
pasta de destino (ambos são strings)
'''

dir = '/tmp'
dirOri = '/tmp/files/'
arqOri = dirOri + 'xpto.txt'

# Alterar o diretorio de trabalho para /tmp
os.chdir(dir)
# Verificando se o arquivo existe
if os.path.exists(arqOri):
    # Se existir fazer uma copia
    shutil.copy(arqOri, dirOri + 'xptonew.txt')
# Se nao existir
else:
    # Verificar se o diretiro existe
    if not os.path.exists(dirOri):
        # Se nao existir cria o diretorio
        os.mkdir(dirOri)
    # depois cria o arquivo
    os.mknod(arqOri)

'''
Copiando diretorios shutil.copytree()
Copiara uma pasta completa
'''

# Verificando se a pasta nao existir, faz uma copia
if not os.path.exists('/tmp/filesnew'):
    shutil.copytree(dirOri, '/tmp/filesnew')

'''
Movendo e renomear arquivos e pastas
shtuil.move(origem, destino) moverá o arquivo ou a pasta da origem para o
destino e retornará uma string com o path absoluto da nova localidade
Caso o arquivo nao existe o mesmo sera sobreescrito

obs: Se copiar um arquivo para uma pasta que o arquivo já exista com o mesmo
nome ocorrerá um erro
'''

shutil.move(arqOri, '/tmp/filesnew/xptonew.txt')

'''
Apagando arquivos e pastas permanentemente
Podemos apagar um único arquivo ou único pasta vazia com funçoes do módulo os,
para pagar uma pasta e todo o conteudo, devemos usar o módulo shutil.

os.unlink(path) apagará o arquivo em path
os.rmdir(path) apagara a pasta em path deste que esteja vazia
shtuil.rmtree(path) removerá a pasta e todo o conteudo.
'''

for filename in os.listdir(dirOri):
    if filename.endswith('.txt'):
        os.unlink(dirOri + filename)  # Apagando o arquivo
        print(dirOri + filename)  # Imprimindo antes de deletar

'''
Apagando arquivos com segurança usando o módulo send2trash
Com esse modulo os arquivos e pastas serao enviados para a lixeira
para instalar execute o comando
pip3 install send2trash
'''
dir = '/home/sergei/Midias/Dev/Python/estudos_python/09_files/Livro_Automatize_Tarefas_Python'
baconFile = open(dir + 'bacon.txt', 'a')  # Criar o arquivo
baconFile.write('Bacon is not a vegetable\n')
baconFile.close()
send2trash.send2trash(dir + 'bacon.txt')
# obs: Esta ocorrendo erro quando executado fora do direto do projeto

'''
Percorendo uma árvore de diretorios os.walk()
a Função os.walk() recebe um único valor de string: o path de uma pasta.
Que pode ser usada em uma instrução de loop for para percorerer uma árvore de
diretorio, de modo muito semelhante á forma como a funcão range.
A função os.walk() retornrá três valores a cada iteração pelo loop:
1 - Uma string com o nome da pasta atual.
2 - Uma lista de string com as pasta da pasta atual
3 - Uma lista de string com os arquivos da pasta atual
'''

dir = '/home/sergei/Midias/Videos/Outros/Ero-Sub'
for folderName, subfolders, filenames in os.walk(dir):
    print('O diretorio atual é: ' + folderName)
    for subfolder in subfolders:
        print('  A subpasta de ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('    O arquivo dentro ' + folderName + ': ' + filename)


# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 9
