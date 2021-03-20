num = [[], []]
for i in range(0, 7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    if valor % 2 == 1:
        num[1].append(valor)
print('-='*25)
print(f'Os valores pares digitados foram {num[0]}.')
print(f'Os valores impares digitados foram {num[1]}.')
print(num)
