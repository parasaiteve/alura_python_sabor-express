import os

def exibir_o_nome_do_programa():
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝

""")
def exibir_opcoes():
    print('1.Cadastrar Restaurante')
    print('2.listar Restaurante')
    print('3.ativar Restaurante')
    print('4.Sair\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear') no sistema MacOS
    print('finalizando o app\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opcao: '))          
# opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1 :
        print('cadastrar restaurante')
    elif opcao_escolhida == 2 :
        print('listar restaurantes')
    elif opcao_escolhida == 3 :
        print('ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_o_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__name__' :
    main()