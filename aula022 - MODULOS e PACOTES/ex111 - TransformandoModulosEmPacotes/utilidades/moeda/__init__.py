def aumentar(n, taxa=10, formato=False):
    a = n + (n * taxa / 100)
    return a if formato is False else moeda(a)


def diminuir(n, taxa=10, formato=False):
    a = n - (n * taxa / 100)
    return a if formato is False else moeda(a)


def dobro(n, formato=False):
    a = n * 2
    return a if not formato else moeda(a)


def metade(n, formato=False):
    a =  n / 2
    return a if formato is False else moeda(a)


def moeda(n=0, moeda='R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=20, taxar=10):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco,taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')

    print('-'*30)
