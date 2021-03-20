#LISTAS PODEM SER CONECTADAS OU PODEM SER COPIADAS CONFORME EXEMPLO ABAIXO
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
c = a
c[0] = 1
d = a[:] + b[:]
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
print(d)