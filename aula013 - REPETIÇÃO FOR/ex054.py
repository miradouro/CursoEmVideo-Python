from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    idade = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if ano - idade < 21:
        #print(ano - idade)
        menor += 1
    else:
        #print(ano - idade)
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
