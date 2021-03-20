def area(a, b):
    area = a * b
    print(f'A área de um terreno de {a:.1f}x{b:.1f} é igual a {area:.1f}m².')

print(f'{"CONTROLE DE TERRENOS":^30}')
print('-'*30)
larg = float(input('Largura (mts): '))
comp = float(input('Comprimento (mts): '))

area(larg, comp)
