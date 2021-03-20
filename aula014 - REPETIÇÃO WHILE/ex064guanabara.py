n = qtd = soma = 0
n = int(input('Digite um valor ou digite 999 para finalizar: '))
while n != 999:
    qtd += 1
    soma += n
    n = int(input('Digite um valor ou digite 999 para finalizar: '))
print('Você digitou {} numeros e a soma entre eles é {}.'.format(qtd, soma))
