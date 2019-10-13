#!/usr/bin/python3

'''
Propriedades do objeto, usando get e set
self._idade = None
_ = significado que é um atributo privado, porem, o conceito de privado em
    Python é uma convenção e não um recurso forçado pela linguagem, o
    sublinhado diz ao desenvolvedor que ele não deveria estar acessando aquele
    membro da classe.

O set é importante pois podemos colocar validacoes nele, impedindo que qualquer
valor se atribuido ao objeto


'''


class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if idade < 0:  # Validando se o valor da idedade nao é negativo
            raise ValueError('Idade deve ser um número positivo!')
        self._idade = idade  # Caso positivo defini a idade

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    jose.set_idade(40)
    print(f'Nome: {jose.nome} Idade: {jose.get_idade()}')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 160
# https://github.com/cod3rcursos/curso-python/tree/master/poo_avancada
