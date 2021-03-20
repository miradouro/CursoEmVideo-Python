num = [7, 5, 0, 3, 2, 1, 2, 1]
print(num)
print(f'Esta lista tem {len(num)} elementos.')
num.pop()#REMOVE A ULTIMA POSIÇÃO DA LISTA
print(num)
print(f'Esta lista tem {len(num)} elementos.')
num.pop(2)#REMOVE UMA POSIÇÃO ESPECIFICA DA LISTA
print(num)
print(f'Esta lista tem {len(num)} elementos.')
num.remove(2)#REMOVE O PRIMEIRO VALOR ESPECIFICO ENCONTRADO DENTRO DA LISTA
print(num)
print(f'Esta lista tem {len(num)} elementos.')
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
print(f'Esta lista tem {len(num)} elementos.')




