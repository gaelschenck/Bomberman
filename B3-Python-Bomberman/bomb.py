def explo_bomb(map, x, y,bomb):
    #choix des directions de l'explosion
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, -1), (-1, 1), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        #si la map est vide, on peut poser la bombe
        if map[nx][ny] == " " :
            map[nx][ny] = bomb

def after_explo_bomb(map, x, y,bomb, enemi,mur_cassable):
    # Remplacement de la bombe par un espace
    if map[x][y] == bomb:
        map[x][y] = " "
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, -1), (-1, 1), (1, 1)]:
        nx, ny = x + dx, y + dy
        # si c'est un mur ou une bombe, on les supprime
        if map[nx][ny] == bomb or map[nx][ny] == mur_cassable:
            map[nx][ny] = " "
        # si c'est un ennemi, on le "tue"
        elif map[nx][ny] == enemi["e1"]:
            enemi["e1"] = " "

            
        