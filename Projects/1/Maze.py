import random
from Cell import Cell
import Notif

class Maze():
    living = 0
    dead = 0
    complete = False


    def __init__(self, size, cellSize):
        self.size = size
        self.cellSize = cellSize
        self.board = [[0]*size for i in range(size)]
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
                cell = Cell(pos, cellSize)
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


    def getCell(self, x, y):
        for row in self.board:
            for cell in row:
                if cell.rect.collidepoint(x,y):
                    print(cell)
                    print(f'row: {self.board.index(row)}')
                    print(f'col: {row.index(cell)}')
                    return cell
        return None


    def getNeighbors(self, row, col):
        neighbors = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
        n = []
        for cell in neighbors:
            if cell[0] >= self.size or cell[1] >= self.size:
                continue
            if cell[0] < 0 or cell[1] < 0:
                continue

            # add neighbor to list
            n += [self.board[row][col]]

        return n
            

    def setStates(self):
        for row in range(self.size):
            for col in range(self.size):
                cell = self.board[row][col]
                cell.setState()
                return


    def click(self, event, x, y):
        cell = self.getCell(x, y)
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        cell.color = (R, G, B) if cell.dead else (0,0,0)
        cell.dead = not cell.dead
        self.setStates()

    

    def __str__(self):
        return f"Board: {self.board}\nBoard size: {len(self.board)}x{len(self.board[0])}"
