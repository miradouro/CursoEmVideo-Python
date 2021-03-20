from random import randint
maior = 0
menor = 0
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
qtd = len(tupla)
print('Os valores sorteados foram:', end=' ')
for c in range(0, 5):
    print(tupla[c], end=' ')
    if c == 0:
        maior = tupla[c]
        menor = tupla[c]
    if maior < tupla[c]:
        maior = tupla[c]
    if menor > tupla[c]:
        menor = tupla[c]
print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
