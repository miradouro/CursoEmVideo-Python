def aumentar(n, taxa=10):
    a = n + (n * taxa / 100)
    return a


def diminuir(n, taxa=10):
    a = n - (n * taxa / 100)
    return a


def dobro(n):
    return float(n * 2)


def metade(n):
    return n / 2


def moeda(n=0, moeda='R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')
