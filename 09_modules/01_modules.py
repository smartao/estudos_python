#!/usr/bin/python3
#
'''
A Module can be included in another Python program by using the "import" statement followed by 
the module name
Ex

import time
time.method_name()
time.attribute_name

'''

'''
Python is distributed with a large library of modules.
Check the Python standard library before writing any of you own code!

Just a few modules:
cvs
logging
urllib.request
json

Pesquisar no site
https://docs.python.org/3/library

'''


print('\nImportando o modulo time e utilizando')
import time
print(time.asctime())
print(time.timezone)

# Importanando apenas o metodo asctime
print('\nImportando apenas o metodo asctime do modulo time')
from time import asctime
print(asctime())

'''
from module_name import method_name
from module_name import method_name1, method_nameN
'''

# Importando dois metodos do modulo tempo
print('\nImportando o metodo asctime e o sleep do modulo time')
from time import asctime, sleep
print(asctime())
sleep(2) # funciona igual ao sleep do linux
print(asctime())

# Importando todos os metodos de um moduloe
print('\nImportando todos os metodos de um modulo, nao recomendando fazer dessa forma!')
#from time import *
#print(timezone)
print(asctime())
sleep(2)
print(asctime())

'''
Verificando os métodos e atributos que um modulo tempo
execute o comando no terminal do linux, exemplo do modulo time

$ python3
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> import time
>>> dir(time)
['CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME', 'CLOCK_THREAD_CPUTIME_ID', '_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock', 'clock_getres', 'clock_gettime', 'clock_settime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'perf_counter', 'process_time', 'sleep', 'strftime', 'strptime', 'struct_time', 'time', 'timezone', 'tzname', 'tzset']
>>> 
'''

# Imprimindo o diretorio de modulos do python e adicicionado para pesquisar
# Modulos no diretorio /home/sergei
print('\nImprimindo o diretorio de modulos do python')
import sys
sys.path.append('/home/sergei')
for path in sys.path:
    print(path)

'''
Também é possível manibular a variavel de ambiente PYTHONPATH 
Mac/Linux
PYTHONPATH=path1:pathN
Windows
PYTHONPATH=path1;pathN

Exemplo de adicionar um diretorio nos modulos de python

$ export PYTHONPATH=/usr/local/python/modules
$ /usr/bin/python3 /home/sergei/Desktop/estudos_python/09_modul
es/show_module_path.py

/home/sergei/Midias/Desenvolvimento/Github/estudos_python/09_modules
/usr/local/python/modules
/usr/lib/python36.zip
/usr/lib/python3.6
/usr/lib/python3.6/lib-dynload
/usr/local/lib/python3.6/dist-packages
/usr/lib/python3/dist-packages
'''

print('\nUsando o modulo sys para retornar codígo de saida especifico 1')
import sys
file_name = '09_modules/test1.txt'
try:
    with open(file_name) as test_file:
       for line in test_file:
           print(line)
except:
    print('Could not open {}.'.format(file_name))
    # sys.exit(1) # Linha comentada para seguir com a execucao do programa


# Exemplo de como importar um modulo de outro arquivo
print('\nImportando um mudulo de outro arquivo')
import say_hi2
say_hi2.say_hi()

print('\nImportando um mudulo de outro arquivo e ignorando a funcao principal')
import say_hi3
say_hi3.say_hi()

#
# Fontes: 
#Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 72 e 74