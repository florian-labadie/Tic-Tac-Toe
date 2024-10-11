# Permet de gérer le tour du joueur.
def player_move(board):
    while True:
        try:
            row = int(input("Entrez la ligne (0, 1, 2) : "))
            col = int(input("Entrez la colonne (0, 1, 2) : "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cette case est déjà occupée.")
        except (IndexError, ValueError):
            print("Entrez des coordonnées valides (0, 1, 2).")
            