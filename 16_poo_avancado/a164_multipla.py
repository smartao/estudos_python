#!/usr/bin/python3

'''
Heranças multiplas
Python é uma das poucas linguagem que suporta heranças multiplas
o C++ também suporta

Herançar simples, uma classe pode ter apenas uma classe pai
Herança multiplas, uma classe pode ter várias classes pai

Nesse exemplo sera usando do homen aranha, que tem herança de homen quanto de
aranha


'''


class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        # Somando duas tuplas
        return super().capacidades + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + \
            ('bater em bandidos', 'atirar teias entre prédios')


if __name__ == '__main__':
    john = Homem()
    print(f'John: {john.capacidades}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')

    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidades}')

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 164
# https://github.com/cod3rcursos/curso-python/tree/master/poo_avancada
