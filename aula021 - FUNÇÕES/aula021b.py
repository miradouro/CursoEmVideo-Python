def par(n=1):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Informe um numero:' ))
if par(num):
    print('Esse numero é par!!!')
else:
    print('Esse numero é impar!!!')
