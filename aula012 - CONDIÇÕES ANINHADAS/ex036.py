casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salario do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
emprestimo = casa / (anos * 12)
#print('{:.2f}'.format(emprestimo))
print('Para pagar uma casa de R$ {:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação será de R$ {:.2f}'.format(emprestimo))
if emprestimo > salario * 30 / 100:
    print('Empréstimo \033[1;31mNEGADO!\033[m')
else:
    print('Empréstimo \033[1;32mAPROVADO!!!\033[m')
#print(salario * 30 / 100)