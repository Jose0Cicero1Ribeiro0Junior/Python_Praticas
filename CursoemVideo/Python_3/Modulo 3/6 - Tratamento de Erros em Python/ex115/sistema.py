from lib.interface import menu, cabeçalho, leiaInt
from time import sleep
from lib.arquivo import lerArquivo, criarArquivo, arquivoExiste, cadastrar

arq = 'Curso_em_video.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        # Opção de listar um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida! \033[m')
    
    sleep(2)


