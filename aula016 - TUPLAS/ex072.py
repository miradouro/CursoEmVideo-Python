tupla = ('zero', 'hum', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezesete', 'dezoito', 'dezenove', 'vinte')
numero = 21
while numero > 20 or numero < 0:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero > 20:
        print('Digito invalido!!!\nTente Novamente!')
    elif numero < 0:
        print('Digito invalido!!!\nTente Novamente!')
print(f'Você digitou o numero {tupla[numero]}.')
