'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#print(junto)
qtd = len(junto)
inverso = ''
for c in range(qtd - 1, -1, -1):
    #print(junto[c], end='')
    inverso += junto[c]
print('O inverso da {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo!')
'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso da {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo!')