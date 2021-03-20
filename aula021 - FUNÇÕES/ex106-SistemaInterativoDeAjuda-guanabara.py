from time import sleep
c = ('\033[m',      # sem cor
     '\033[1;41m',  # vermelho
     '\033[1;42m',  # verde
     '\033[1;43m',  # amarelo
     '\033[1;44m',  # azul
     '\033[1;45m',  # roxo
     '\033[7m'      # invertido
        );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)

# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)

