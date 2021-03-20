pessoas = homens = mulheres = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    resp = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {pessoas}')
print(f'Ao todo temos {homens} homem cadastrados.' if homens == 1 else f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulher com menos de 20 anos' if mulheres == 1 else f'E temos {mulheres} mulheres com menos de 20 anos')


