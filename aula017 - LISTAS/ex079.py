numero = []
verificador = 0
while True:
    if verificador == 1:
        break
    valor = int(input(f'Digite um valor: '))
    if valor not in numero:
        numero.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        s = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if s == 'S':
            break
        elif s == 'N':
            verificador = 1
            break
        else:
            print('Digito invalido!!!\nFavor digitar novamente!')
print('-='*30)
print(f'Os numeros informados foram: {sorted(numero)}')
