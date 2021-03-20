matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)
print(f'A soma dos valores pares é {par}.')
for i in range(0, 3):
    soma += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {soma}.')
for i in range(0, 3):
    if matriz[1][i] > maior:
        maior = matriz[1][i]
print(f'O maior valor da segunda linha é {maior}.')
