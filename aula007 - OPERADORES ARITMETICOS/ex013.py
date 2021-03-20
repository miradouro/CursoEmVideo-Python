n1 = float(input('Qual é o preço do produto?\n'))
novo = n1 + (n1 * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a ganhar R${:.2f}!'.format(n1, novo))
