#!/usr/bin/python3
# mcb.pyw - Multiclipboard
# A program that can save and load pieces of text to the clipboard.
# Usage: python3 mcb.pyw save <keyword> - Saves clipboard to keyword.
#        python3 mcb.pyw <keyword> - Load keyword to clipboard.
#        python3 mcb.pyw list - Load all keywords to clipboard.

'''
Podemos criar um programa Python que controle diversas porçoes de texto.
Esse "Multiclipboard" se chamara mcb.pyw.
A extensão .pyw que dizer que o Python não mostrará uma janela do terminal
quando executar esse programa

Eis o que o programa faz:
O Argumento de linha de comand para palavra-chave é verificado.
Se o argumento for save, o conteúdo do clipboard será salvo como palavra-chave.
Se o argumento for list, todas as palvras-chaves serão copiadas para clipboard
Caso contrário, o texto da palavra-chave será copiada para o clipboard.

Isso siginfica que o código deverá fazer o seguinte
Ler os argumento de linha de comando em sys.argv.
Ler e escrever no clipboard.
Savar e carregar um arquivo shelf.
'''

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb.tmp')

# Se existir 3 argumentos, visto que o zero sempre o nome do programa e
# Se o primeiro argumento, que sera o indice 1 da lista sys.argv, for 'save'
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # O segundo arg será a palavra chave para o conteudo atual do clipboard
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# Se houver apenas um argumento...
elif len(sys.argv) == 2:
    # Verificar se é list, caso seja
    if sys.argv[1].lower() == 'list':
        # Uma representacao em string da lista de chaves do shlef
        # sera copiada para o clipboard
        pyperclip.copy(str(list(mcbShelf.keys())))
    # Caso nao seja list, suporemos que o argumento seja uma palavra chave
    # Se essa palavra chave existir no shelf mcbShelf como chave, poderemos
    # carregar o valor no clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
# Assim listara palavras-chave e carregara no conteudo

# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 8 pos 5690
