#!/usr/bin/python3

'''
No Linux pode ocorrer o erro: locale.Error: unsupported locale setting

Para corrigir execute
1 - sudo dpkg-reconfigure locales.
2 - Marque o locale desejado, neste caso pt_BR.UTF-8 e confirme.
3 - Depois coloque no código,  acrescente .UTF-8  no setlocale(LC_ALL, 'pt_BR')
4 - setlocale(LC_ALL, 'pt_BR.UTF-8') → modo que funcionou no meu

'''


from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
# setlocale(LC_ALL, 'pt_BR')  # Exemplo para windows
setlocale(LC_ALL, 'pt_BR.UTF-8')

# Listar todos os meses do ano com 31 dias
# 1. (filter) pegar os indices de todos os meses com 31 dias 1, 3, 5...
# 2. (map) transformar os índices em nome
# 3. (reduce) juntar tudo para imprimir
meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nomes = map(lambda mes: month_name[mes], meses_31)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                      meses_nomes, 'Meses com 31 dias:')

print(juntar_meses)
# Metodo acima mais organizado!

print(
    reduce(
        lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
        map(
            lambda mes: month_name[mes],
            filter(
                lambda mes: mdays[mes] == 31,
                range(1, 13)
            )
        ),
        'Meses com 31 dias:'
    )
)

# Fontes:
# Curso Python 3 - Curso Completo do Básico ao Avançado Udemy Aula 181 e 182
# https://github.com/cod3rcursos/curso-python/tree/master/programacao_funcional
