from random import randint
from time import sleep
comp = randint(0, 2)
pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Informe sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 20)
#TRATANDO DIGITOS INVALIDOS
if jog >=3:
    print('Opção errada!\nTente novamente!')
    comp = 3
#----------------------------------------------------------
#ASSOCIANDO NUMERO COM PALAVRA
if comp == 0:
    print('Computador jogou {}'.format(pedra))
elif comp == 1:
    print('Computador jogou {}'.format(papel))
elif comp == 2:
    print('Computador jogou {}'.format(tesoura))
if jog == 0:
    print('Jogador jogou {}'.format(pedra))
elif jog == 1:
    print('Jogador jogou {}'.format(papel))
elif jog == 2:
    print('Jogador jogou {}'.format(tesoura))
#----------------------------------------------------------
print('-=-' * 20)
#MECANICA DO JOGO
if jog == 0 and comp == 0:
    print('EMPATE')
elif jog == 0 and comp == 1:
    print('COMPUTADOR VENCE')
elif jog == 0 and comp == 2:
    print('JOGADOR VENCE')
elif jog == 1 and comp == 0:
    print('JOGADOR VENCE')
elif jog == 1 and comp == 1:
    print('EMPATE')
elif jog == 1 and comp == 2:
    print('COMPUTADOR VENCE')
elif jog == 2 and comp == 0:
    print('COMPUTADOR VENCE')
elif jog == 2 and comp == 1:
    print('JOGADOR VENCE')
elif jog == 2 and comp == 2:
    print('EMPATE')