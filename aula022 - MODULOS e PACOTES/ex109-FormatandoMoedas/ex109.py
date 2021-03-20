import moeda

valor = float(input('Digite o preço: '))
p = 20
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentando {p}%, temos {moeda.aumentar(valor, p, True)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(valor, 10, True)}')
