'''
num = int(input('Digite um numero: '))
s = 0
for c in range(num - 1, 0, -1):
    if num % c == 0:
        s += c
if s == 1:
    print('{} É um numero primo!!!'.format(num))
else:
    print('{} NÃO é um numero primo!!!'.format(num))
'''
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end='')
print('\n\n\033[mO numero {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('\no numero {} É um numero primo!!!'.format(num))
else:
    print('\nO numero {} NÃO é um numero primo!!!'.format(num))
