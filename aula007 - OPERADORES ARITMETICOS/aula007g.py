n1 = float(input('Qual o preço do produto?\n'))
print('Seu valor de R${:.2f} reais com 5% de desconto fica por R${:.2f} reais!'.format(n1, n1-((n1*5)/100)))
