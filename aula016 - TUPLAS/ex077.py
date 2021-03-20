listagem = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for palavra in listagem:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra.upper() in 'A E I O U':
            print(letra.lower(), end=' ')
