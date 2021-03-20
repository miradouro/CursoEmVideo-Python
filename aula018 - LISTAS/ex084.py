pessoas = list()
dado = list()
maior = list()
menor = list()
qtd = 0
while True:
    dado.append(str(input('Nome: ')).strip().title())
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    qtd += 1
    if len(pessoas) == 1:
        maior.append(dado[:])
        menor.append(dado[:])
    else:
        if dado[1] > maior[0][1]:
            maior[0] = dado[0]
            maior[1] = dado[1]
        elif dado[1] < menor[0][1]:
            menor[0][0] = dado[0]
            menor[0][1] = dado[1]
    dado.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
print(f'Ao todo, você cadastrou {qtd} pessoas.')
print(f'O maior peso foi de {maior[0][1]} kilos. Foi o peso de ', end='')
for p in pessoas:
    if p[1] == maior[0][1]:
        print(f'{p[0]}...', end=' ')
print(f'\nO menor peso foi de {menor[0][1]} kilos. Foi o peso de ', end='')
for p in pessoas:
    if p[1] == menor[0][1]:
        print(f'{p[0]}...', end=' ')
