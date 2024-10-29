from sty import fg, RgbFg, Style
from map import MUR

fg.rouge = Style(RgbFg(255, 150, 50))
fg.rouge = Style(RgbFg(255,0,0))
bomb = fg.orange + "*" + fg.rs
def explo_bomb(map,x,y):
    if map[x-1][y] == " ":
        map[x-1][y] =  bomb
    if map[x + 1][y] == " ":
        map[x + 1][y] = bomb
    if map[x][y-1] == " ":
        map[x][y-1] = bomb
    if map[x][y+1] == " ":
        map[x][y+1] = bomb
    if map[x + 1][y - 1] == " ":
        map[x + 1][y - 1] = bomb
    if map[x - 1][y -1] == " ":
        map[x -1][y-1] = bomb
    if map[x -1][y + 1] == " ":
        map[x -1][y + 1] = bomb
    if map[x+1][y+1] == " ":
        map[x + 1][y + 1] = bomb

def after_explo_bomb(map,x,y):
    if map[x][y] == bomb:
        map[x][y] = " "
    if map[x-1][y] == bomb or map[x-1][y] == MUR:
        map[x-1][y] =  " "
    if map[x + 1][y] == bomb or map[x + 1][y] == MUR:
        map[x + 1][y] = " "
    if  map[x][y-1] == bomb or map[x][y-1] == MUR:
        map[x][y-1] = " "
    if map[x][y+1] == bomb or map[x][y+1] == MUR:
        map[x][y+1] = " "
    if map[x + 1][y - 1] == bomb or map[x + 1][y - 1] == MUR:
        map[x + 1][y - 1] = " "
    if map[x -1][y-1] == bomb or map[x -1][y-1] == MUR:
        map[x -1][y-1] = " "
    if map[x -1][y + 1] == bomb or map[x -1][y + 1] == MUR:
        map[x -1][y + 1] = " "
    if map[x + 1][y + 1] == bomb or map[x + 1][y + 1] == MUR:
        map[x + 1][y + 1] = " "
