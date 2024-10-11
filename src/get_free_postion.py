# Vérifie si une position de la map est libre lors du coup.

def get_free_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
