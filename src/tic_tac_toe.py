from src.board import print_board, check_winner
from src.player import player_move
from src.ai import ai_move
 
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Bienvenue dans le jeu de Tic-Tac-Toe !")

    for turn in range(9):
        print_board(board)
        if turn % 2 == 0:
            print("C'est le tour du joueur X.")
            player_move(board)
            if check_winner(board, "X"):
                print_board(board)
                print("Le joueur X a gagné !")
                return
        else:
            print("C'est le tour de l'IA (O).")
            ai_move(board)
            if check_winner(board, "O"):
                print_board(board)
                print("L'IA (O) a gagné !")
                return

    print_board(board)
    print("Match nul !")
 