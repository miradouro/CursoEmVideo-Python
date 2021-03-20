media = 0
menos = 0
maiorIdade = 0
nome1 = ''
for c in range(1, 5):
    nome = str(input('Informe o nome: ')).strip().title()
    idade = float(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
    media += idade
    if sexo == 'F' and idade < 20:
        menos += 1
    elif sexo == 'M' and idade > maiorIdade:
        nome1 = nome
        maiorIdade = idade
print('A média de idade do grupo é de {:.1f} anos'.format(media/4))
print('O homem mais velho tem {:.0f} anos e se chama {}.'.format(maiorIdade, nome1))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menos))
