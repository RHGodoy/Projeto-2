# Jogo da velha

import random

def desenhaTabuleiro(board):
    # Esta funcao imprime o tabuleiro (board) do jogo

    # "board" é uma lista de 12 strings representando o tabuleiro (ignorando o índice 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def decideLetraDoJogador():
    # Deixa o jogador escolher com qual letra ele gostaria de ser representado no jogo
    # Retorna uma lista com a letra que o jogador escolheu como o primeiro item e a do computador como o segundo
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('Você deseja ser X ou O?')
        letra = input().upper()

    # o primeiro elemento na tupla é a letra do jogador, a segunda é a do computador
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quemVaiPrimeiro():
    # Aleatoriamente escolhe quem que inicia o jogo
    if random.randint(0, 1) == 0:
        return 'computador'
    else:
        return 'jogador'

def jogaNovamente():
    # Esta funcao retorna True se o jogador quiser jogar novamente.
    print('Você deseja jogar novamente? (sim ou não)')
    return input().lower().startswith('s')

def jogada (board, letra, move):
    board[move] = letra

def jogadaVencedora(board, letra):
    # Esta funcao retorna True se o jogador vencer o jogo

    return ((board[7] == letra and board[8] == letra and board[9] == letra) or
    (board[4] == letra and board[5] == letra and board[6] == letra) or
    (board[1] == letra and board[2] == letra and board[3] == letra) or
    (board[7] == letra and board[4] == letra and board[1] == letra) or
    (board[8] == letra and board[5] == letra and board[2] == letra) or
    (board[9] == letra and board[6] == letra and board[3] == letra) or
    (board[7] == letra and board[5] == letra and board[3] == letra) or
    (board[9] == letra and board[5] == letra and board[1] == letra))

def copiaTabuleiro(board):
    # Faz uma copia da lista do tabuleiro e retorna
    copiaBoard = []

    for i in board:
        copiaBoard.append(i)

    return copiaBoard

def esteEspacoTaLivre(board, move):
    # Retorna True se a jogada esta livre no tabuleiro
    return board[move] == ' '

def movimentoJogador(board):
    # Permite ao jogador digitar seu movimento
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not esteEspacoTaLivre(board, int(move)):
        move = input ('Qual sua próxima jogada? - use o teclado numérico: (1-9)')
         
    return int(move)

def escolheJogadaDaLista(board, lista):
    # Retorna um movimento valido da lista passada no tabuleiro
    jogadasPossiveis = []
    for i in lista:
        if esteEspacoTaLivre(board, i):
            jogadasPossiveis.append(i)

    if len(jogadasPossiveis) != 0:
        return random.choice(jogadasPossiveis)
    else:
        return None

def movimentoAI(board, letraAI):
    # Dado um tabuleiro e o simbolo do jogador, a funcao determina onde jogar e retorna o movimento
    if letraAI == 'X':
        letraJogador = 'O'
    else:
        letraJogador = 'X'

    # Aqui estah o teste para o jogo da velha
    # Verifica se é possivel vencer na proxima jogada
    for i in range(1, 10):
        clone = copiaTabuleiro(board)
        if esteEspacoTaLivre(clone, i):
            jogada(clone, letraAI, i)
            if jogadaVencedora(clone, letraAI):
                return i

    # Verifica se o jogador pode vencer na proxima jogada e, o bloqueia
    for i in range(1, 10):
        clone = copiaTabuleiro(board)
        if esteEspacoTaLivre(clone, i):
            jogada(clone, letraJogador, i)
            if jogadaVencedora(clone, letraJogador):
                return i

    # Tenta ocupar algum dos cantos, se eles estiverem livres
    move = escolheJogadaDaLista(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Tenta ocupar o centro, se estiver livre
    if esteEspacoTaLivre(board, 5):
        return 5

    # Ocupa os lados, se nenhuma das anteriores foi possivel
    return escolheJogadaDaLista(board, [2, 4, 6, 8])

def verificaTabuleiroCheio(board):
    # Retorna True se todos os espacos do tabuleiro estiverem ocupados
    for i in range(1, 10):
        if esteEspacoTaLivre(board, i):
            return False
    return True

# -----------**********----------**********----------
print('Bem Vindo ao Jogo da Velha!')

while True:
    # Reinicia o tabuleiro
    tabuleiro = [' '] * 10                  # Volto a usar tabuleiro, para diferenciar as variaveis
    letraJogador, letraAI = decideLetraDoJogador()
    vez = quemVaiPrimeiro()
    print('O ' + vez + ' joga primeiro.')
    jogoEmCurso = True

    while jogoEmCurso:
        if vez == 'jogador':
                                            # Vez do jogador
            desenhaTabuleiro(tabuleiro)
            move = movimentoJogador(tabuleiro)
            jogada(tabuleiro, letraJogador, move)

            if jogadaVencedora(tabuleiro, letraJogador):
                desenhaTabuleiro(tabuleiro)
                print('Parabéns! Você venceu o jogo!')
                jogoEmCurso = False
            else:
                if verificaTabuleiroCheio(tabuleiro):
                    desenhaTabuleiro(tabuleiro)
                    print('O jogo empatou!')
                    break
                else:
                    vez = 'computador'

        else:
                                            # Vez do computador
            move = movimentoAI(tabuleiro, letraAI)
            jogada(tabuleiro, letraAI, move)

            if jogadaVencedora(tabuleiro, letraAI):
                desenhaTabuleiro(tabuleiro)
                print('O computador venceu! Parabéns para ele!.')
                jogoEmCurso = False
            else:
                if verificaTabuleiroCheio(tabuleiro):
                    desenhaTabuleiro(tabuleiro)
                    print('O jogo empatou!')
                    break
                else:
                    vez = 'jogador'

    if not jogaNovamente():
        break
