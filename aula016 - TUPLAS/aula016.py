#TUPLAS
#TUPLAS SÃO IMUTAVEIS
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print('-=-'*20)
print(len(lanche))
print('-=-'*20)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-=-'*20)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('-=-'*20)
for pos, food in enumerate(lanche):
    print(f'Eu vou comer {food} na posição {pos}')
print('-=-'*40)
print('Comi pra caramba!')
print('-=-'*40)
print(sorted(lanche))#SORTED COLOCA EM ORDEM ALFABETICA
print(lanche)
