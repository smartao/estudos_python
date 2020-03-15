#!/usr/bin/python3
# renameDates.py - Renomeia os nomes de arquvivos com formatado de
# data MM-DD-AAAA em estilo americano para o formatado DD-MM-AAAA em
# estilo europeu

'''
Suponha que seu chefe envie milhares de arquivos a voce por email com datas
em estilo americano (MM-DD-AAAA) nos nomes dos arquivos e precise que eles
sejam renomeados com datas em estilo europeu (DD-MM-AAAA). Essa tarefa macante
poderia exigir um dia inteiro para ser feito manualmente!

Eis o que o programa deve fazer:
Procurar todos os nomes de arquivos do diretorio de trabalho atual em busca de
    datas em estilo americanos.
Quando um arquivo for encontrado, ele devera ser renomeado com o mes e o dia
    trocado par adeixa a data em estilo europeu
Criar uma regex que possa identificar o padrao de texto para data em estilo
    americano
Chamar os.listdir() para encontrar todos os arquivos no diretorio de trabalho
Percorre todos os nomes de arquivos em um loop usando a regex para verificar
    se lee contem uma data
Se houve uma data o arquivo devera ser renomeado com shutil.move()
'''

import shutil
import os
import re

# Cria uma regex que corresponde aos arquivos com formato de data em estilo
# Americano

'''
Contando os grupos da regex:
Procure ler a regex do inicio e contabilize cada vez que encontrar um parêntese
de abertura. Sem pensar no código, simplesmente crie um esquema para a
exmpressao regular, ex:

datePattern = re.compile(r"""^(1) # todo o texto antes da data
    (2(3))-             # Um ou dois digitos para o mês
    (4(5))-             # Um ou dois digitor para o dia
    (6(7))             # Quatro digitos para o ano
    (8)$                # todo o texto apos a data
""", re.VERBOSE)        # VERBOSE permiti o usu de espacoes em branco
'''

datePattern = re.compile(r"""^(.*?) # todo o texto antes da data
    ((0|1)?\d)-         # Um ou dois digitos para o mês
    ((0|1|2|3)?\d)-     # Um ou dois digitor para o dia
    ((19|20)\d\d)      # Quatro digitos para o ano
    (.*?)$              # todo o texto apos a data
    """, re.VERBOSE)        # VERBOSE permiti o usu de espacoes em branco


# Percorre os arquivos do diretorio de trabalho atual com um loop
# amerFilename = Filename em formato americano
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Ignora os arquivos que nao tenham uma data
    if mo is None:
        continue  # Faz o Loop volta para o inicio

    # Obetendo as diferentes partes do nome do arquivo
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Compoe o nome do arquivo em estilo europeu
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Obtem os paths absolutos completo do arquivos
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Renomeia os arquivos
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename)  # Descomente para funcionar o arquiov

    '''
    Exemplo de arquivo para renomear
    DE:   xpto-11-20-2018.tmp
    PARA: xpto-20-11-2018.tmp
    DE:   xpto11-20-2018.tmp
    PARA: xpto20-11-2018.tmp
    DE:   xpto2-5-2019.tmp
    PARA: xpto5-2-2019.tmp
    '''

# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 9 pos 6100
# github https://is.gd/Mv8f8E
