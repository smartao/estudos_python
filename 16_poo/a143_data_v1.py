#!/usr/bin/python3

'''
notacoa de classe usa CamelCase

class Data:
    def __str__(self):
        Todo método dentro de uma classe por convenção deve
        utilizar a palavra self, é o objeto que esta sendo acessado
        naquele momento

     def __str__
     Método especial suportado por todos os objetos do python
     ele serve para imprimir o retorno sem precisar chamar o método em si
     Exemplo sem o método especial
     print(d1.__str__)
     utilizando o método __str__
     print(d1)
'''


class Data:
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1)

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 143
# https://github.com/cod3rcursos/curso-python/tree/master/poo
