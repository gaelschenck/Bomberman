import random

class Board:


    # min = 10
    # max = 25

    # i = random.randint(min,max)
    # j = random.randint(min,max)

    # def create_board(i,j):
    #     # Crée une liste de listes, initialisée avec des 0
    #     board = [[0 for _ in range(i)] for _ in range(j)]
    #     return board

    # board = create_board(i,j)
    # print(i,j)

    # for row in board: 
        
    #     print(row)

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def display(self):
        for row in self.grid:
            print(" | ".join([str(cell) if cell is not None else "_" for cell in row]))
            print("-" * (self.cols * 4 - 1))

    def make_move(self, row, col, symbol):
        if self.grid[row][col] is None:
            self.grid[row][col] = symbol
        else:
            raise ValueError("Cell is already taken.")
            #zeef