# player.py
class Player:
    def __init__(self, name, start_row=1, start_col=1):
        self.name = name
        self.row = start_row
        self.col = start_col

    def move_up(self):
        if self.row > 0:
            self.row -= 1
        else:
            print(f"{self.name} cannot move up, already at the top.")

    def move_down(self, max_rows):
        if self.row < max_rows - 1:
            self.row += 1
        else:
            print(f"{self.name} cannot move down, already at the bottom.")

    def move_left(self):
        if self.col > 0:
            self.col -= 1
        else:
            print(f"{self.name} cannot move left, already at the edge.")

    def move_right(self, max_cols):
        if self.col < max_cols - 1:
            self.col += 1
        else:
            print(f"{self.name} cannot move right, already at the edge.")

    def get_position(self):
        return self.row, self.col

    def __str__(self):
        return f"Player {self.name} is at position ({self.row}, {self.col})"
