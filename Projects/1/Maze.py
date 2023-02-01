import random
from Cell import Cell
import Notif
from GameObject import GameObject
import pygame 

class Maze(GameObject):
    living = 0
    dead = 0
    complete = False


    def __init__(self, size, cellSize):
        self.size = size
        self.cellSize = cellSize
        self.board = [[0]*size for i in range(size)]
        self.cells = pygame.sprite.Group()
        self.initBoard(cellSize)
        Notif.registerMBDEvent(self.click)
        
    
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
                pos = self.getNextCell(pos, cellSize)
        self.initCellNeighbors()


    def initCellNeighbors(self):
        for row in range(self.size):
            for col in range(self.size):
                cell = self.board[row][col]
                cell.neighbors = self.getNeighbors(row, col)


    # Get next cell in row
    def getNextCell(self, position, cellSize):
        width = height = self.size * cellSize
        x = position[0]
        y = position[1]
        
        x = (x + cellSize) if (x + cellSize) < width else 0
        
        # move to new row
        y = y if x > 0 else y + cellSize

        # board complete
        y = y if y < height else -1

        return (x, y) if y != -1 else None
    

    def getNeighbors(self, row, col):
        neighbors = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
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
            

    def click(self, x, y):
        self.cells.update(x, y)
        return


    def update(self):
        self.cells.update()
        return


    def __str__(self):
        return f"Board: {self.board}\nBoard size: {len(self.board)}x{len(self.board[0])}"
