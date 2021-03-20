#programa tem erro de logica / melhor opção a do guanabara
exp = str(input('Digite a expressão: '))
pilha = 0
for sim in exp:
    if sim == '(':
        pilha += 1
    elif sim == ')':
        pilha -= 1
if pilha != 0:
    print('Sua expressão está errada!')
else:
    print('Sua expressão está correta!')
