#!/usr/bin/python3

'''
Explicao do conceito atributo de instantancia vs de objeto
ou Membro de classe vs membro de instancia ocorreu na aula 157

Atributo de classe significa que o valor tem apenas uma cópia e é
compartilhado com todos os objetos, caso o valor mude sera alterado
em todos os objetos pertencentes a essa classe

Nesse exemplo é criado um atributo da classe e um atributo da instancian
Por padrao todo método retorna None, quando colocar o serf o fica como True
Demonstracao de encadeamento de chamadas de objetos linha 33,
sempre que uma funcao retornar self podemos chamar uma outra funcao
'''


class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        # Atributo que pertence a instancia (objeto)
        self.especie = 'Homo Neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 158
# https://github.com/cod3rcursos/curso-python/tree/master/poo_avancada
