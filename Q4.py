import re


def ordem_de_grandesa(x):
    cont = 0

    while x // 10 != 0:
        x //= 10
        cont += 1
    return cont


def adiciona(mapa, valor):
    if valor in mapa:
        mapa[valor] += 1
    else:
        mapa[valor] = 1


def le_arquivo():

    try:
        arquivo = open("Texto.txt", 'r')
    except:
        print("Erro ao abrir o arquivo :(")
        exit(0)

    # crio o mapa/dicionario para colocar nele as palavras e seus valores
    mapa = dict([])
    # caracteres diferente de letras comuns na lingua portuguesa
    caracteres = "[!?.:;,()-]"
    cont = 1
    maior_tamanho = 0
    maior_quantidade = 0

    for linha in arquivo:
        linha = linha.split(' ')
        for palavra in linha:
            palavra = palavra.strip()
            # retito da string os caracteres diferente de letras comuns na lingua portuguesa
            palavra = re.sub(caracteres, '', palavra).lower()
            adiciona(mapa, palavra)
            if len(palavra) > maior_tamanho:
                maior_tamanho = len(palavra)
            if mapa[palavra] > maior_quantidade:
                maior_quantidade = mapa[palavra]

    espacos = ordem_de_grandesa(maior_quantidade)

    for i in mapa:

        alinha_com_maior_palavra = maior_tamanho - len(i)
        casas_embaixo_de_casas = ordem_de_grandesa(mapa[i])
        casa_entre = abs(alinha_com_maior_palavra - casas_embaixo_de_casas + espacos)

        espacos_entre = ''

        for j in range(0, casa_entre):
            espacos_entre += ' '
        if cont == 1:
            print('|', end='')

        print("{}:{}{}".format(i, espacos_entre, mapa[i]), end='   ')

        if cont % 4 == 0:
            print('|')
            # print()
            cont = 1
        else:
            cont += 1


if __name__ == '__main__':
    le_arquivo()
