numero = int(input('Digite um numero para ver sua tabuada: '))
for c in range (1, 11):
    print('{:2} x {} = {:2}'.format(c, numero, c * numero))
