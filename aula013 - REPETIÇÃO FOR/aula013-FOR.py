#ESTRUTURA DE REPETIÇÃO FOR
'''
for c in range(0, 6):
    print('oi',c)
print('FIM')
'''
#REPETIÇÃO COUNTDOWN
'''
for c in range(7, 0, -1):
    print(c)
print('FIM')
'''
#REPETIÇÃO PULANDO
'''
for c in range(0, 10, 3):
    print(c)
print('FIM')
'''
#REPETIÇÃO COM INTEREÇÃO DE INPUT
'''
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('Fim')
'''
#REPETIÇÃO COM SOMATORIA
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores foi {}'.format(s))
