num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
if num1 > num2:
    print('O PRIMEIRO numero é maior!')
elif num2 > num1:
    print('O SEGUNDO numero é maior!')
elif num1 == num2:
    print('Os numeros são iguais!')
else:
    print('CARACTERE INCORRETO!!\nFavor digitar um numero inteiro!!!')
