from random import randint
from time import sleep
lista = list()
jogos = list()
tot = 1
print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-'*30)
quant = int(input('Quantos jogos você quer sortear? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'\n-=-=-= SORTEANDO {quant} JOGOS =-=-=-')
for i in range(0, quant):
    sleep(1)
    print(f'Jogo {i+1}: {jogos[i]}')
print(f'-=-=-=-=-= BOA SORTE =-=-=-=-=-')

