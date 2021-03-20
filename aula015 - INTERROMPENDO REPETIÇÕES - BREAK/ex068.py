from random import randint
print('-=-'*20)
print('Vamos jogar Paar ou Impar')
print('-=-'*20)
contador = 0
tipo = ''
while True:
    n = int(input('Diga um valor: '))
    tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 5)
    resultado = ''
    if (n + computador) % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    if resultado == tipo:
        contador += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-=-' * 20)
    else:
        print(f'GAME OVER! Você venceu {contador} vez.')
        break
