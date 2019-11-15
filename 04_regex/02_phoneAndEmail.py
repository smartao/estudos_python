#!/usr/bin/python3
import pyperclip
import re


'''
Projeto extrator de número de telefone (posicao 4899)

O extrator de número de telefone e de endereços de email deverá fazer:
- Obter o texto do clipboard
- Encontrar todos os número de telefone e os endereços de email do texto
- colá-los no clipboard
'''


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Codigo de área
    (\s|-|\.)?          # Separador
    (\d{3})             # Primeiros 3 digitos
    (\s|-|\.)           # Separador
    (\d{4})             # Ultimos 4 digitos
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # Extensao
    )''', re.VERBOSE)

'''
O formato dos endereços de email tem muitas regras singulares. Essa regex
não corresponderá a todos os endereços poss[iveis de email, porém corresponderá
a quase todos os endereços tipicos.
'''

text = str(pyperclip.paste())

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%=-]+   # Nome do usuario
    @                   # Simbolo de @
    [a-zA-Z0-9.-]+      # Nome do dominio
    (\.[a-zA-Z]{2,4})   # ponto seguido de outros caracteres
)''', re.VERBOSE)

matches = []  # Armazenando as correspondencias em uma lista
for groups in phoneRegex.findall(text):  # EXPLICACAO 1
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):  # EXPLICACAO 2
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))  # EXPLICACAO3
    print('Copied to cliboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')


'''
Explicacao 1
Para número de telefones, queremos queesse número seja concatenando em
um formatado único e padrão, contendo os grupos, código de área [1], três
primeiros números [3], quatros ultimos digitos [5] e a extenção [8]
Explicacao 2
Para endereços devemos concatenar o grupo 0 de cada correspondencia
Explicacao 3
Lembrando que pyperclip suporta apenas um string, por isso devemos usar
o método join para juntar

Texto para testar o programa
(11) 800-444-3333 55.700-333-5431 sergei@gmail.com tieni@bol.com
99-111-341-9898 111-341-9898 111-341-9898 xxx@xxx.com.br
'''

# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 7
