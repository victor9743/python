# jogo da velha

# criando 9 espaços em branco simulando um tabuleiro
tabuleiro = ['' for _ in range(9)]


def exibir_tabuleiro():
    print()
    print(f'  { tabuleiro[0] } |  { tabuleiro[1] } | { tabuleiro[2] }')
    print('---|---|---')
    print(f'  { tabuleiro[3] } |  { tabuleiro[4] } | { tabuleiro[5] }')
    print('---|---|---')
    print(f'  { tabuleiro[6] } |  { tabuleiro[7] } | { tabuleiro[8] }')
    print()

def jogada(jogador):
    while True:
        try:
            posicao = int(input(f"jogador {jogador}, escolha uma posição entre 1 e 9:")) - 1
            if posicao < 0 or posicao > 8:
                print("posição inválida")
            elif tabuleiro[posicao] != '':
                print("posição já ocupada")
            else:
                tabuleiro[posicao] = jogador
                break
        except ValueError:
            print("Entrada inválida!")

def verificar_vitoria(jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combinacao in combinacoes:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True

def jogar_jogo():
    jogador_atual = 'X'

    for turno in range(9):
        exibir_tabuleiro()
        jogada(jogador_atual)
        if verificar_vitoria(jogador_atual):
            exibir_tabuleiro()
            print(f'jogador {jogador_atual} venceu')
            return 
        jogador_atual = '0' if jogador_atual == 'X' else 'X'

    exibir_tabuleiro()
    print('empate')


jogar_jogo()
