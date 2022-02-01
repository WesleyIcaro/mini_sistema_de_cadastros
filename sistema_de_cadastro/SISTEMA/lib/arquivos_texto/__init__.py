from SISTEMA.lib.interface import *


# Fazer uma função capaz de criar um arquivo de texto se não tiver criado um outro antes
def criararquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print(f'Erro ao criar o arquivo {arquivo}')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!')


# Criar uma função capaz de inserir os dados em um arquivo de texto
def cadastrararquivos(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('\33[31mErro ao inserir dados no arquivo de texto!\33[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'\33[31mNão foi possível inserir dados no arquivo {nome}')
        else:
            print(f'Dados de {nome} adicionados com sucesso!')
            a.close()

# Fazer função capaz de ver os dados cadastrados
def exibirarquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print(f'\33[31mNão foi possível exibir o arquivo {arquivo}!\33[m')
    else:
        formato('VER PESSOAS CADASTRADAS')
        for linhas in a:
            dados = linhas.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<45}{dados[1]:>4} anos')
    finally:
        a.close()


# Função capaz de conferir se arquivo existe
def arquivoexiste(arquivo):
        try:
            a = open(arquivo, 'rt')
            a.close()
        except:
            print(f'\33[31mArquivo {arquivo} não existe!\33[m')
            return False
        else:
            print(f'O arquivo {arquivo} foi encontrado com sucesso!')
            return True
