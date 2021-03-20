lista = []
par = []
impar = []
while True:
    lista.append(int(input(f'Digite um valor: ')))
    s = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if s == 'S':
        print('-=-'*10)
    elif s == 'N':
        break
print('-=-'*10)
print(f'A lista completa de números é: {lista}.')
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        par.append(lista[i])
        i += 1
    else:
        impar.append(lista[i])
        i += 1
print(f'A lista de pares é {par}.')
print(f'A lista de impares é {impar}.')
