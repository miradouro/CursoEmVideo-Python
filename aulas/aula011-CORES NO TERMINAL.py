#AULA SOBRE CODIGO DE CORES ANSI

nome = 'Guanabara'
cores = {'limpa': '\033[m',
         'azul': '\033[33m',
         'amarelo': '\033[7;30m'}
print('Olá! Prazer em te conhecer, {}{}{}!'.format(cores['azul'], nome, cores['limpa']))
print("\033[1;31mEsta\033[m \033[1;32mé\033[m \033[1;34moutra\033[m \033[1;36mforma\033[m \033[1;35mde\033[m \033[1;37mcolocar\033[m \033[1;33mcores\033[m!!!")
print('{}Outra forma pra fechar a aula!!!{}'.format('\033[1;34m', '\033[m'))
