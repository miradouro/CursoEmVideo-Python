from datetime import date
ano = int(input('Ano de nascimento: '))
data = date.today().year
idade = data - ano
print('Escolha qual o seu sexo:')
print('[ 1 ] para MASCULINO')
print('[ 2 ] para FEMININO')
sexo = int(input('Digite sua opção: '))
if sexo == 1:
    print('Quem nasceu em {} tem {} anos em {}!'.format(ano, idade, data))
    if idade < 18:
        print('Ainda faltam {} anos para você se alistar!'.format(18 - idade))
        print('E seu alistamento será em {}!!!'.format(ano + 18))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos!'.format(idade - 18))
        print('E seu alistamento foi em {}!!!'.format(data - (idade - 18)))
    elif idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!!!')
else:
    print('Você é mulher e não precisa se alistar!!!')