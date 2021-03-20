distancia = float(input('Qual é a distancia de sua viagem? '))
print('Você está prestes a começar uma viagem de {:.0f}km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
