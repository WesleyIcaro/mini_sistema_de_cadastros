# Fazer uma função capaz de tratar os erros de números inteiros
def leiaint(msg):
    while True:
        try:
            opcao = int(input(msg))
        except ValueError:
            print('\33[31mO valor digitado é inválido!\33[m')
            continue
        except KeyboardInterrupt:
            print(f'\33[31mO programa foi fechado sem colocar os valores!\33[m')
            break
        else:
            return opcao
