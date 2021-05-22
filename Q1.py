def media():
    media = 0
    cont = 0
    temp = input("")

    while temp != 'f':

        if temp <= '9':
            media += int(temp)
            cont += 1
        temp = input("-> ")
    if(cont == 0):
        print("Nenhum número inserido")
    else:
        print("A média é {}".format(media/cont))


if __name__ == '__main__':
    media()
