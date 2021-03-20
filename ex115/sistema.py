from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas',
                     'Cadastrar nova pessoa',
                     'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade) 
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(2)
        break
    else:
        print(linha())
        print('\033[1;33mERRO! Digite uma opção valida!\033[m')

