tabela = ('Flamengo', 'Internacional', 'Atletico-MG', 'São Paulo',
          'Fluminense', 'Gremio', 'Palmeiras', 'Santos',
          'Athletico -PR', 'Bragantino', 'Ceara SC', 'Corinthians',
          'Atletico-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama',
          'Goiás', 'Coritiba', 'Botafogo')
print('-='*20)
print(f'A classificação atual do brasileirão é: {tabela}')
print('-='*20)
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print('-='*20)
print(f'Os 4 ultimos colocados são: {tabela[-4:]}')
print('-='*20)
print(f'os times em ordem alfabetica são: {sorted(tabela)}')
print('-='*20)
print(f'O Palmeiras esta na {tabela.index("Palmeiras") + 1}ª posição.')
print('-='*20)
#print(len(tabela))
