"""
Point d'entrée du jeu Bomberman
"""
import time
from sty import fg, RgbFg, Style
import keyboard
from map import creat_map, display_map
from player import move_dwon, move_left, move_right, move_up, place_bomb
from enemi import move_enemi, attraper_par_enemi
from score import count_score


# initialisation couleur
fg.orange = Style(RgbFg(255, 150, 50))
fg.rouge = Style(RgbFg(255, 0, 0))
fg.bleu = Style(RgbFg(0, 0, 255))


# definition des variables
CASE_VIDE = " "
MUR_CASSABLE = fg.orange + '|' + fg.rs
MUR_INCASSABLE = "|"
SCORE = 0
PLAYER = "p"
ENEMI = {
    "e1": fg.rouge + "E" + fg.rs
}
BOMB = "*"
POSITION_PLAYER = {
    "x": 1,
    "y": 1
}
BORDURE_GAUCHE_DROITE = fg.bleu + "|" + fg.rs
BORDURE_BAS_HAUT = fg.blue + "_" + fg.rs
MAP = []


# menu du jeu
print("--------------------------------MODE DE JEU-----------------------------------------")
print("1- MODE HISTOIRE")
mode_jeu = input()

# ------
if int(mode_jeu) == 1:
    dimension = int(input("entrer la dimension du map: "))
    MAP = creat_map(
        dimension, MUR_CASSABLE, MUR_INCASSABLE, BORDURE_GAUCHE_DROITE, BORDURE_BAS_HAUT
        )
    position_enemi = {
        "x": int(dimension) - 2,
        "y": int(dimension) - 2
    }
    COMPTEUR_BOUCLE = 0
    while True:
        FIN_JEU = attraper_par_enemi(MAP, position_enemi)
        MAP = display_map(MAP, POSITION_PLAYER, PLAYER, position_enemi, ENEMI["e1"])
        print("q: move_left, z: move_top, d: move_right, s: move_dwon, e: placer une bombe: ")
        if keyboard.is_pressed('q'):
            move_left(MAP, POSITION_PLAYER, PLAYER)
            SCORE = count_score(SCORE)
        if keyboard.is_pressed('s'):
            move_dwon(MAP, POSITION_PLAYER, PLAYER)
            SCORE = count_score(SCORE)
        if keyboard.is_pressed('d'):
            move_right(MAP, POSITION_PLAYER, PLAYER)
            SCORE = count_score(SCORE)
        if keyboard.is_pressed('z'):
            move_up(MAP, POSITION_PLAYER, PLAYER)
            SCORE = count_score(SCORE)
        if keyboard.is_pressed('e'):
            place_bomb(MAP, POSITION_PLAYER, BOMB, ENEMI, MUR_CASSABLE)

        if not FIN_JEU:
            if COMPTEUR_BOUCLE % 10 == 0:
                move_enemi(MAP, position_enemi, ENEMI["e1"])
            COMPTEUR_BOUCLE += 1
        if FIN_JEU:
            print("--------------------------------------------------------vous avez perdu------------------------------------------------")
            print(f"---score:{SCORE}")
            break
        if ENEMI["e1"] == " ":
            time.sleep(1)
            print("--------------------------------------------------------vous avez gagné------------------------------------------------")
            print(f"---score:{SCORE}")
            break
        time.sleep(0.1)      