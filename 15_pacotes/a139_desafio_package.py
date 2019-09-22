#!/usr/bin/python3


from app.utils.gerador import novo_nome
from app.negocio import nome_existe
from app.negocio.backend import add_nome


def main():
    while True:
        nome = novo_nome()
        if not nome_existe(nome):
            add_nome(nome)
            break

    print(f'Criado novo nome de testes: "{nome}"')


if __name__ == '__main__':
    main()

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 139
# https://github.com/cod3rcursos/curso-python/tree/master/pacotes
