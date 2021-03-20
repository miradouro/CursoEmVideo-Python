s = ''
while 'F' != s != 'M':
    s = str(input('Informe o sexo: [M/F] ')).strip().upper()[0]
    if 'F' != s != 'M':
        print('Digito invalido!!!\nFavor digitar novamente!')
print(s)
