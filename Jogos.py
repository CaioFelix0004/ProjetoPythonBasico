import Forca
import Jogo_ADV
def escolheJogo:
    print('Bem vindo a escolha de jogos!')
    print('Jogos disponiveis: FORCA, ADIVINHAÇÃO')
    print()
    print('Forca: 1, Adivinhação: 2')
    escolha = int(input("Qual jogo você quer?"))

    if escolha == 1:
        print('MANUNTENÇÂo')
    elif escolha == 2:
        Jogo_ADV.iniciarAdv()


if __name__ == "__main__":
    escolheJogo()
