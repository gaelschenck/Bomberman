import random
# définition des mouvements
def move_up(map,position,enemi):
        if map[position['x'] - 1][position['y']] == ' ' :
           map[position['x']][position['y']] = ' '
           map[position['x'] - 1][position['y']] = enemi
           position['x'] = position['x']  - 1  

def move_left(map,position,enemi):
    if map[position['x']][position['y'] - 1] == ' ' :
        map[position['x']][position['y']] = ' '
        map[position['x']][position['y'] - 1] = enemi
        position['y'] = position['y']  - 1 

def move_right(map,position,enemi):
    if map[position['x']][position['y'] + 1] == ' ' :
        map[position['x']][position['y']] = ' '
        map[position['x']][position['y'] + 1 ] = enemi
        position['y'] = position['y']  + 1   


def move_dwon(map,position,enemi):
    if map[position['x'] + 1][position['y']] == ' ' :
        map[position['x']][position['y']] = ' '
        map[position['x'] + 1][position['y']] = enemi
        position['x'] = position['x']  + 1

# utilisation des nombres aléatoires pour faire bouger les ennemis        
def move_enemi(map,position,enemi):
    number_random = random.randint(0,3)
    
    if number_random == 0 :
        move_dwon(map,position,enemi)
    elif number_random == 1 :
        move_left(map,position,enemi)
    elif number_random == 2 :
        move_right(map,position,enemi)
    else :
        move_up(map,position,enemi)

# partie perdue si on se fait toucher par l'ennemi
def attraper_par_enemi(map,position):  
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, -1), (-1, 1), (1, 1)]
    for dx, dy in directions:
        nx, ny = position["x"] + dx, position["y"] + dy
        if map[nx][ny] == "p" :
            return True
    else:
        return False