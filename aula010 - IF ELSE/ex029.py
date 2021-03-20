velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO!!! Você excedeu o limite de segurança que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
