pt = int(input('primeiro termo: '))
r = int(input('Razão: '))
d = pt + 10 * r
for c in range(pt, d, r):
    print(c, end=' ')
print('Fim')
