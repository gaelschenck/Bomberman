import random

def count_enemy(map,enemi):
    compteur = 0
    for ligne in map:
       compteur = compteur +  ligne.count(enemi)
    return compteur

def move_up(map,position,enemi):
        if map[position['x'] - 1][position['y']] == ' ' :
           map[position['x']][position['y']] = ' '
           map[position['x'] - 1][position['y']] = enemi
           position['x'] = position['x']  - 1  

def move_left(map,position,enemi):
    if map[position['x']][position['y'] - 1] == ' ' :
        map[position['x']][position['y']] = ' '
        map[position['x']][position['y'] - 1] = enemi
        position['y'] = position['y']  - 1 

def move_right(map,position,enemi):
    if map[position['x']][position['y'] + 1] == ' ' :
        map[position['x']][position['y']] = ' '
        print( map[position['x']][position['y']])
        map[position['x']][position['y'] + 1 ] = enemi
        position['y'] = position['y']  + 1   


def move_dwon(map,position,enemi):
    if map[position['x'] + 1][position['y']] == ' ' :
        map[position['x']][position['y']] = ' '
        map[position['x'] + 1][position['y']] = enemi
        position['x'] = position['x']  + 1
        print(position['x'])
    

def move_enemi(map,position,enemi):
    number_random = random.randint(0,3)
    if number_random == 0 :
        move_dwon(map,position,enemi)
    elif number_random == 1 :
        move_left(map,position,enemi)
    elif number_random == 2 :
        move_right(map,position,enemi)
    else :
        move_up(map,position,enemi)

def near_enemi(map,position):
    if map[position["x"] - 1][position["y"]] == "p" or map[position["x"] + 1][position["y"]] == "p" or map[position["x"]][position["y"]-1] == "p" or map[position["x"]][position["y"]+1] == "p" or map[position["x"] + 1][position["y"] - 1] == "p" or map[position["x"] - 1][position["y"] -1] == "p" or map[position["x"] -1][position["y"] + 1] == "p" or map[position["x"] +1][position["y"] +1] == "p" :
        x = position["x"]
        y = position["y"]
        return [True, x , y]
    else :
        return [False, 0, 0]




        