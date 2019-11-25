#!/usr/bin/python3
import re

'''
Expressoes regualres
'''

'''
search() group()

O método search() retornará None se o padrao da regex não for encontrado
string. Se o padrão for encontrado retornaráum objeto Match.
Objetos Matchs tem um método group() que retornará o texto correspondente
extraido da string pesquisasa

Obs: Usamos o r' dentro do re.compile para assim passar um string pura
dessa forma o \d ou \n nao é tratado como cacteres de scape
'''

# Passando a exmpressao regular para uma variavel
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Funciona semelhante a linha de cima
phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# Fazendo uma string e fazendo a pesquisa baseado da regex
# passada anteriormente, o resultando sera armazenado na variavel mo
mo = phoneNumberRegex.search('My number is 415-555-4242')
# Imprimindo o valor foi encontrando, caso nao fosse retorna uma
# Exececao None
print('Exemplo simples de regex')
print('Phone number found: ' + mo.group())

'''
Resumo de uso

1 - Importar o modulo re
2 - Criar um objeto Regex usando a funcao re.compile()
    Lembre-se de usar uma string pura
3 - Passe a string que você quer pesquisar ao método search()
    Isso fará um objeto Match ser retornando
4 - Chame o método group() do objeto Match para retornar uma
    string com o texto correspondente
'''

'''
Agrupando com parênteses
A Adição de parenteses criará groups na regex, então voce podera usar
o método group do objeto de correspondencia

gropo 0 ou nao informando = retorna o texto correspondente completo
grupo 1 = primeiro conjunto encontrado
grupo 2 = segundo conjunto encontrado
'''

phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumberRegex.search('My number is 415-555-4242')

print('\nTeste de regex + grupos:')
print('Primeiro grupo: ' + mo.group(1))
print('Segundo grupo: ' + mo.group(2))
print('Texto equivalente da regex: ' + mo.group(0))

print('\nTodos os grupos em formato de tuplas:' + str(mo.groups()))
areaCode, mainNumber = mo.groups()
print('Codigo de area: ' + areaCode + '\nNumero principal: ' + mainNumber)

'''
Escapando dos caracteres pareneteses ()
Caso queria pesquisar por codigo de area que tenha parenteses ex, (415)
Sera necessário usar o \( \) para fazer a pesquisa
'''


phoneNumberRegex = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
mo = phoneNumberRegex.search('My number is (415)-555-4242')
print('\nTeste regex com caracteres de escape para ()')
print('Primeiro grupo: ' + mo.group(1))
print('Segundo grupo: ' + mo.group(2))

'''
Fazendo a correspondencia de vários grupos com pipe
Podemos usar o | em qualquer lugar em qualquer lugar em que quisermos
fazer a correspondência de uma entre várias epxressos
'''

print('\nTeste de regex usando o | pipe:')
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

'''
O Pipe também pode ser usado para fazer a correspondencia de uma entre diversos
padroes como parte de sua regex, por exemplo procurar tudo que comece com bat.
'''

print('\nTeste de regex usando pipe com várias correspondencias')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())  # Retornara o texto completo Batmobile
print(mo.group(1))  # Retornara apenas mobile

'''
Correspondencia opcional usando o ponto de interrogação
Ás vezes há um padrao ao qual você quer corresponder somente de formar opcional
O Caractere ? marca o grupo que o antecede como sendo uma parte opcional do
padrao
? = corresponde a 0 ou a uma vez que ocorrer no texto
'''

print('\nTeste de regex com cactere opcional (?)')
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

'''
Usando com número de telefone
Criando uma regex que procure numeros de telefone que tenha ou não
um código de área
'''

print('\nTeste regex com prefixo de telefone com o ?')
# Parametro opcional (\d\d\d-)?
phoneNumberRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneNumberRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneNumberRegex.search('My number is 555-4242')
print(mo2.group())

'''
Correspondendo a zero ou mais ocorrencias usando o asterisco
O * quer dizer, corresponda a zero ou a mais ocorrencias
O grupo que antecede o asterisco pode ocorrer qualquer numero de vezes no texto
'''

print('\nTeste de regex usando o asterisco *')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The adventures of Batwowowowowoman')
print(mo3.group())

'''
Correspondendo a uma ou mais ocorrenncias usando o sinal de adição
O sinal de + quer dizer, corresponde a uma ou mais ocorrencias
O grupo que antecede o asterisco deve aparecer pelo menos uma vez!
'''

print('\nTeste de regex usando o sinal de adicao +')
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwowowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)  # Imprimira True pois o valor é vazio

'''
Correspondendo a repetições especificas usando chaves

Se voce tiver um grupo que deseja repetir um núme especifico de vezes
insira um numero entre chaves após o grupo em sua regex. Exemplo
regex: (Ha){3} corresponde a string 'HaHahHa'

Em vez de um número, podemos especifica um intervalos especificando um minimo
e um máximo
regex: (Ha){3,5} corresponde a string 'HaHahHa' ,'HaHahHaHa', 'HaHahHaHaHahHa'

Também podemos deixar de fora o primeiorou ou o segundo número nas chaves para
deixar se especificar o minimo ou o máximo
regex: (Ha){3,} corressponde a tres ou mais instancias do 'Ha'
regex: (Ha){,5} corresponde a zero ou 5 intancias de 'Ha'
'''

print('\nTeste de regex usando repetições')
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 is None)  # Retornara True

'''
Correspondencia greedy e nongreedy

greedy (gulosa) as empressoes em python são assim por padrao
o que singifica que em situacoes ambiguas, a correspondencia sera feita com
a maior string possivel.
nongreedy (não gulosa), faz correspondencia com a menor string

Obs: que o pnoto de interrogacao pode ter dois significados, declarar uma
correspondencia noongreedy ou indicar um  grupo opcional
'''

print('\nExemplo de greedy e nongreedy regex')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHaHa')
print(mo2.group())

'''
Metodo findall()
Retornará, as string de todas as correspondencias na string pesquisa.
Nao retorna um objeto Match, mas uma lista de string (desde que nao haja
grupo de expressos regulares)
Se houver grupos na regex o findall retornará uma lista de tuplas
Cada tupla representará uma correspondencia identificada
'''

print('\nComparando search x findall')
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('Cell: 515-555-9999 Work: 212-555-9999')
print(mo.group())
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # SEM GRUPO
mo = phoneNumberRegex.findall('Cell: 515-555-9999 Work: 212-555-9999')
print(mo)  # Retorno em uma lista

print('\nMetodo findall com grupos')
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumberRegex.findall('Cell: 515-555-9999 Work: 212-555-9999')
print(mo)  # Retorno em uma lista de tuplas

'''
Classes de caracteres
\d - Qualquer digito
\D - Qualquer cactere NÃO digito
\w - Qualquer letra digita ou caractere undescore (palavras)
\W - Qualquer cactere que não seja letra digita ou caractere undescore
\s - Qualquer espaço, tabulação ou caractere de quebra de linha (espaco)
\S - Qualquer caractere que não seja, espaço, tabulação ou quebra de linha
'''

print('\nExemplo de Classe de caracteres')
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

'''
Criando suas própria classe de caractere (posicao 4701 kindle)
Podemos definir sua própria classe de cacteres usando colchetes.
Exemplos: a classe de caractere [aeiouAEIOU] corresponde a qualquer vogal
Outro exemplo [a-zA-Z0-9] corresponderá a todas a letras minusculas,
maisculas e numeros

Observe que nos colchetes [] os simbolos de regex não são interpretados.
Por exemplo a classe de caracteres [0-5.] corresponderá aos digitios de
0 a 5 e um ponto, não é preciso escrever essa classe como [0-5\.]
'''

print('\nTeste classe de caracteres')
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('Robocop eats baby food. BABY FOOD')
print(mo)

'''
Acento cincunflexo (^)
Ao inserir o ^ logo depois do colchete de abertura da classe de caracte,
podemos criar uma classe negativa de caractere
'''

print('\nClasse negativa de caractere')
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall('Robocop eats baby food. BABY FOOD')
print(mo)

'''
Acento circunflexo ^ e o sinal de dólas $

o acento ^ também pode ser usado no inicio de uma regex para indicar que
uma correspondenias deve ocorre no inicio de um texto pesquisado
e o sinal de dolar significa no final do texto

a regex r'\d$' corresponde a string que terminar com cactere numerico de 0 a 9
'''

print('\nTeste Acento circunflexo ^')
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello World')
print(mo.group())

print('\nTeste de regex de digitos')
endWithNumber = re.compile(r'\d$')
mo = endWithNumber.search('Your number is 42')
print(mo.group())

wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234567890')
print(mo.group())
mo = wholeStringIsNum.search('1234sfsdf7890')
# print(mo.group())  # Retorno sera None
mo = wholeStringIsNum.search('89 18203')
# print(mo.group())  # Retorno sera None

'''
Cactere curinga .
O caractere ponto (.) corresponde a qualquer caractere exceto 
uma quebra de linha
'''

print('\nRegex com caractere curinga')
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat')
print(mo)

'''
Correspondendo a tudo usando .*
Suponha que voce queira fazer correspondencia da string 'First Name:' seguida
de todo e qualquer texto seguido de 'Last Name:'
Podemos usando .* para indicar qualquer caractere
. = qualquer caractere único exceto a quebra de linha
* = zero ou mais ocorrencias do caracte anterior
'''

print('\nTeste correspondendo tudo usando .*')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

'''
Correspondendo tudo .* greedy e nongreedy
.* por padrao utiliza o modo greedy, sempre tentará corresponder ao
máximo de texto possível
Para corresponder a todo e qualquer texto em modo nongreedy, utilize .*?
assim informando ao python para usar nongreedy
'''

print('\nTeste correspondendo tudo usando .* greedy e nongreedy')
nongreedyHaRegex = re.compile(r'<.*?>')
mo = nongreedyHaRegex.search('<To server man> for dinner.>')
print(mo.group())
greedyHaRegex = re.compile(r'<.*>')
mo = greedyHaRegex.search('<To server man> for dinner.>')
print(mo.group())

'''
Correspondendo a caractere de quebra de linha
Ao passarmos o re.DOTALL como segundo argumento de re.compile(), podemos
fazer o caractere ponto corresponder a todos os caracteres, incluidno
quebra de linha
'''

print('\nCorrespondendo todos caracteres + quebra de linha')
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search(
    'Server the public trust.\nProtect the inoccent.\nUphold the law')
print(mo.group())
noNewlineRegex = re.compile('.*', re.DOTALL)
mo = noNewlineRegex.search(
    'Server the public trust.\nProtect the inoccent.\nUphold the law')
print(mo.group())

'''
Correspondendo sem case-sensitive
Utilize o parametro re.IGNORECASE ou re.I
'''

print('\nTeste case sensitive')
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('Robocop is part man, part machine, all copp')
print(mo.group())

'''
Substituindo string com método sub()
O método sub() dos objetos regex recebe dois argumentos
1 - argumento é uma string para substituir qualquer correspondencia
2 - é a string para expressão regular

Além disso, podemos digitiar \1 \2 \3 e assim por digante para dizer
insira o texto do grupo 1 2 3 e assim por diante na substituicao
'''

print('\nTeste método sub')
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub(
    'CENSORED', 'Agent Alice gave the secret docuemnts to Agent Bob')
print(mo)

print('\nTeste método sub avançada')
agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.sub(
    r'\1***', 'Agent Alce told Agent Carol tha Agent Eve knew Agent Bob was a double agent')
print(mo)

'''
Adminsitrando expressoes regular complexas
Para expressos mais complexas podemos dizer a funcao re.compile()
que ignore espacoes em branco e comentários na string
Observer que sera usado aspas triplas
'''
# agora em vez de uma expressão:
phoneRegex = re.compile(
    r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# Podemos fazer a expressao
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Codigo de área
    (\s|-|\.)?          # Separador
    \d{3}               # Primeiros 3 digitos
    (\s|-|\.)           # Separador
    \d{4}               # Ultimos 4 digitos
    (\s*(ext|x|ext.)\s*\d{2,5})?) # # Etensao
    )''', re.VERBOSE)

'''
Combinando re.IGNORECASE, re.DOTALL e RE.VERBOSE
re.compile() aceitar apenas um único valor como segundo argumetno
Portando, se  quiser uma expressao regular com vários argumentos a cima
é necessário usar o pipe para passar os argumentos

Também podemos passar outras opçoes para o segundo argumentos,
mas elas são bem incomuns
posicao livro 4889
'''

someRegexValor = re.compile('foo', re.IGNORECASE | re.DOTALL | re. VERBOSE)


# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 7
