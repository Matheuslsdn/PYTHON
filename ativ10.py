def jogoDaVelha():
    mesa = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
while True:
    print("Jogar o jogo s/n")
    escolha = str(input(""))
    if escolha == "s":
        jogo()
    elif escolha == "n":
        print("Obrigado por jogar!")
        break
    else:
        print("Escolha inválida. Por favor, tente novamente.")

def jogo():