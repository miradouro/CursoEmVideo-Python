s = 0
count = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        count += 1
        s += n
print('Você informou {} numeros pares e a soma deles foi {}'.format(count, s))
