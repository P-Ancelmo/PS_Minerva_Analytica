def cavalo():


    pos_cavalo = input("-> ").lower()
    pos_desejada = input("-> ").lower()

    eixo_x = ['a','b','c','d','e','f','g','h']
    if len(pos_cavalo) == 2 and len(pos_desejada) == 2:
        if eixo_x.__contains__(pos_cavalo[0]) and eixo_x.__contains__(pos_desejada[0]):
            diferenca_x = eixo_x.index(pos_cavalo[0]) - eixo_x.index(pos_desejada[0])
            diferenca_y = int(pos_cavalo[1]) - int(pos_desejada[1])
            if (abs(diferenca_x) == 2 and abs(diferenca_y) == 1) or (abs(diferenca_x) == 1 and abs(diferenca_y) == 2):
                print("VÁLIDO")
            else:
                print("INVÁLIDO")
        else:
            print("Alguma das posições inserida não faz parte do tabuleiro")
    else:
        print("Alguma das posições inserida está incompleta")


if __name__ == '__main__':
    cavalo()
