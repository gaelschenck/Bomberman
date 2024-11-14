from sty import fg, RgbFg, Style
import time
import keyboard
from map import creat_map,display_map
from player import move_dwon,move_left,move_right,move_up,place_bomb
from enemi import move_enemi
from enemi import attraper_par_enemi
from score import count_score

# initialisation couleur
fg.orange = Style(RgbFg(255, 150, 50))
fg.rouge = Style(RgbFg(255,0,0))
fg.bleu = Style(RgbFg(0,0,255))

# definition des variables
case_vide = " "
mur_cassable = fg.orange + '|' + fg.rs
mur_incassable = "|"
score = 0
player = "p"
enemi = {
        "e1" :fg.rouge + "E" + fg.rs
      }
bomb = "*"
position_player = {
    "x" : 1,
    "y" : 1
}
bordure_gauche_droite = fg.bleu +  "|" + fg.rs
bordure_bas_haut = fg.blue + "_" + fg.rs



#menu du jeu
print("--------------------------------MODE DE JEU-----------------------------------------")
print("1- MODE HISTOIRE")
mode_jeu = input()
#------
if int(mode_jeu) == 1 : 
   dimension  = int(input("entrer la dimension du map: "))
   map = creat_map(dimension,mur_cassable,mur_incassable,bordure_gauche_droite,bordure_bas_haut) 
   position_enemi = {
    "x" : int(dimension) - 2,
    "y" : int(dimension) - 2
    }  
   compteur_boucle = 0
   while True:
       
        bool = attraper_par_enemi(map,position_enemi)
        map = display_map(map,position_player,player,position_enemi,enemi["e1"])
        print("q: move_left, z: move_top, d: move_right, s: move_dwon, e: placer une bombe: ") 
        if keyboard.is_pressed('q'):
            move_left(map, position_player, player)
            score = count_score(score)
        if keyboard.is_pressed('s'):
            move_dwon(map, position_player,player)
            score = count_score(score)
        if keyboard.is_pressed('d'):
            move_right(map,position_player,player)
            score = count_score(score)
        if keyboard.is_pressed('z'):
            move_up(map,position_player,player)
            score = count_score(score)
        if keyboard.is_pressed('e'):
             place_bomb(map,position_player,bomb,enemi,mur_cassable)
             
        if not(bool):
            if compteur_boucle % 10 == 0:
                move_enemi(map,position_enemi,enemi["e1"])   
            compteur_boucle += 1    
        if bool:
            print("--------------------------------------------------------vous avez perdu------------------------------------------------")
            print(f"---score:{score}")
            break
        if enemi["e1"] == " ":
            print("--------------------------------------------------------vous avez gagné------------------------------------------------")
            print(f"---score:{score}")
            break
        time.sleep(0.1)

      

