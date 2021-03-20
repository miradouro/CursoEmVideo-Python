print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
total = maisQue1k = valor = 0
nomeProduto = ''
while True:
    nome = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: R$ '))
    resp = ' '
    if total == 0:
        nomeProduto = nome
        valor = preco
    total += preco
    if preco > 1000:
        maisQue1k += 1
    if preco < valor:
        nomeProduto = nome
        valor = preco
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R$ {total:.2f}.')
print(f'Temos {maisQue1k} produtos custando mais de R$ 1000,00.')
print(f'O produto mais barato foi "{nomeProduto}" que custa R$ {valor:.2f}')

