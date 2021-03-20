'''
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
li = [n1, n2, n3, n4]
random.shuffle(li)
print('A ordem de apresentação será: \n', li)
'''
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
li = [n1, n2, n3, n4]
shuffle(li)
print('A ordem de apresentação será: \n', li)
