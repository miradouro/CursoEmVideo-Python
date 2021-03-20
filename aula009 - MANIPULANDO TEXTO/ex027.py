'''
nome = str(input('Digite seu nome completo: ')).strip().title()
separa = nome.split()
ult = nome.rfind(' ')
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(separa[0]))
print('Seu ultimo nome é {}.'.format(nome[ult+1:]))
'''

n = str(input('Digite seu nome completo: ')).strip().title()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1]))
