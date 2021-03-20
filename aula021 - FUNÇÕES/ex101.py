def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÂO VOTA.'
    elif 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'


# Programa Principal
idade = int(input('Informe sua idade: '))
print(voto(idade))
