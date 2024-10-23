from board import Board  # Importer la classe Board de board.py
from player import Player

def main():
    # Initialiser un plateau (hauteur, longueur)
    board = Board(5, 15)
    
    # Afficher le plateau vide
    board.display()
    
    # Créer un joueur
    player = Player(name="Alice", start_row=2, start_col=2)
    
    # Afficher la position initiale du joueur
    print(player)
    
    # Déplacer le joueur
    player.move_up()
    print(player)  # Devrait être à (1, 2)

    player.move_left()
    print(player)  # Devrait être à (1, 1)

    player.move_down(board.rows)
    print(player)  # Devrait être à (2, 1)

    player.move_right(board.cols)
    print(player)  # Devrait être à (2, 2)  
    
    # Afficher le plateau mis à jour
    board.display()

if __name__ == "__main__":
    main()
