from Switcher_Questao import Switcher_Questao
from platform import system as sy
from os import system
from time import sleep


def limpa_tela():
    #verificando qual o sistema operacional para usar o comando correto
    if sy() == 'Windows':
        clear = "cls"
    else:
        clear = "clear"
    return system(clear)


def menu():
    print("-----------------------------------------------------------------------------")
    print("Olá, esse é o arquivo de respostas do Processo Seletivo da minerva Analytica.")
    print("Deseja ver questao_escolhida resposta de qual questão ? ")
    print("(Para finalizar digite 0)")
    print("-----------------------------------------------------------------------------")

    switch = Switcher_Questao()

    retorno_switch = -1

    while retorno_switch == -1:
        questao = input("-> ")
        retorno_switch = switch.questoes(questao)
        if questao == '0':
            print("Finalizando o programa...")
            sleep(1)
            exit(0)
        if retorno_switch == -1:
            print("Opção inválida, digite novamente")


if __name__ == '__main__':
    while True:
        limpa_tela()
        menu()
