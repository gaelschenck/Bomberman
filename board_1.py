import random
import os

TAILLE_GRILLE = 10
VIDE = ' '
MUR = '#'
MUR_INCASABLE = "||"
JOUEUR = 'P'
BOMBE = 'B'
EXPLOSION = 'X'

class map:
    def init_grille(self):
            self.grille = [[VIDE for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
            for _ in range(20):
                x, y = random.randint(0, TAILLE_GRILLE-1), random.randint(0, TAILLE_GRILLE-1)
                self.grille[x][y] = MUR
            for _ in range(20):    
                w, z = random.randint(0, TAILLE_GRILLE-1), random.randint(0, TAILLE_GRILLE-1)
                self.grille[w][z] = MUR_INCASABLE
            for ligne in self.grille:
                print(' '.join(ligne))

map_1 = map()

map_1.init_grille()

