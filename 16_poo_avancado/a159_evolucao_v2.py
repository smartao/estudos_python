#!/usr/bin/python3

'''
Metodos disponveis em pythone
metodo de instancia, recebe a instancia como primeiro parametro, tem o self
metodo de classe, recebe a classe como primeiro parametro
Obs: Em alguns linguagem nao tem diferente de metodo de classe e instancia
porem no python existe esse diferenca
metodo estático, nao recebe nenhum parametro, e utiliza o decorator
o método estatico de classe escebe apenas a classe utilizando cls

O cls é polimosfirmo, podemos chamado de multplas formas diferentes


'''


class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod  # Metodo estatico
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        # Gerando uma tupla com todos os adjetivos
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod  # Metodo de classe
    def is_evoluido(cls):  # cls = classe, mesmo que o self
        # Verificar se é a ultima especies retornando pela funcao anterior
        # caso for a ultima quer dizer que é evoluido, repare o nome da classe
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):  # Subclasse
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):  # Subclasse
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    # Outra forma de utilizar, usando a classe e passando a instancia
    # Poem menos recomendado
    # HomoSapiens.das_cavernas(jose)

    grokn = Neanderthal('Grokn')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluído? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluído? {Neanderthal.is_evoluido()}')
    print(f'José evoluído? {jose.is_evoluido()}')
    print(f'Grokn evoluído? {grokn.is_evoluido()}')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 159
# https://github.com/cod3rcursos/curso-python/tree/master/poo_avancada
