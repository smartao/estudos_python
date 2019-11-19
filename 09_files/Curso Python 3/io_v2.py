#!/usr/bin/python3
#
'''
Leitura via stream
Versao mais otimizada pos na linha do arquivo anterior
dados = arquivo.read()
Faz com que todo o arquivo seja carregado na memoria do computador!
Se tiver 100Mb sera usado 100Mb de memoria RAM

Em compensasao aqui usamos o for que le o arquivo sob demanda
Esse técnica se chama stream, mesma utilizados por videos online
Para ir na metade do vídeo carregamos em memoria apenas o necessário
'''

arquivo = open('pessoas.csv')  # Abrindo o arquivo
for registro in arquivo:  # lendo sob demanda
    print('Nome: {} Idade: {}'.format(*registro.split(',')))
arquivo.close()  # Fechando o arquivo

'''
Caso queria usar o f-print seria das seguintes formas
forma1
partes = registro.split(',')
print(f'Nome: {partes[0]}, Idade: {partes[1]}')
Forma2
print(f'Nome: {*registro.split(',')[0]}, Idade:{*registro.split(',')[1]}')
'''

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 97 a 107
# https://github.com/cod3rcursos/curso-python/tree/master/manipulacao_arquivos
