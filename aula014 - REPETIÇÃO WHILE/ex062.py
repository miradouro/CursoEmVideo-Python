primeiro = 0
razao = 0
decimo = 0
c = 1
opcao = 1
while opcao != 0:
    primeiro = int(input('Informe o primeiro termo: '))
    razao = int(input('Informe a razão: '))
    decimo = primeiro + razao * 10
    while primeiro != decimo:
        print(' {} →'.format(primeiro), end='')
        primeiro = primeiro + razao
    print(' FIM\n')
    print('-=-'*20)
    print('\nDeseja repetir o processo com outros valores?')
    print('[ 1 ] Repetir')
    print('[ 2 ] Sair')
    opcao = int(input('Informe sua opção: '))
    if opcao == 1:
        opção = 1
    elif opcao == 2:
        opcao = 0
    print('-=-'*20)
