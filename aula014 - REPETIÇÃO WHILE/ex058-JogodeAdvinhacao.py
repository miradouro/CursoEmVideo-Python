from random import randint
from time import sleep
print('\033[1;33m-=-\033[m'*20)
print('\033[1;34mVou pensar em um numero entra 0 e 10. Tente advinhar...\033[m')
print('\033[1;33m-=-\033[m'*20)
computador = 30
jogador = 20
contador = 0
while computador != jogador:
    jogador = int(input('Em qual numero pensei? '))
    computador = randint(0, 10)
    contador +=1
    print('Processando...')
    sleep(1)
    if computador != jogador:
        print('\033[1;31mVocê errou!!!\033[m')
        #print('Pensei no numero {} e você no {}'.format(computador, jogador))
        print('Tente novamente!')
print('\033[1;32mPARABENS!!!\033[m\nVocê acertou!!!\nVocê precisou de {} tentativas para acertar!'.format(contador))
