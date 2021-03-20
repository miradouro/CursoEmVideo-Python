from random import randint


def sorteando(i):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        a = randint(1, 9)
        print(f'{a}', end=' ')
        i.append(a)
    print('PRONTO!')


def pares(num):
    soma = 0
    for p, v in enumerate(num):
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores de {num}, temos {soma}.')


numeros = []
sorteando(numeros)
pares(numeros)
