#!/usr/bin/python3
import shelve
import pprint
import myCats

'''
Resumo
Em python, há tres passos para ler e escrever em arquivos:
1 - Chamar a funcao open() para que um objeto file seja retornado.
2 - Chamar o método read() ou write() do objeto File.
3 - Fechar o arquivo chamando o método close() no objeto File.
Obs: Lembrando que estamos falando de arquivos de textos simples
'''

'''
Abrindo aquivo com a funcao open()
open (), passe um path em forma de string indicando o arquivo que você
deseja abrir; poderá ser um path absoluto ou relativo. A função open()
retorna um objeto File
'''

helloFile = open('./hello.txt')

'''
Lendo o conteudo dos arquivos
Se quiser ler todo o conteúdo de um arquivo como um valor string, utilize
o método read() do objeto File
'''

helloContent = helloFile.read()
print(helloContent)

print('Lendo linha por linha do arquivo')
frasesFile = open('frases.txt')
print(frasesFile.readlines())

'''
Escrevendo em arquivos
O modo de escrita sobrescreverá o arquivo existente e começará do zero,
como ocorre quando o valor de uma variável é sobrescrita com um novo valor
O mode de adição, adicionara o texto no final do arquivo existente
Se o nome do arquivo passado para open() não existir, ambos os modos criarão
um novo arquivo vazio
Obs:
O método write() não acrescenta um caractere de quebra de linha
automaticamente no final da string, sendo necessário fazer isso de forma manual
'''

baconFile = open('bacon.txt', 'w')
# Mostrando o numero de caracteres escritos
print(baconFile.write('Hello world!\n'))
baconFile.close()  # Fechando o arquivo

baconFile = open('bacon.txt', 'a')
print(baconFile.write('Bacon is not a vegetable.'))
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

'''
Salvando variáveis como o módulo shelve
É possível salvar variaveis em seus programas Python em arquivos shelf binários
usando o módulo shelve, ele permitirá adicionar funcionalidade Save e Open
nos programas. Os valores de shelf nao precisam ser abertos em modo leitura
ou escrita, ambas as operacoes serao permitidas
necessário usar o import shelve
'''

shelfFile = shelve.open('mydata')  # Nome do arquivo mydata
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

print('\nUsando o shelve para salvar dados')
shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

'''
Assim como os dicionarios, os valores de shelf tem métodos keys() e values()
que retornarao as chaves e os valores do shelf em formatados semelhantes a
listas.
Como esses metodos retornaram valores semelhantes a listas, e nao listas de
verdade, voce deve passa-los a funcao list() para obtelos em forma de lista
'''

print('\nUsando o método list para transformar em listas')
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

'''
Salvando variaveis com funcao pprint.pformat()
A chamada pprint.pformat() fornecerá uma string que poderá ser gravada em
um arquivo .py. Esse arquvio será seu próprio módulo, que poderá ser importado
sempre que voce quiser usar as variaveis armazenadas nele.
necessário import pprint
'''

cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))  # Exemplo de impressao
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

'''
Utilizamos pprint.pformat() para retornar a lista como uma string
assim facilitando para gravar esses dados em um arquivo
'''

'''
Como os scripts Python em si são apenas arquivos textos como a extensao
.py, seus programar podem até mesmo gerar outros programas em python.
'''

print('\nImportando o modulo myCats')
# import myCats  # Adicionado no inicio do arquivo
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])

'''
Somente tipos de dados básicos como inteiros, números de ponto flutuante,
strings, lista e dicionarios podem ser gravados em um arquivo texto simples
'''

# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 8
