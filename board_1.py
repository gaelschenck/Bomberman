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
            self = [[VIDE for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
            x, y = random.randint(0, TAILLE_GRILLE-1), random.randint(0, TAILLE_GRILLE-1)
            self[x][y] = MUR
            w, z = random.randint(0, TAILLE_GRILLE-1), random.randint(0, TAILLE_GRILLE-1)
            self[w][z] = MUR_INCASABLE
    def display_map(self):
           for ligne in self:
                print(' '.join(ligne))
    def jouer(self):
          self.display_map()

map_1 = map()

map_1.jouer()

