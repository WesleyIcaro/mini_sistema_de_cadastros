from SISTEMA.lib.arquivos_texto import *

arquivo = 'lista.txt'
if not arquivoexiste(arquivo):
    criararquivo(arquivo)

opcoes = ['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair']

while True:
    formato('MENU PRINCIPAL')
    opcao = menu(opcoes)
    if opcao == 1:
        exibirarquivo(arquivo)
    elif opcao == 2:
        formato('CADASTRAR NOVAS PESSOAS')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrararquivos(arquivo, nome, idade)
    elif opcao == 3:
        print('Programa finalizado, obrigado e volte sempre!')
        break
    else:
        print('\33[31mEssa opção é inválida, por favor tente novamente!\33[m')

