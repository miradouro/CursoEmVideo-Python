from datetime import date
today = date.today()
#print(today.year)
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = today.year - nasc
dados['ctps'] = int(input('carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + 35

print('-='*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}.')
