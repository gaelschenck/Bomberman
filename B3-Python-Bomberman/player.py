"""
les fonctions qui definissent le comportement du joueur
"""

import threading
from bomb import explo_bomb, after_explo_bomb

# mouvement du personnage
def move_down(game_map, position, player):
    """
    Move the player down on the game map.
    """
    if game_map[position['x'] + 1][position['y']] == ' ':
        game_map[position['x']][position['y']] = ' '
        game_map[position['x'] + 1][position['y']] = player
        position['x'] = position['x'] - 1

def move_up(game_map, position, player):
    """
    Move the player up on the game map.
    """
    if game_map[position['x'] - 1][position['y']] == ' ':
        game_map[position['x']][position['y']] = ' '
        game_map[position['x'] - 1][position['y']] = player
        position['x'] = position['x'] - 1

def move_right(game_map, position, player):
    """
    Move the player right on the game map.
    """
    if game_map[position['x']][position['y'] + 1] == ' ':
        game_map[position['x']][position['y']] = ' '
        game_map[position['x']][position['y'] + 1] = player
        position['y'] = position['y'] + 1

def move_left(game_map, position, player):
    """
    Move the player left on the game map.
    """
    if game_map[position['x']][position['y'] - 1] == ' ':
        game_map[position['x']][position['y']] = ' '
        game_map[position['x']][position['y'] - 1] = player
        position['y'] = position['y'] - 1

# placement des bombes
def place_bomb(game_map, position, bomb, enemy, destructible_wall):
    """
    Place a bomb on the game map.
    """
    xb = position['x']
    yb = position['y'] + 1
    if game_map[position['x']][position['y'] + 1] == ' ':
        game_map[position['x']][position['y'] + 1] = bomb
        timer_1 = threading.Timer(3, explo_bomb, args=(game_map, xb, yb, bomb))
        timer_2 = threading.Timer(
            5, after_explo_bomb, args=(game_map, xb, yb, bomb, enemy, destructible_wall)
            )
        timer_1.start()
        timer_2.start()
