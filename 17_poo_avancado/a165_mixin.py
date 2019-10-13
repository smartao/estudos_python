#!/usr/bin/python3

'''
Mixin server para fazer uma mistura entre classes
Utilizando herancas multiplas, várias APIs do python utilizando esse recurso

Na aula 166 mostra o diagrama de como funciona o mixin

'''


class HtmlToStringMixin:
    def __str__(self):
        # Conversão para HTML
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + ' (pet)' if self.pet else ''


class PessoaHtml(HtmlToStringMixin, Pessoa):
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    p1 = Pessoa('Maria Eduarda')
    print(p1)

    p2 = PessoaHtml('Roberto Carlos')
    print(p2)

    toto = AnimalHtml('Totó')
    print(toto)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 165 e 166
# https://github.com/cod3rcursos/curso-python/tree/master/poo_avancada
