tabuleiro = [' ' for _ in range(9)]

def imprimir_tabuleiro():
    print(f' {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ')
    print('-----------')
    print(f' {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ')
    print('-----------')
    print(f' {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ')

def verificar_vencedor():
    for i in range(3):
        if tabuleiro[i*3] == tabuleiro[i*3+1] == tabuleiro[i*3+2] != ' ':
            return tabuleiro[i*3]
    
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != ' ':
            return tabuleiro[i]

    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != ' ':
        return tabuleiro[0]
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != ' ':
        return tabuleiro[2]
    if ' ' not in tabuleiro:
        return 'Empate'
    return None

def realizar_jogada(jogador, posicao):
    if tabuleiro[posicao] == ' ':
        tabuleiro[posicao] = jogador
        return True
    else:
        return False

jogador_atual = 'X'
while True:
    imprimir_tabuleiro()
    posicao = int(input(f'Jogador {jogador_atual}, digite a posição (1-9): ')) - 1
    if realizar_jogada(jogador_atual, posicao):
        resultado = verificar_vencedor()
        if resultado:
            imprimir_tabuleiro()
            if resultado == 'Empate':
                print('Empate!')
            else:
                print(f'Jogador {resultado} venceu!')
            break
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    else:
        print('Posição inválida, tente novamente.')