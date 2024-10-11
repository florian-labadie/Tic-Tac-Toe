# Affiche la map actualisé.

def print_board(board):
    i = 0
    for row in board:
        i += 1
        print(" | ".join(row))
        if i < 3:
            print("-" * 9)

# Map

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]] 
    ]
    return [player, player, player] in win_conditions
