#!/usr/bin/python3

import traceback

try:
    raise Exception('This is the erro message')
except Exception:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to error info.txt')

# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 10
