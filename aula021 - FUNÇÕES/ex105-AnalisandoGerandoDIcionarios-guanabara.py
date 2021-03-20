def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas de alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return:dicionario com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if r['media'] >= 7:
        r['situacao'] = 'BOA'
    elif r['media'] >= 5:
        r['situacao'] = 'RAZOÁVEL'
    else:
        r['situacao'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 4, 9, 8.5, sit=True)
print(resp)
help(notas)
