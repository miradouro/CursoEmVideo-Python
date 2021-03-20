mult = 1
n = int(input('Informe um numero: '))
print('\033[1;34m{}!\033[m ='.format(n), end=' ')
while n != 1:
    print('{}'.format(n), end='x')
    mult *= n
    n -= 1
print('1 =', mult)
