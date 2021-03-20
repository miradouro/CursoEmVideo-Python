import moeda

valor = float(input('Digite o preço: '))
p = 20
print(f'A metade de R${valor:.2f} é R${moeda.metade(valor):.2f}')
print(f'O dobro de R${valor:.2f} é R${moeda.dobro(valor):.2f}')
print(f'Aumentando {p}%, temos R${moeda.aumentar(valor, p):.2f}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(valor):.2f}')
