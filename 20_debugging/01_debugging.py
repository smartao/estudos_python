#!/usr/bin/python3

'''
Atencao
A maioria dos codigos desse arquivo estao comentados pois os mesmos geram
exececoes para executados utilizado o atalho no Code de Ctrl+Alt+N
'''

'''
Podemos gerar nossas próprias execocoes pno codigo
Gerar uma excecao e uma maneira de dizer "Pare de executar o codigo dessa
funcao e passe a executar do programa para a instrucao except"
As exceoes sao geradas com uma instrucao raise. No codigo uma instrucao raise
é constuitda das seguintes partes:
- a palavra-chave raise;
- uma chamada a funcao Exception();
- Uma string com uma mensagem de erro conveniente passada para a funcao
Exception()

Se nao houver nenhuma instrucao try e except para cuidar da instrucao raise
que gerou a execao, o programar simplesmente falhara e exibira a mensagem de
erro da excecao
'''

# Exemplo
# raise Exception ('this is the erro message')
print('Executar o script 02_boxprint.py que tem mais detalhes')

'''
Obetendo o traceback com uma string
O traceback inclui:
a mensagem de erro
o número da linha que provocou o erro e
a sequencia de chamadas de funcao que resultou o erro
Esse sequencia de chamadas se chama pilha de chamada (call stack)
'''

print('Executar o script 03_errorExample_v1.py que tem mais detalhes')

'''
O Traceback é exibido pelo python sempre que uma exececao gerada nao é tratada
Porem tambem podemos obtelo como uma string chamando traceback.format_exc().
Essa funcao será útill se quisermos obter informacoes do traceback de uma
execacao, mas também quisermos que uma instrucao execept trate a execacao de
modo elegante

Por exemplo, em vez de fazer o programa falha assim que uma excecao ocorrer,
podemos gravar as informações de traceback em um arquivo de log e manter o
programa funcionando.
'''

print('Executar o script 03_errorExample_v2.py que tem mais detalhes')

'''
Assercoes
'''

# Fonte
# Livro Automatiando tarefas maçantes com python, capitulo 10
