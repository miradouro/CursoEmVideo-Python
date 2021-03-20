def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O numero a ser calculado.
    :para show: (opcional) Mostrar ou não a conta.
    :return: Retorna o valor do Fatorial de un número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


'''n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')'''
print(fatorial(5, True))
