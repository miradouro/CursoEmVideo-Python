'''
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
li = [n1, n2, n3, n4]
es = random.choice(li)
print('O aluno escolhido foi {}'.format(es))
'''

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
li = [n1, n2, n3, n4]
es = choice(li)
print('O aluno escolhido foi {}'.format(es))