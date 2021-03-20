print('='*40)
print('{:^40}'.format('BANCO RMB'))
print('='*40)
nota50 = 50
nota20 = 20
nota10 = 10
nota1 = 1
qtd50 = qtd20 = qtd10 = qtd1 = 0
while True:
    valor = int(input('Informe o valor para efetuar o saque: R$ '))
    while valor >= nota50:
        valor -= nota50
        qtd50 += 1
    while valor >= nota20:
        valor -= nota20
        qtd20 += 1
    while valor >= nota10:
        valor -= nota10
        qtd10 += 1
    while valor >= nota1:
        valor -= nota1
        qtd1 += 1
    if valor == 0:
        break
if qtd50 >= 1:
    print(f'Total de {qtd50} cedulas de R$ 50,00')
if qtd20 >= 1:
    print(f'Total de {qtd20} cedulas de R$ 20,00')
if qtd10 >= 1:
    print(f'Total de {qtd10} cedulas de R$ 10,00')
if qtd1 >= 1:
    print(f'Total de {qtd1} cedulas de R$ 1,00')
