import random
import os
import time
import keyboard

TAILLE_GRILLE = 10
VIDE = ' '
MUR = '#'
MUR_INCASSABLE = "||"
JOUEUR = 'P'
BOMBE = 'B'
EXPLOSION = 'X'

# Initialisation de la grille avec murs et murs incassables
def init_grille():
    grille = [[VIDE for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
    
    # Placement des murs cassables
    for _ in range(20):
        x, y = random.randint(0, TAILLE_GRILLE-1), random.randint(0, TAILLE_GRILLE-1)
        grille[x][y] = MUR
    
    # Placement des murs incassables
    for _ in range(20):    
        w, z = random.randint(0, TAILLE_GRILLE-1), random.randint(0, TAILLE_GRILLE-1)
        grille[w][z] = MUR_INCASSABLE 
    
    return grille

# Affichage de la grille
def afficher_grille(grille, joueur_x, joueur_y):
    os.system('cls' if os.name == 'nt' else 'clear')  # Nettoyer le terminal
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            if i == joueur_x and j == joueur_y:
                print(JOUEUR, end=' ')
            else:
                print(grille[i][j], end=' ')
        print()

# Fonction pour vérifier si le déplacement est valide
def deplacement_valide(grille, x, y):
    if 0 <= x < TAILLE_GRILLE and 0 <= y < TAILLE_GRILLE:  # Vérifie que le joueur reste dans la grille
        if grille[x][y] == VIDE:  # Le joueur peut se déplacer sur une case vide
            return True
    return False

# Fonction pour déplacer le joueur
def deplacer_joueur(grille, joueur_x, joueur_y):
    while True:
        afficher_grille(grille, joueur_x, joueur_y)
        move = input("Déplacez-vous avec Z (haut), S (bas), Q (gauche), D (droite) : ").lower()
        
        if keyboard.is_pressed('z'):  # Haut
            if deplacement_valide(grille, joueur_x - 1, joueur_y):
                joueur_x -= 1
        elif keyboard.is_pressed('s'):  # Bas
            if deplacement_valide(grille, joueur_x + 1, joueur_y):
                joueur_x += 1
        elif keyboard.is_pressed('q'):  # Gauche
            if deplacement_valide(grille, joueur_x, joueur_y - 1):
                joueur_y -= 1
        elif keyboard.is_pressed('d'):  # Droite
            if deplacement_valide(grille, joueur_x, joueur_y + 1):
                joueur_y += 1
        elif keyboard.is_pressed('x'): #Arrêt
            print("Fin du jeu.")
            break

        time.sleep(0.1)  # Petite pause pour éviter trop de rapidité dans les mouvements

# Programme principal
grille = init_grille()

# Position initiale du joueur
joueur_x, joueur_y = 1, 1

# Déplacement du joueur
deplacer_joueur(grille, joueur_x, joueur_y)
