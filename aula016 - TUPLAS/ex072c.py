tupla = ('zero', 'hum', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezesete', 'dezoito', 'dezenove', 'vinte')
v = 0
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o numero {tupla[numero]}.')
        while True:
            tente = str(input('Deseja consultar novamente? [S/N]')).strip().upper()[0]
            if tente == 'N':
                v = 1
                break
            elif tente == 'S':
                break
    else:
        print('Tente Novamente!')
    if v == 1:
        break

