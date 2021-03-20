aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['media'] = float(input('Média: '))
print('-='*40)
print(f'- nome é igual a {aluno["nome"]}')
print(f'- média é igual a {aluno["media"]}')
if aluno['media'] <= 7:
    print(f'- situação é igual a RECUPERAÇÃO!')
else:
    print(f'- situação é igual a APROVADO!')

#print(notas)
