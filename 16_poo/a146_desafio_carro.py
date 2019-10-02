#!/usr/bin/python3

'''

def __init__(self, dia=1, mes=1, ano=1970):
é um construtor da classe, e python nao permite que tenha mais do
que um por classe, contudo pode-se usar parametro padrao no chamada
do objeto

'''


class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        maxima = self.velocidade_maxima
        nova = self.velocidade_atual + delta
        # If validando a velocidade maxima, operador ternario
        self.velocidade_atual = nova if nova <= maxima else maxima
        return self.velocidade_atual

    def frear(self, delta=5):
        nova = self.velocidade_atual - delta
        # if validando a velocidade minima que é 0
        self.velocidade_atual = nova if nova >= 0 else 0
        return self.velocidade_atual


if __name__ == '__main__':
    c1 = Carro(180)  # Passando a velocdiade maxima

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 146
# https://github.com/cod3rcursos/curso-python/tree/master/poo
