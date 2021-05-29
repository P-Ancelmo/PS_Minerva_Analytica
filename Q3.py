def checa_dinheiro(valor, dinheiro, tipo):
    if tipo == 'moeda':
        string = "{} moeda(s) de R${:.2f}".format(valor // dinheiro, dinheiro / 100)
    else:
        string = "{} nota(s) de R${:.2f}".format(valor // dinheiro, dinheiro)
    if valor - dinheiro >= 0:
        print(string)
        valor -= (valor // dinheiro) * dinheiro
    else:
        print(string)
    return valor


# função que verifica se a entrada é válida evitando falhas
def verifica_entrada(entrada):
    if len(entrada) == 2:
        part_int = int(entrada[0])
        part_dec = int(entrada[1])

    elif entrada[0] != '':
        part_int = int(entrada[0])
        part_dec = 0

    else:
        part_int = 0
        part_dec = 0

    return part_int, part_dec


def caixa():
    entrada = input("-> ")
    entrada = entrada.split('.')
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [100, 50, 25, 10, 5, 1]

    part_int, part_dec = verifica_entrada(entrada)

    print("\nNOTAS:")
    for i in notas:
        part_int = checa_dinheiro(part_int, i, "nota")

    # caso sobre 1 real da parte inteira a gente passa pra parte decimal pra poder colocar nas moedas

    part_dec += part_int * 100
    print("\nMOEDAS:")
    for i in moedas:
        part_dec = checa_dinheiro(part_dec, i, "moeda")


if __name__ == '__main__':
    caixa()
