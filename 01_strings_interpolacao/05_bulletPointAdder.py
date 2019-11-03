#!/usr/bin/python3
import pyperclip

'''
Acrescenta marcores da wikipedia no inicio de cada linha de texto

Queremos que o programa bulletPointAdder faça o seguinte
1 - Obetenha o texto do clipboard
2 - Faca algo com ele
3 - Copiar o novo texto para o Clipboard
'''

text = pyperclip.paste()

# Separa as linhas e acresta os asteriscos.
lines = text.split('\n')

# percorre todos os indicies da lista 'lines'
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]  # Acrescenta um asterisco em cada string
text = '\n'.join(lines)
pyperclip.copy(text)

# Observao, nao saira nada na tela, o retorno sera no proprio clioboard!

# Fontes
# Livro Automatiando tarefas maçantes com python, posicao 4162
