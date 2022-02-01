from SISTEMA.lib.tratamento import *


# Função com linha horizontal para deixar o mini sistema mais estiloso
def linha():
    return '_' * 65


# Função com título principal entre linhas
def formato(msg):
    print(linha())
    print(f'{msg:^65}')
    print(linha())


# Função com menu feito através do for, dando entrada na opção e retornado o valor da opção
def menu(lista):
    for contador, valores in enumerate(lista):
        print(f'{contador + 1} - {valores}')
    print(linha())
    opcao = leiaint('Sua opção: ')
    print(linha())
    return opcao
