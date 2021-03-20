tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('-'*20)

nome = str(input('Qual seu nome? ')).title().strip()
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é normal!')
print('Bom dia, {}.'.format(nome))
print('-'*20)
