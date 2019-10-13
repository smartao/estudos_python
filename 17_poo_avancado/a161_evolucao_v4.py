#!/usr/bin/python3

'''
Utilizando os decorator @property e @idade.setter
Com isso nao precisamos mais utilizar .get_idade e .set_idade
Antes:
jose.set_idade(40)
jose.get_idade()
Depois:
jose.idade = 40
jose.idade
Maior vantagem é que parece que estamos usando atributos de instancias normais
mas internamente isso é convertido para o método get e set

'''


class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')
        self._idade = idade

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
    jose.idade = 40
    print(f'Nome: {jose.nome} Idade: {jose.idade}')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 161
# https://github.com/cod3rcursos/curso-python/tree/master/poo_avancada
