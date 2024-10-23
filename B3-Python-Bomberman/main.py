from board import Board  # Importer la classe Board de board.py

def main():
    # Initialiser un plateau de 3x3 par exemple
    board = Board(5, 15)
    
    # Afficher le plateau vide
    board.display()
    
    # Exemple de mouvement
    board.make_move(1, 1, 'X')  # Joueur 'X' joue en (0, 0)
    
    # Afficher le plateau mis à jour
    board.display()

if __name__ == "__main__":
    main()
#df