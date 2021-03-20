import moeda

valor = float(input('Digite o preço: '))
p = 20
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando {p}%, temos {moeda.moeda(moeda.aumentar(valor, p))}')
print(f'Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(valor))}')
