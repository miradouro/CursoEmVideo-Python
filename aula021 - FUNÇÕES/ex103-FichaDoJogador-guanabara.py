def jogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do jogador: ')).strip().title()
g = str(input('Numero de gols: '))
if g.isnumeric():#comando "isnumeric" funciona apenas em strings
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jogador(gols=g)
else:
    jogador(n, g)
