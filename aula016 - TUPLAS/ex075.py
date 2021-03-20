par = 0
nove = 0
tupla = (int(input('Digite um numero: ')),
         int(input('Digite outro numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite o ultimo numero: ')),
         )
print('Os valores digitados foram:', end=' ')
for c in tupla:
    print(f'{c}', end=' ')
    if c % 2 == 0:
        par += 1
    if c == 9:
        nove += 1
print(f'\nO valor 9 apareceu {nove} vezes.')
print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição.')
print(f'Os valores pares digitados foram {par}.')
