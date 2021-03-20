def mensagens(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)


def soma(a, b):
    print(a + b)


def contador(*num):
    somatoria = 0
    for valor in num:
        somatoria += valor
    print(somatoria)


mensagens('Olá, Mundo!')
soma(4, 5)
contador(2, 3, 4, 1)

