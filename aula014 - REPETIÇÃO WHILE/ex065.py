menu = 0
cont = 0
media = 0
menor = 0
maior = 0
while menu != 2:
    n1 = int(input('Informe um numero: '))
    if menu == 0:
        menor = n1
        maior = n1
        media += n1
        cont += 1
        print('[ 1 ] deseja informar mais um numero?')
        print('[ 2 ] deseja finalilzar o programa?')
        menu = int(input('Informe a opção desejada: '))
        print('-='*15)
    else:
        if menor > n1:
            menor = n1
        elif maior < n1:
            maior = n1
        media += n1
        cont += 1
        print('[ 1 ] deseja informar mais um numero?')
        print('[ 2 ] deseja finalilzar o programa?')
        menu = int(input('Informe a opção desejada: '))
print('O maior numero foi o {}.'.format(maior))
print('O menor numero foi o {}.'.format(menor))
print('A quantidade de numeros digitados foi de {} numeros.'.format(cont))
print('A media entre eles foi {:.1f}.'.format(media/cont))
