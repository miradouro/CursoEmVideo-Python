#LISTAS SÃO MUTAVÉIS
num = [2, 5, 9, 1]
print(num)
num[2] = 3#SUBISTITUI UMA POSIÇÃO ESPECIFICADA DA LISTA
print(num)
print(f'1-Esta lista tem {len(num)} elementos.')
num.append(7)#ADICIONA AO FINAL DA LISTA
print(num)
num.sort(reverse=True)#COLOCA EM ORDEM DECRESCENTE
print(num)
print(f'2-Esta lista tem {len(num)} elementos.')
num.insert(2, 0)#INSERE EM UMA POSIÇÃO ESPECIFICA DA LISTA
print(num)
print(f'3-Esta lista tem {len(num)} elementos.')


