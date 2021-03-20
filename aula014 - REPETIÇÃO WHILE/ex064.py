n = 1
qtd = 0
soma = 0
while n != 999:
    n = int(input('Digite um valor ou digite 999 para finalizar: '))
    if n != 999:
        qtd += 1
        soma += n
print('Você digitou {} numeros e a soma entre eles é {}.'.format(qtd, soma))
