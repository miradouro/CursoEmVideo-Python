qtd = soma = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    qtd += 1
    soma += n
print(f'A soma dos {qtd} valores foi {soma}.')
