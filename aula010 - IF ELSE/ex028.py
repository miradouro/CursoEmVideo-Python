from random import randint
from time import sleep
comp = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. tente advinhar...')
print('-=-' * 20)
jog = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(3)
if jog == comp:
    print('PARABENS! Você conseguiu me vencer!!!')
else:
    print('VOCê PERDEU!!! Eu pensei no numero {} e não no numero {}!!!'.format(comp, jog))
print('-=-' * 20)
