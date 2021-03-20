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
