from map import init_map
from player import  move_dwon,move_left,move_right,move_up,place_bomb
from score import count_score
from ennemy import count_enemy, move_enemi, near_enemi
from sty import fg, rs, RgbFg, Style
import keyboard
import os
import time
import textwrap
TAILLE_GRILLE = 20
player_1 = "p"
fg.rouge = Style(RgbFg(255,0,0))
ENEMI = fg.rouge + "E" + fg.rs
position_player = {
    "x" : 1,
    "y" : 1
}


number_enemi = 0
score_player = 0
def display_map(map,position,player_1):
    os.system('cls' if os.name == 'nt' else 'clear')
    map[position_enemi_1['x']][position_enemi_1['y']] = ENEMI
    map[position_enemi_2['x']][position_enemi_2['y']] =  ENEMI
    map[position_enemi_3['x']][position_enemi_3['y']] =  ENEMI
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




def center_text(text, width):
    return '\n'.join([line.center(width) for line in textwrap.wrap(text, width)])

text = "Ceci est un exemple de texte centré dans la console."
width = 200  # Largeur de la console

print("--------------------------------MODE DE JEU-----------------------------------------")
print("1- MODE HISTOIRE")
print("2- MODE COMPETITION")
print("3- quitter le jeu")
mode_jeu = input()
if int(mode_jeu) == 1 :
    TAILLE_GRILLE = input("entrer la dimension du map: ")
    map = init_map(int(TAILLE_GRILLE))
    position_enemi_1 = {
       "x" : int(TAILLE_GRILLE) - 2,
       "y" : int(TAILLE_GRILLE) - 2
    }
    position_enemi_2 = {
       "x" : 1,
       "y" : int(TAILLE_GRILLE) - 2
    }
    position_enemi_3 = {
       "x" : int(TAILLE_GRILLE) - 2,
       "y" : 1
    }
    while True:
        time.sleep(0.1)
        map = display_map(map,position_player,player_1)
        if keyboard.is_pressed('q'):
            move_left(map, position_player, player_1)
            score_player = count_score(score_player)
        if keyboard.is_pressed('s'):
            move_dwon(map, position_player,player_1)
            score_player = count_score(score_player)
        if keyboard.is_pressed('d'):
            move_right(map,position_player,player_1)
            score_player = count_score(score_player)
        if keyboard.is_pressed('z'):
            move_up(map,position_player,player_1)
            score_player = count_score(score_player)
        if keyboard.is_pressed('e'):
            place_bomb(map,position_player,ENEMI)
        if keyboard.is_pressed(' '):
            print("mettre le jeu  en pause")
        print(score_player)
        [bool1,x1,y1] = near_enemi(map,position_enemi_1)
        [bool2,x2,y2] = near_enemi(map,position_enemi_2)
        [bool3,x3,y3] = near_enemi(map,position_enemi_3)
        if not(bool1 or bool3 or bool2) :
            move_enemi(map,position_enemi_1,ENEMI)
            move_enemi(map,position_enemi_2,ENEMI)
            move_enemi(map,position_enemi_3,ENEMI)

        if count_enemy(map,ENEMI) == 0 or bool1 or bool2 or bool3:
            print(position_player)
            print(x2,y2)
            break
        print(number_enemi)
        print(center_text(text, width))
        


