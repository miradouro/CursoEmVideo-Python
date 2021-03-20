from time import sleep


def analisador(*num):
    tam = len(num)
    maior = 0
    print('-='*20)
    print('Analisando os valores passados...')
    cont = 0
    for cont in range(0, tam):
        print(f'{num[cont]}', end=' ')
        sleep(.5)
        if num[cont] > maior:
            maior = num[cont]

    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa Principal
analisador(2, 9, 4, 5, 7, 1)
analisador(4, 7, 0)
analisador(1, 2)
analisador(6)
analisador()
