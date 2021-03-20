tupla = (int(input('Digite um numero: ')),
         int(input('Digite outro numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite o ultimo numero: ')),
         )
print(f'Os valores digitados foram: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição.')
else:
    print('O valor 3 não aparece em nenhuma posição.')
print(f'Os valores pares digitados foram', end='')
for n in tupla:
    if n % 2 == 0:
        print(f', {n}', end='')
print('.')
