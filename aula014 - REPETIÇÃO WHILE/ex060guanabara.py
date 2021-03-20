'''from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
r = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c),end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    r *= c
    c -= 1
print('{}'.format(r))
