peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (mts) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal!')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está na faixa de SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está na faixa de OBESIDADE!')
else:
    print('CUIDADO! Você está na faixa de OBESIDADE MORBIDA')
