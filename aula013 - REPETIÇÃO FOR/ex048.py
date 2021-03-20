'''
m = 0
for c in range(1, 500 + 1):
    if c % 2 == 1:
        if c % 3 == 0:
            #print(c)
            m += c
print(m)
'''
m = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        #print(c, end= ' ')
        m += c
#print(m)
#print(count)
print('A soma dos {} numeros é igual a {}.'.format(count, m))
