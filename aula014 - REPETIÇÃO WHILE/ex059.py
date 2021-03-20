from time import sleep
n1 = 0
n2 = 0
menu = 0
soma = 0
mult = 0
while menu != 5:
    if n1 == 0 == n2:
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Numeros')
    print('[ 5 ] Sair do Programa')
    menu = int(input('Escolha uma opção acima: '))
    if menu == 1:
        soma = n1 + n2
        print('-=-'*15)
        print('A somatória dos valores informados é {}.'.format(soma))
        print('-=-'*15)
        menu = 0
    elif menu == 2:
        mult = n1 * n2
        print('-=-'*15)
        print('A multiplicação dos valores informados é {}.'.format(mult))
        print('-=-'*15)
        menu = 0
    elif menu == 3:
        if n1 > n2:
            print('-=-'*15)
            print('O numero {} é maior que o numero {}.'.format(n1, n2))
            print('-=-'*15)
            menu = 0
        else:
            print('-=-'*15)
            print('O numero {} é maior que o numero {}.'.format(n2, n1))
            print('-=-'*15)
            menu = 0
    elif menu == 4:
        n1 = n2 = 0
    elif menu == 5:
        menu = 5
        print('Finalizando...')
    else:
        print('Digito invalido!!!\nFavor digitar novamente!')
    sleep(2)
print('-=-'*5)
print('Fim')
print('-=-'*5)
