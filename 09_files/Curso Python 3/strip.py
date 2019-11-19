#!/usr/bin/python3
#

a = "       esacoes em branco        "
b = "000000 variavelB 0000000"
c = "        000000 variavelC 0000000         "

# Removendo os espacoes laterias da variavel A
print(f'variavel A: {a.strip()}')

# Removendo os 0 da variavel B, porem ainda fica os 2 espacoes em brancos
print(f'variavel B:{b.strip("0")}')

# Remomvendo os 0 e espacoes em brancos da variaavel C
print(f'variavel C:{c.strip().strip("0").strip()}')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 100
# https://github.com/cod3rcursos/curso-python/tree/master/manipulacao_arquivos
