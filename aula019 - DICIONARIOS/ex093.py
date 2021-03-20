jogador = dict()
gols = list()
total = g = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    g = int(input(f'Quantas gols na partida {i+1}? '))
    gols.append(g)
    total += g
jogador['gols'] = gols
jogador['total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(0, partidas):
    print(f'  => Na pasrtida {i+1}, fez {gols[i]} gols.')
print(f'Foi um total de {jogador["total"]} gols!')
