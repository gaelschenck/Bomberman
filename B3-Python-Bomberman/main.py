from map import init_map
from player import  move
import os
import time
TAILLE_GRILLE = 20
player_1 = "p"
position_player = {
    "x" : 1,
    "y" : 1
}
def display_map(map,position,player_1):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    map[position['x']][position['y']] = player_1
    for ligne in map:
        print(' '.join(ligne))
    print("q: move_left, z: move_top, d: move_right, s: move_dwon, e: placer une bombe: ") 
    return map
#map, position  = display_map_init_p(map)
#qzds
#map, position = move(map, position)
#map, position = display_map(map)
#zsd
map = init_map(TAILLE_GRILLE)
while True:
    map = display_map(map,position_player,player_1)
    move(map,position_player,player_1)
    time.sleep(0.05)


