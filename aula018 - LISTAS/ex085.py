lista = []
par = []
impar = []
for i in range(0, 7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor % 2 == 0:
        par.append(valor)
    if valor % 2 == 1:
        impar.append(valor)
print('-='*20)
print(f'Os valores pares digitados foram {par}.')
print(f'Os valores impares digitados foram {impar}.')
