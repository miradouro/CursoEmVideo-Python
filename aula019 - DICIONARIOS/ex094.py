lista = list()
dicionario = dict()
verificador = contador = media = somaIdade = 0
while True:
    #verificador = 0
    sexo = ' '
    continuar = ' '
    dicionario['nome'] = str(input('Nome: ')).strip().title()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('ERRO! Responda apenas M ou F.')
    dicionario['sexo'] = sexo
    idade = int(input('Idade: '))
    dicionario['idade'] = idade
    lista.append(dicionario.copy())
    contador += 1
    somaIdade += idade
    while continuar not in 'SN':
        continuar = str(input(f'Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar not in 'SN':
            print('ERRO! Responda apenas S ou N.')
        if continuar == 'N':
            verificador = 1
            break
    if verificador == 1:
        break
print('-='*40)
print(f'A) Ao todo temos {contador} pessoas cadastradas.')
media = somaIdade / contador
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for e in lista:
    for k, v in e.items():
        if v == 'F':
            #print(f'{e["nome"]} => {k} = {v}')
             print(f'[{e["nome"]}]', end=' ')
media = int(media)
print(f'\nD) Lista das pessoas que estão acima da média:')
for e in lista:
    if e['idade'] > media:
            print(f'    nome = {e["nome"]}; sexo = {e["sexo"]}; idade = {e["idade"]} ')
print('<< ENCERRADO >>')
