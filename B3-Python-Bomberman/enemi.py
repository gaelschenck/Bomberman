"""
definition des mouvements enemi et de la partie perdue si on se fait toucher par l'ennemi
"""

import random

def move_up(map, position, enemi):
    """
    deplace l'ennemi vers le haut.
    """
    if map[position['x'] - 1][position['y']] == ' ':
        map[position['x']][position['y']] = ' '
        map[position['x'] - 1][position['y']] = enemi
        position['x'] = position['x'] - 1

def move_left(map, position, enemi):
    """
    deplace l'enemi vers le gauche.
    """
    if map[position['x']][position['y'] - 1] == ' ':
        map[position['x']][position['y']] = ' '
        map[position['x']][position['y'] - 1] = enemi
        position['y'] = position['y'] - 1

def move_right(map, position, enemi):
    """
    deplace l'enemi vers le droite.
    """
    if map[position['x']][position['y'] + 1] == ' ':
        map[position['x']][position['y']] = ' '
        map[position['x']][position['y'] + 1] = enemi
        position['y'] = position['y'] + 1

def move_down(map, position, enemi):
    """
    deplace l'enemi vers le bas.
    """
    if map[position['x'] + 1][position['y']] == ' ':
        map[position['x']][position['y']] = ' '
        map[position['x'] + 1][position['y']] = enemi
        position['x'] = position['x'] + 1

def move_enemy(map, position, enemi):
    """
    deplace l'enemi aleatoirement soit vers le gauche,droite,haut ou bas.
    """
    number_random = random.randint(0, 3)

    if number_random == 0:
        move_down(map, position, enemi)
    elif number_random == 1:
        move_left(map, position, enemi)
    elif number_random == 2:
        move_right(map, position, enemi)
    else:
        move_up(map, position, enemi)

def attraper_par_enemi(map, position):
    """
    retourne True si le joueur se fait toucher par l'ennemi.
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, -1), (-1, 1), (1, 1)]
    for dx, dy in directions:
        nx, ny = position["x"] + dx, position["y"] + dy
        if map[nx][ny] == "p":
            return True
    return False

