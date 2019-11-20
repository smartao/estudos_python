#!/usr/bin/python3
import random

'''
Eis o que o programa faz
Cria 35 provas diferentes.
Cria 50 perguntas de multiplas escolhas para cada prova em ordem aleatória
Fornece resposta correta e três respostas incorretas aleatória para cada
pergunta em ordem aleatória
Grava as provas em 35 arquivos de texto
Grava os gabaritos contendo as repostas em 35 arquivos de texto
'''
# Os dados para as provas.
# As chaves são os estados e os valores são as capitais
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento',
            'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
            'Idaho': 'Boie', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
            'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oaklahoma': 'Oaklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}

# Gera os arquivos contendo as provas, total de 35 provas
for quizNum in range(35):
    # Criar os arquivos com as provas e os gabaritos das respostas
    quizFile = open('quiz/capitalsquiz%s-tmp.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('quiz/capitalsquiz_answers%s-tmp.txt' % (quizNum + 1), 'w')

    # Escreve o cabeçalho da prova
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)\n\n' % (quizNum + 1))

    # Coleta todos os estados em uma lista chamado states
    states = list(capitals.keys())
    # Embaralha a ordem dos estados para gerar perguntas aleatorias
    random.shuffle(states)

    # Percore todos os 50 estados em um loop, criando uma pergunta para cada um
    for questionNum in range(50):
        # Guardando o restado correto da pergunta em um string
        # capitals é o dicionario, que pega a lista state com o index
        correctAnswer = capitals[states[questionNum]]
        # Criando uma lista com todos os valores do dicionario capitals
        wrongAnswer = list(capitals.values())
        # Apagando a resposta correta da lista
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        # Selecionando 3 valores aleatorios dessa lista de respostas erradas
        # random.sample, 1 arg, lista para fazer a selecao
        # 2 arg, quantidade de valores que deseja selecionar
        wrongAnswer = random.sample(wrongAnswer, 3)
        # Adicionamos [] para transformamos correctAnswer em uma lista
        # e assim jutamos com a lista wrongAnswer adicionadno o sinal +
        # dessa forma criamos uma lista completa com 4 opcoes de resposta
        answerOptions = wrongAnswer + [correctAnswer]
        # As respostas sao embaralhadas novamente
        # para que a reposta correta nao seja sempre a letra D
        random.shuffle(answerOptions)

        # Escrevendo no arquivo texto a pergunta
        quizFile.write('%s. What is the capital of %s?\n' %
                       (questionNum + 1, states[questionNum]))

        # Loop para escrever as 4 opcoes de reposta baseado na
        # lista answerOption
        for i in range(4):
            # A expressao 'ABCD'[i] trata a string 'ABCD'como um array que
            # sera avaliada como A,B,C,D nas posicoes 0,1,2,3
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))

        quizFile.write('\n')  # Pulando linha para proxima pergunta

        # ### Grava o gabarito com as respostas em um arquivo ###
        # A expressao [answerOptions.index(correctAnswer)]) encontrará o índice
        # inteiro da resposta correta nas opções de resposta ordenanda
        # aleatoriamente
        # e 'ABCD'[answerOptions.index(correctAnswer)])) será
        # avaliada com a letra da resposta correta, que será grava no arquivo
        # contendo o gabarito
        # questionNum + 1 para nao comecar na pergunta zero e sim na 1
        answerKeyFile.write('%s. %s\n' % (
            questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

# Fechando os arquivos
quizFile.close()
answerKeyFile.close()

# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 8 pos 5520
