primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
media = (primeira + segunda) / 2
if media >= 7:
    print('Tirando {:.1f} e {:.1f}, a média é {:.1f}.'.format(primeira, segunda, media))
    print('O aluno esta \033[1;32mAPROVADO!!\033[m')
elif media < 5:
    print('Tirando {:.1f} e {:.1f}, a média é {:.1f}.'.format(primeira, segunda, media))
    print('O aluno esta \033[1;31mREPROVADO!!\033[m')
elif media >=5 and media < 7:
    print('Tirando {:.1f} e {:.1f}, a média é {:.1f}.'.format(primeira, segunda, media))
    print('O aluno esta de \033[1;33mRECUPERAÇÃO!!\033[m')

