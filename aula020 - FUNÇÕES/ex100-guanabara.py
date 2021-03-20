from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        a = randint(1, 9)
        sleep(.4)
        print(f'{a}', end=' ')
        lista.append(a)
    sleep(.4)
    print('PRONTO!')


def somaPar(num):
    soma = 0
    for v in num:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {num}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)
