import random
from Cell import Cell
from GameObject import GameObject
import pygame

class Maze(GameObject):

    def __init__(self, size, cellSize, group):
        super().__init__((0,0), size, group)
        self.group = group
        self.size = size
        self.cellSize = cellSize
        self.board = [[None]*size for i in range(size)]
        self.cells = pygame.sprite.Group()
        self.initBoard(cellSize)
        
    
    def initBoard(self, cellSize):
        pos = (0, 0)
        mid = self.size/2
        midpoints = [(mid, mid), (mid-1, mid), (mid, mid-1), (mid-1, mid-1)]
        for row in range(self.size):
            if pos is None:
                break
            for col in range(self.size):
                cell = Cell(pos, cellSize, self.cells)
                if (row, col) in midpoints:
                    R = random.randint(0,255)
                    G = random.randint(0,255)
                    B = random.randint(0,255)
                    cell.color = (R, G, B)
                    cell.dead = False
                self.board[row][col] = cell
                pos = self.getNextCell(pos)
        self.initCellNeighbors()


    def initCellNeighbors(self):
        for row in range(self.size):
            for col in range(self.size):
                cell = self.board[row][col]
                cell.neighbors = self.getNeighbors(row, col)


    # Get next cell in row
    def getNextCell(self, position):
        width = height = self.size * self.cellSize
        x = position[0]
        y = position[1]
        
        x = (x + self.cellSize) if (x + self.cellSize) < width else 0
        
        # move to new row
        y = y if x > 0 else y + self.cellSize

        # board complete
        y = y if y < height else -1

        return (x, y) if y != -1 else None
    

    def getNeighbors(self, row, col):
        neighbors = [(row-1, col-1), (row-1, col), (row-1, col+1),
                     (row, col-1),                  (row, col+1), 
                     (row+1, col-1),  (row+1, col), (row+1, col+1)]
        n = []
        for cell in neighbors:
            r = cell[0]
            c = cell[1]
            if r >= self.size or c >= self.size:
                continue
            if r < 0 or c < 0:
                continue

            # add neighbor to list
            n += [self.board[cell[0]][cell[1]]]

        return n


    def update(self):
        self.cells.update()


    def __str__(self):
        return f"Board: {self.board}\nBoard size: {len(self.board)}x{len(self.board[0])}"
