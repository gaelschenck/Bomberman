import threading
import keyboard
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
        timer_2 = threading.Timer(4, after_explo_bomb, args=(map, x, y))
        timer_1.start()
        timer_2.start()
def move(map, position,player):
   
    if keyboard.is_pressed('q'):
        move_left(map, position, player)
    if keyboard.is_pressed('s'):
        move_dwon(map, position,player)
    if keyboard.is_pressed('d'):
        move_right(map,position,player)
    if keyboard.is_pressed('z'):
        move_up(map,position,player)
    if keyboard.is_pressed('e'):
        place_bomb(map,position)