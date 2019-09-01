#!/usr/bin/env python3


def say_hi():
    print('Hi!')


def main():
    print('Hello from say_hi3.py!')
    say_hi()

# com isso a funcao principal sera ignorada no momento da importancao
# e assim consiguiremos apenas usando a funcao say_hi
# Caso a chamado seja para o main, ai sim todo o codigo sera executado
if __name__ == '__main__':
    main()

#Fontes
##Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 73