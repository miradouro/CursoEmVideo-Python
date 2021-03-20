num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Digite sua opção: '))
if opcao == 1 or opcao == 2 or opcao == 3:
    print('Sua opção: {}'.format(opcao))
    if opcao == 1:
        print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
    elif opcao == 2:
        print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
    elif opcao == 3:
        print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('\033[1;31mOpção INVALIDA\033[m\nTente novamente!')

