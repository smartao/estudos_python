#!/usr/bin/python3

'''



'''


from a186_generators_v1 import cores_arco_iris

if __name__ == '__main__':
    generator = cores_arco_iris()
    for cor in generator:
        print(cor)
    print('Fim!')


# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 187
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
