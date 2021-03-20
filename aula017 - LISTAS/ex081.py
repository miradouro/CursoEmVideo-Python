lista = []
cont = 0
while True:
    n = int(input(f'Digite um valor: '))
    lista.append(n)
    cont += 1
    s = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if s == 'S':
        print('-=-'*10)
    elif s == 'N':
        break
lista.sort(reverse=True)
print('-=-'*10)
print(f'Você digitou {cont} elementos.')
print(f'os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado!')

