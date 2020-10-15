import random


def iniciarAdv():
    print('Seja bem vindo ao meu jogo')
    numero_da_sorte = int(random.randint(1, 100))
    tentativas = int(input('Quantas tentativas você quer?: '))
    contador = 1
    while (contador <= tentativas):
        numero_chutado = int(input('Solte um numero: '))
        if numero_chutado == numero_da_sorte:
            print('Você acertou')
            break
        elif numero_chutado > numero_da_sorte:
            print('Você está indo além!')
        elif numero_chutado < numero_da_sorte:
            print('Você está se segurando muito!')

        print('Essa tentativa foi a: {} '.format(contador))
        contador += 1
    print('Fim do jogo! O numero correto era: ', numero_da_sorte)


if __name__ == "__main__":
    iniciarAdv()
