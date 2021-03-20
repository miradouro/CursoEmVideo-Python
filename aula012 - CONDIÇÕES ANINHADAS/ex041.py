from datetime import date
nasc = int(input('Ano de nascimento: '))
data = date.today().year
idade = data - nasc
print('O atleta tem {}.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <=14:
    print('Classificação: INFANTIL')
elif idade <=19:
    print('Classificação: JUNIOR')
elif idade <=25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
