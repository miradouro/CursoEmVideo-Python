def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite un número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[1;32mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = str(input(msg)).replace(',', '.').strip()
            n = float(n)
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite un número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[1;32mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n


# Programa Principal
n = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n} e o valor real foi {n2}')
