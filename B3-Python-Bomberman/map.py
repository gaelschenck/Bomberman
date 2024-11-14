import random
import os

def creat_map(dimension,mur_cassable,mur_incassable,bordure_gauche_droite,bordure_bas_haut):
    map = [[" " for _ in range(dimension)] for _ in range(dimension)]
    # mise en place des murs
    for _ in range(dimension):
        x, y = random.randint(0, dimension-1), random.randint(0, dimension-1)
        map[x][y] = mur_cassable
        z, w = random.randint(0, dimension-1), random.randint(0, dimension-1)
        map[w][z] = mur_incassable
    for _ in range(dimension):
        map[0][_] = bordure_bas_haut   # bordure du haut
        map[dimension - 1][_] = bordure_bas_haut   # Bordure du bas
        if _ == 0 :
            map[_][0] = bordure_bas_haut
        if _ > 0 :
            map[_][0] = bordure_gauche_droite  # bordure de gauche
        map[_][dimension - 1] = bordure_gauche_droite # bordure de droite

    for ligne in map:
        print(' '.join(ligne))
    
    return map
        
# affichage de la map
def display_map(map,position_player,player,position_enemi,enemi):
    os.system('cls' if os.name == 'nt' else 'clear')
    map[position_enemi['x']][position_enemi['y']] = enemi
    map[position_player['x']][position_player['y']] = player
    for ligne in map:
        print(' '.join(ligne))
    return map