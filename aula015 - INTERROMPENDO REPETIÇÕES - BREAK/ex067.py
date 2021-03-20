qtd = soma = 0
while True:
    tab = 1
    n = int(input('Informe um numero para efetuar a tabuada: '))
    print('-'*45)
    if n < 0:
        break
    while tab < 11:
        print(f'{n} x {tab:2} = {n*tab:2}')
        tab += 1
    print('-'*45)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')