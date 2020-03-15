#!/usr/bin/python3

'''
Geralmente é o código que chama a funcao, e nao a funcao em si, que sabe como
tratar uma execao.
Portanto, normalmente você verá uma instruo raise em uma função e as instruções
try e excepton no código que chama a funcao. Exemplo
'''


def boxPrint(symbol, width, height):
    # Funcao que imprime uma caixa na tela
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be a greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


# Armazenando os parametros das tuplas em variaveis simples
for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:  # Testando funcao no bloco try
        # Executando a funcao com os parametros recebidos
        boxPrint(sym, w, h)
    # Caso ocorra alguma execao
    except Exception as err:
        # A Excecao retorna em raise Exception sera armazenada na variavel err
        # Dessa forma conseguindo imprimir a mensagem a baixo, mais o retorno
        # Da execacao que ocorreu na funcao
        print('An Exception happened: ' + str(err))


# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 10 pos 6424
