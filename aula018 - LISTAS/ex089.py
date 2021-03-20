from time import sleep
lista = list()
aluno = list()
contador = 0
while True:
    aluno.append(str(input('Nome: ')).strip().title())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    lista.append(aluno[:])
    aluno.clear()
    contador +=1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
print(f'No.  {"Nome":<10} Media')
print('-'*25)
for i in range(0, contador):
    media = float((lista[i][1] + lista[i][2])/2)
    print(f'{i+1:<4} {lista[i][0]:<10} {media:>5.1f}')
print('-'*25)
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao <= len(lista):
        print(f'Notas de {lista[opcao-1][0]} são {lista[opcao-1][1]} e {lista[opcao-1][2]}.')
        print('-' * 40)
    elif opcao == 999:
        print('-' * 25)
        print('Finalizando...')
        sleep(2)
        print('-' * 25)
        print('<<< VOLTE SEMPRE >>>')
        break
