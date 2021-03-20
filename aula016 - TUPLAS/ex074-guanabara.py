from random import randint
maior = 0
menor = 0
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
qtd = len(tupla)
print('Os valores sorteados foram:', end=' ')
for c in tupla:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')
