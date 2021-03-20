km = float(input('Quantos km rodados?'))
dias = int(input('Quantos dias alugados?'))
cd = dias * 60
ck = km * 0.15
print('O total a pagar é de R${:.2f}.'.format(cd + ck))

