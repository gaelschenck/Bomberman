from bomb import  explo_bomb,after_explo_bomb
import threading
def move_dwon(map,position,player):
    if map[position['x'] + 1][position['y']] == ' ' :
        map[position['x']][position['y']] = ' '
        map[position['x'] + 1][position['y']] = player
        position['x'] = position['x']  + 1
     
    
    
    
def move_up(map,position,player):
    if map[position['x'] - 1][position['y']] == ' ' :
        map[position['x']][position['y']] = ' '
        map[position['x'] - 1][position['y']] = player
        position['x'] = position['x']  - 1   

def move_right(map,position,player):
    if map[position['x']][position['y'] + 1] == ' ' :
        map[position['x']][position['y']] = ' '
        print( map[position['x']][position['y']])
        map[position['x']][position['y'] + 1 ] = player
        position['y'] = position['y']  + 1   

def move_left(map,position,player):
    if map[position['x']][position['y'] - 1] == ' ' :
        map[position['x']][position['y']] = ' '
        map[position['x']][position['y'] - 1] = player
        position['y'] = position['y']  - 1 

def place_bomb(map,position,bomb,enemi,mur_cassable):
    xb = position['x']
    yb = position['y'] + 1
    if map[position['x']][position['y'] + 1] == ' ' :
        map[position['x']][position['y'] + 1] = bomb
        timer_1 = threading.Timer(3, explo_bomb, args=(map, xb, yb,bomb))
        timer_2 = threading.Timer(5, after_explo_bomb, args=(map, xb, yb,bomb,enemi,mur_cassable))
        timer_1.start()
        timer_2.start()
    
 