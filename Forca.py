import random
def jogar():

    bemVindos()

    palavra_secreta = carregar_palavras()

    letras_acertadas = inicializa_letrasAcertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        print(letras_acertadas)
        chute = input('Qual letra?: ').strip().upper()
        if len(chute) > 1:
            print('Apenas uma letra!')
            continue


        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, letras_acertadas, chute)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        print(letras_acertadas)
        acertou = "_" not in letras_acertadas

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


print("Fim do jogo")



palavras = []
def inicializa_letrasAcertadas(palavra):
    lista = ["_" for letra in palavra]
    return lista
def bemVindos():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
def carregar_palavras():
    arquivo = open("palavras.txt", "r")
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
def marca_chute_correto(palavra, letra_secreta, chute):
    index = 0
    for letra in palavra:
        if chute == letra:
           letra_secreta[index] = letra

        index += 1
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if __name__ == "__main__":
    jogar()
