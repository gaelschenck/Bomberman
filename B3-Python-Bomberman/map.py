import random
from sty import fg, rs, RgbFg, Style
fg.orange = Style(RgbFg(255, 150, 50))
fg.bleu = Style(RgbFg(0,0,255))
fg.rouge = Style(RgbFg(255,0,0))
VIDE = " "
MUR = fg.orange + '|' + fg.rs
MUR_INCASABLE = "|"

def creat_mur_enemi(TAILLE_GRILLE):
    grille = [[VIDE for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
    for _ in range(TAILLE_GRILLE):
        x, y = random.randint(0, TAILLE_GRILLE-1), random.randint(0, TAILLE_GRILLE-1)
        grille[x][y] = MUR
        z, w = random.randint(0, TAILLE_GRILLE-1), random.randint(0, TAILLE_GRILLE-1)
        grille[w][z] = MUR_INCASABLE
    return grille
def creat_bordure(grille, TAILLE_GRILLE):
    for _ in range(TAILLE_GRILLE):
        grille[0][_] = fg.bleu +  "-" + fg.rs   # bordure du haut
        grille[TAILLE_GRILLE - 1][_] = fg.bleu +  "-" + fg.rs   # Bordure du bas
        if _ == 0 :
            grille[_][0] = fg.bleu +  "-" + fg.rs 
        if _ > 0 :
            grille[_][0] = fg.bleu +  "|" + fg.rs  # bordure du gauche
        grille[_][TAILLE_GRILLE - 1] = fg.bleu +  "|" + fg.rs  
        
    return grille

def creat_map(TAILLE_GRILLE):
     grille = creat_mur_enemi(TAILLE_GRILLE)
     grille = creat_bordure(grille, TAILLE_GRILLE)
     return grille
def init_map(TAILLE_GRILLE):
        init_grille = creat_map(TAILLE_GRILLE)
        return init_grille


    

