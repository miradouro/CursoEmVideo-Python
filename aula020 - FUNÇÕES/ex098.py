from time import sleep
def contagem(a, b, c):
    if a < b:
        if c == 0:
            c = 1
            print('-='*20)
            print(f'Contagem de {a} até {b} de {c} em {c}')
            b +=1
            for i in range(a, b, c):
                sleep(.3)
                print(i, end=' ')
            print('FIM!')
        elif c < 0:
            c = -(c)
            print('-='*20)
            print(f'Contagem de {a} até {b} de {c} em {c}')
            b +=1
            for i in range(a, b, c):
                sleep(.3)
                print(i, end=' ')
            print('FIM!')
        else:
            print('-='*20)
            print(f'Contagem de {a} até {b} de {c} em {c}')
            b +=1
            for i in range(a, b, c):
                sleep(.3)
                print(i, end=' ')
            print('FIM!')
    if a > b:
        if c > 0:
            print('-='*20)
            print(f'Contagem de {a} até {b} de {c} em {c}')
            b -= 1
            c = -(c)
            for i in range(a, b, c):
                sleep(.3)
                print(i, end=' ')
            print('FIM!')
        elif c < 0:
            print('-='*20)
            print(f'Contagem de {a} até {b} de {-c} em {-c}')
            b -= 1
            for i in range(a, b, c):
                sleep(.3)
                print(i, end=' ')
            print('FIM!')
        elif c == 0:
            c = -1
            print('-='*20)
            print(f'Contagem de {a} até {b} de {c} em {c}')
            b -= 1
            for i in range(a, b, c):
                sleep(.3)
                print(i, end=' ')
            print('FIM!')


a = 1
b = 10
c = 1
contagem(a, b, c)
a = 10
b = 0
c = 2
contagem(a, b, c)
print('-=' * 20)
print(f'Agora é a sua vez de personalizar a contagem!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contagem(a, b, c)
