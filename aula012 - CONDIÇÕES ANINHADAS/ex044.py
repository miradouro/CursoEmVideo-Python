preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Informe a opção: '))
if opcao == 1:
    print('Sua compra será paga a vista no dinheiro ou cheque.')
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}.'.format(preco, preco - ( preco * 10 / 100)))
elif opcao == 2:
    print('Sua compra será paga à vista no cartão.')
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}.'.format(preco, preco - ( preco * 5 / 100)))
elif opcao == 3:
    print('Sua compra será paga em 2x no cartão (SEM JUROS).')
    print('Sua compra não tem direito a desconto e vai custar R$ {:.2f}.'.format(preco))
elif opcao == 4:
    qtd = int(input('Informe a quantidade de parcelas: '))
    print('Sua compra será paga em {}x de R${:.2f} no cartão.'.format(qtd, (preco+ ( preco * 20 / 100)) / qtd))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}.'.format(preco, preco + ( preco * 20 / 100)))
else:
    print('OPÇÃO INVALILDA DE PAGAMENTO')
    print('Tente Novamente!!!')

