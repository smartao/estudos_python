#!/usr/bin/python3
# backupToZip.py - copia uma pasta toda e seu conteúdo para um arquivo
# ZIP cujoo o nome seja incrementado.

'''
Caso de uso
Voce esta preocupado em perder seu trabalho, portando gostaria de criar
arquivos ZIP que sejam "snapshots" de todas a pasta. Voce gostaria de
manter diferentes versoes, portanto quer que o nome dos arquivos ZIP seja
incrementado a cada vez que for criada, por exemplo, arquivoxpto_1.zip,
arquivoxpto_2.zip e assim por diante.
'''

import zipfile
import os


def backupToZip(folder):
    # Faz backup de todo o conteudo de "folder" em um arquivo ZIP
    # Garante que o folder e um path absoluto
    folder = os.path.abspath(folder)

    # Determinar o nome do arquivo que esse codigo devera usar de
    # acordo com os arquivos ja existentes.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Criando o arquivo ZIP
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Percorre toda a arvore de diretorio e compacta os arquivos em cada pasta
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding file in %s...' % (foldername))
        # Acrescenta a pasta atual ao arquivo ZIP.
        backupZip.write(foldername)

        # Acrescenta todo os arquivos dessa pasta ao arquivo ZIP
        for filename in filenames:
            # Verificando se existe arquivos de backup .zip
            # Para assim nao fazer backup do backup!
            if filename.startswith(os.path.basename(folder) + '_') and \
                    filename.endswith('.zip'):
                continue  # Pulando o laco
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


# Fazendo o backup
backupToZip('backupfolder.tmp')


# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 9
