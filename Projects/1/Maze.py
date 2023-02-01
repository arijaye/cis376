import random
import Notif
from Cell import Cell

class Maze():
    living = 0
    dead = 0
    complete = False

    def __init__(self, size, cellSize):
        self.size = size
        self.cellSize = cellSize
        self.board = [[0]*size for i in range(size)]
        self.populateBoard(cellSize)
        
        Notif.registerMBDEvent(self.cellClick)

    
    def populateBoard(self, cellSize):
        pos = (0, 0)
        for row in range(self.size):
            if pos is None:
                break
            for col in range(self.size):
                cell = Cell(pos, cellSize)
                self.board[row][col] = cell
                pos = self.getNextCell(pos, cellSize)


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

    def getCell(self, x, y):
        for row in self.board:
            for cell in row:
                if cell.coordinates == (x, y):
                    print(f'row: {self.board.index(row)}')
                    print(f'col: {row.index(cell)}')
                    return cell
        return None
    
    def cellClick(self, event, x, y):
        nearest_x = x - (x % self.cellSize)
        nearest_y = y - (y % self.cellSize)
        cell = self.getCell(nearest_x, nearest_y)
        print(cell)
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        cell.color = (R,G,B)
        # DISPLAY.blit(label, (10,10))
        

    def __str__(self):
        return f"Board: {self.board}\nBoard size: {len(self.board)}x{len(self.board[0])}"
