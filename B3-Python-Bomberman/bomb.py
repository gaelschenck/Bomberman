"""
fles fonctions qui définissent le comportement des bomb
"""

def explo_bomb(game_map, x, y, bomb):
    """
    
    Fait exploser la bombe aux coordonnées données sur la carte du jeu.
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, -1), (-1, 1), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if game_map[nx][ny] == " ":
            game_map[nx][ny] = bomb

def after_explo_bomb(game_map, x, y, bomb, enemy, destructible_wall):
    """
    Gère les conséquences de l'explosion de la bombe sur la carte du jeu.
    """
    # Remplacement de la bombe par un espace
    if game_map[x][y] == bomb:
        game_map[x][y] = " "
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, -1), (-1, 1), (1, 1)]:
        nx, ny = x + dx, y + dy
        # si c'est un mur ou une bombe, on les supprime
        if game_map[nx][ny] == bomb or game_map[nx][ny] == destructible_wall:
            game_map[nx][ny] = " "
        # si c'est un ennemi, on le "tue"
        elif game_map[nx][ny] == enemy["e1"]:
            enemy["e1"] = " "
