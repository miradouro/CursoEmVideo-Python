classificacao = list()
jogador = dict()
gols = list()
while True:
    verificador = g = 0
    continuar = ' '
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, partidas):
        g = int(input(f'Quantas gols na partida {i+1}? '))
        gols.append(g)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    classificacao.append(jogador.copy())
    gols.clear()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'N':
            verificador = 1
            break
    if verificador == 1:
        break
print('-='*30)
print(f'{"cod":<5}{"cod nome":<15}{"gols":<15}{"total":<10}')
for e, v in enumerate(classificacao):
    print(f'{e + 1:<5}', end='')
    for c in v.values():
        print(f'{str(c):<15}', end='')
    print()
print('-='*30)
mostrar = 0

while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 papa parar): '))
    if mostrar == 999:
        break
    if mostrar > len(classificacao) or mostrar <= 0:
        print(f'ERRO! Não existe jogador com código {mostrar}!')
    else:
        print(f'--> LEVANTAMENTO DO JOGADOR {classificacao[mostrar-1]["nome"]}')
        for i in range(0, len(classificacao[mostrar-1]["gols"])):
            print(f'    No jogo {i+1} fez {classificacao[mostrar-1]["gols"][i]} gols.')
print('-='*30)
print('PROGRAMA ENCERRADO!!!')
'''for e in classificacao:
    print(e)
'''