#!/usr/bin/python3

'''
Contador de quantos objetos foram criados


'''


class ClasseSimples:
    contador = 0

    def __init__(self):
        # self.__class__.contador += 1
        self.contar()

    @classmethod
    def contar(cls):
        cls.contador += 1


if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador)  # Esperado 3

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 168 e 169
# https://github.com/cod3rcursos/curso-python/tree/master/poo_avancada
