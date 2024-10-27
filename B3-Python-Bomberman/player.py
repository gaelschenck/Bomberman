import threading

from bomb import explo_bomb, bomb, after_explo_bomb



def move_dwon(map,position,player):
    if map[position['x'] + 1][position['y']] == ' ' :
        map[position['x']][position['y']] = ' '
        map[position['x'] + 1][position['y']] = player
        position['x'] = position['x']  + 1
        print(position['x'])
    
    
    
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

def place_bomb(map,position):
    if map[position['x']][position['y'] + 1] == ' ' :
        map[position['x']][position['y'] + 1] = bomb
        x = position['x']
        y = position['y'] + 1
        timer_1 = threading.Timer(3, explo_bomb, args=(map, x, y))
        timer_2 = threading.Timer(3, after_explo_bomb, args=(map, x, y))
        timer_1.start()
        timer_2.start()
def move(map, position,player):
    key = input("q: move_left, z: move_top, d: move_right, s: move_dwon, e: placer une bombe: ") 
    if key == 'q':
        move_left(map, position, player)
    if key == 's':
        move_dwon(map, position,player)
    if key == 'd':
        move_right(map,position,player)
    if key == 'z':
        move_up(map,position,player)
    if key == 'e':
        place_bomb(map,position)