from random import randint
print('-=-'*20)
print('Vamos jogar Paar ou Impar')
print('-=-'*20)
contador = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 5)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            contador += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            contador += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {contador} vez.' if contador == 1 else f'GAME OVER! Você venceu {contador} vezes.')
