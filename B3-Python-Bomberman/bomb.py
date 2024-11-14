def explo_bomb(map, x, y,bomb):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, -1), (-1, 1), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if map[nx][ny] == " " :
            map[nx][ny] = bomb

def after_explo_bomb(map, x, y,bomb, enemi,mur_cassable):
    # Remplacement de la bombe par un espace
    if map[x][y] == bomb:
        map[x][y] = " "
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, -1), (-1, 1), (1, 1)]:
        nx, ny = x + dx, y + dy
        if map[nx][ny] == bomb or map[nx][ny] == mur_cassable:
            map[nx][ny] = " "
        elif map[nx][ny] == enemi["e1"]:
            enemi["e1"] = " "
            
        