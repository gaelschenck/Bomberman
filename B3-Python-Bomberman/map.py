"""
les fonctions qui definissent le comportement de la map et de son affichage
"""
import random
import os

def create_map(dimension, mur_cassable, mur_incassable, bordure_gauche_droite, bordure_bas_haut):
    """
    Create a map with given dimensions and wall types.
    """
    game_map = [[" " for _ in range(dimension)] for _ in range(dimension)]
    # mise en place des murs
    for _ in range(dimension):
        x, y = random.randint(0, dimension-1), random.randint(0, dimension-1)
        game_map[x][y] = mur_cassable
        z, w = random.randint(0, dimension-1), random.randint(0, dimension-1)
        game_map[w][z] = mur_incassable
    for _ in range(dimension):
        game_map[0][_] = bordure_bas_haut   # bordure du haut
        game_map[dimension - 1][_] = bordure_bas_haut   # Bordure du bas
        if _ == 0:
            game_map[_][0] = bordure_bas_haut
        if _ > 0:
            game_map[_][0] = bordure_gauche_droite  # bordure de gauche
        game_map[_][dimension - 1] = bordure_gauche_droite # bordure de droite

    for ligne in game_map:
        print(' '.join(ligne))

    return game_map

def display_map(game_map, position_player, player, position_enemy, enemy):
    """
    Display the game map with player and enemy positions.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    game_map[position_enemy['x']][position_enemy['y']] = enemy
    game_map[position_player['x']][position_player['y']] = player
    for ligne in game_map:
        print(' '.join(ligne))
    return game_map
