from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(.3)
            cont -= p
        print('FIM!')


# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print(f'Agora é a sua vez de personalizar a contagem!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)
