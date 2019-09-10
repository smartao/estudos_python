#!/usr/bin/python3

print('\nFor percorrendo as letras de uma palavra')
palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=',')
print('Fim')

print('\nFor precorrendo uma lista')
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

print('\nFor percorendo um lista a lista retornando o indice')
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

# Criando uma tupla
dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
print('\nFor percorrendo um tupla')
for dia in dias_semana:
    print(f'Hoje é {dia}')

print('\nPercorendo um conjunto')
for numero in {1, 2, 3, 4, 5, 6}:  # criando um conjunto (set)
    print(numero)


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 77 a 81
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
