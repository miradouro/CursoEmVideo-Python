tupla = ('zero', 'hum', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o numero {tupla[numero]}.')
        break
    print('Tente Novamente!')

