val = list()
maior = menor = 0
for cont in range(0, 5):
    val.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior =  menor = val[cont]
    if maior < val[cont]:
        maior = val[cont]
    if menor > val[cont]:
        menor = val[cont]
print(f'Você digitou os valores: {val}')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for p, v in enumerate(val):
    if maior == v:
        print(p, end='... ')
print(f'\nO menor valor digitado foi o {menor} nas posições ', end='')
for p, v in enumerate(val):
    if menor == v:
        print(f'{p}... ', end='')
