#!/usr/bin/python3
from random import randint

'''
Nesse exemplo sera usando o laço for junto com a break + else
No Exemplo a baixo o Break server para nao executar a estrutura else do laco
Em python é permitido declarar o else sem estar diretanete liagado ao if
'''

print('\nExemplo simples de for + break + else')
for i in range(1, 11):
    if i == 6:  # Quando i == 6
        break  # Said do laco
    print(i)
else:  # Quando i == 6 o else sera ignorado
    print('Fim!')

'''
Exemplo mais complexo
Inventado na aula 81 pelo instrutor

Descricao
Criar uma funcao sortear_dado, com numeros de 1 a 6
For com range 1 a 6, sendo entao repetido as tentativas 6 vezes
Se for impar, continue
Se for par e for igual ao valor sorteado
pela funcao sortear_dado, imprimir ACERTOU e depois chamar o break
se nao acertar chamar o else, imprimir NAO Acertou o numero

Nesse caso sempre que for o numero for impar o programa nao conseguira acertar
'''


def sortear_dado():
    return randint(1, 6)


print('\nIniciando programa para tentar acertar o numero:')
for i in range(1, 7):
    if i % 2 == 1:  # Excluindo os numeros impares
        continue

    if sortear_dado() == i:
        print('ACERTOU', i)
        break  # saindo do programa porque acertou
else:
    print('Não acertou o número!')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 77 a 81
# https://github.com/cod3rcursos/curso-python/tree/master/estruturas_controle
