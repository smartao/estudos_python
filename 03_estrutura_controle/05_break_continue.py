#!/usr/bin/python3

'''
Conceitos
Continue
Interrompe a repeticao do laço e vai para a próxima repetição

No exemplo a baixo
colocando o continue sempre que o resto da divicao de x por 2
for igual a 0
ocorrerá o continue e o valor nao sera impresso
Assim imprimindo apenas os números impares

Break
Interrompe o laço inteiro
Quando x for igual a 5 ocorre o break e sai do laço
Nem mesmo executando o print
'''
# Imprmindo apenas os numero impares
print('Exemplo de estrutura de laço com continue')
for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)

print('\nExemplo de estrutura de laço com break')
for x in range(1, 11):
    if x == 5:
        break
    print(x)

print('Fim!')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 80
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
