def media():
    media = 0
    cont = 0

    #loop para checar a entrada (exerce a mesma função de um do While)
    while True:
        temp = input("-> ")
        #verificador de entrada para evitar eventuais falhas
        if temp <= '9' and temp >= '0':
            media += int(temp)
            cont += 1
        elif temp != 'f':
            print("Por favor digite um número ou f")
        if temp == 'f':
            break
    #verifica o tipo (int ou float) da divisao para atender ao pedido de printar o numero sem as casas decimais quando inteiro
    if media % cont == 0:
        media = int(media/cont)
    else:
        media /= cont
    #verifica se
    if(cont == 0):
        print("Nenhum número inserido")
    else:
        print("A média é {}".format(media))


if __name__ == '__main__':
    media()
