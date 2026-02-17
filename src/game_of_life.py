import random
import time
import os


# =========================
# ADT ARRAY 2D
# =========================
class Array2D:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, i, j):
        return self.data[i][j]

    def set(self, i, j, value):
        self.data[i][j] = value

    def display(self):
        for row in self.data:
            print(" ".join("#" if cell == 1 else "." for cell in row))
        print()

    def copy(self):
        new_array = Array2D(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_array.set(i, j, self.get(i, j))
        return new_array


# =========================
# GAME OF LIFE
# =========================
class GameOfLife:
    def __init__(self, rows, cols):
        self.grid = Array2D(rows, cols)

    def random_initialize(self, probability=0.3):
        for i in range(self.grid.rows):
            for j in range(self.grid.cols):
                if random.random() < probability:
                    self.grid.set(i, j, 1)

    def set_pattern(self, positions):
        for (i, j) in positions:
            if 0 <= i < self.grid.rows and 0 <= j < self.grid.cols:
                self.grid.set(i, j, 1)


    def count_neighbors(self, row, col):
        directions = [-1, 0, 1]
        count = 0

        for i in directions:
            for j in directions:
                if i == 0 and j == 0:
                    continue
                r = row + i
                c = col + j
                if 0 <= r < self.grid.rows and 0 <= c < self.grid.cols:
                    count += self.grid.get(r, c)
        return count

    def next_generation(self):
        new_grid = self.grid.copy()

        for i in range(self.grid.rows):
            for j in range(self.grid.cols):
                neighbors = self.count_neighbors(i, j)
                cell = self.grid.get(i, j)

                if cell == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid.set(i, j, 0)
                else:
                    if neighbors == 3:
                        new_grid.set(i, j, 1)

        self.grid = new_grid

    def run(self, generations=20, delay=0.9):
        for gen in range(generations):
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Generasi {gen + 1}")
            self.grid.display()
            self.next_generation()
            time.sleep(delay)

# =========================
# PROGRAM UTAMA
# =========================
if __name__ == "__main__":
    game = GameOfLife(20, 25)

    
    name_pattern = [
        
        # D
(5,2),(5,3),(5,4),
(6,2),(6,4),
(7,2),(7,4),
(8,2),(8,4),
(9,2),(9,3),(9,4),


        # I
        (5,10),(6,10),(7,10),(8,10),(9,10),

        # K
        (5,14),(6,14),(7,14),(8,14),(9,14),
        (7,15),
        (6,16),(8,16),
        (5,17),(9,17),

        # A
        (7,21),
        (6,20),(6,22),
        (5,19),(5,23),
        (8,20),(8,22),
        (9,19),(9,23)
    ]

    game.set_pattern(name_pattern)
    game.run(generations=30, delay=0.4)

