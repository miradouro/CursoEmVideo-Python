from time import sleep


def analisador(*num):
    cont = maior = 0
    print('-='*20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa Principal
analisador(2, 9, 4, 5, 7, 1)
analisador(4, 7, 0)
analisador(1, 2)
analisador(6)
analisador()
