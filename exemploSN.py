while True:
    s = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if s == 'S':
        print('-=-'*20)
        print(s)
        print('-=-'*20)
    elif s == 'N':
        break
    else:
        print('Digito invalido!!!\nFavor digitar novamente!')
