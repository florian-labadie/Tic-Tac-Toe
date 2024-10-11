from src.board import check_winner
from src.get_free_postion import get_free_positions

# Algorythme Minimax pour l'IA.

def minimax(board, depth, is_maximizing):
    # Vérifie les conditions de victoire ou de match nul et retourne le score correspondant.
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif not get_free_positions(board):
        return 0

    # Si c'est au tour de l'ia ("O"), on cherche à maximiser le score.
    if is_maximizing:
        best_score = -float('inf')
        for (i, j) in get_free_positions(board):
            board[i][j] = "O"  # Simule le coup pour "O".
            score = minimax(board, depth + 1, False)  # Appelle récursivement minimax en inversant le joueur.
            board[i][j] = " "  # Annule le coup.
            best_score = max(score, best_score)  # Met à jour le meilleur score si nécessaire.
        return best_score
    
    # Si c'est au tour du joueur ("X"), on cherche à minimiser le score.
    else:
        best_score = float('inf')
        for (i, j) in get_free_positions(board):
            board[i][j] = "X"  # Simule le coup pour "X".
            score = minimax(board, depth + 1, True)  # Appelle récursivement minimax en inversant le joueur.
            board[i][j] = " "  # Annule le coup.
            best_score = min(score, best_score)  # Met à jour le meilleur score si nécessaire.
        return best_score

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    
    # Parcourt toutes les positions libres pour trouver le meilleur coup.
    for (i, j) in get_free_positions(board):
        board[i][j] = "O"  # Simule le coup pour "O".
        score = minimax(board, 0, False)  # Évalue le coup avec minimax.
        board[i][j] = " "  # Annule le coup.
        
        # Met à jour le meilleur coup si le score obtenu est meilleur.
        if score > best_score:
            best_score = score
            best_move = (i, j)
    
    # Joue le meilleur coup trouvé sur le plateau.
    board[best_move[0]][best_move[1]] = "O"
