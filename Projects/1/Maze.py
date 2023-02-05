import random
from Cell import Cell
from GameObject import GameObject
import pygame
import Notif

class Maze(GameObject):

    def __init__(self, size, player, cellSize, group):
        super().__init__(coordinates=(0,0), size=(size, size), group=group)
        self.size = size
        self.player = player
        self.cellSize = cellSize
        self.group = group
        self.initVariables(size)
        self.initBoard(cellSize)
        Notif.registerMBDEvent(self.updateLists) # REMOVE


    def initVariables(self, size):
        self.cells = pygame.sprite.Group()
        self.board = [[None]*size for i in range(size)]
        self.living = []
        self.dead = []
        

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
                    self.living.append(cell)
                else:
                    self.dead.append(cell)

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


    def update(self, run, play, key=None, delta=None):
        if run:
            self.cells.update()
        if play:
            if key != None and delta != None:
                boardsize = self.size * self.cellSize
                self.player.update(key, delta, boardsize)
                self.checkForCollisions()
        self.updateLists()


    def checkForCollisions(self):
        for cell in self.living:
            collision = pygame.Rect.colliderect(self.player.rect, cell.rect)
            if collision:
                self.updatePlayerPos(cell) 


    def updatePlayerPos(self, cell):
        playerRect = self.player.rect
        cellRect = cell.rect
        horizontal = self.player.direction[0] != 0

        if horizontal:
            right = self.player.direction[0] > 0
            if right:
                if playerRect.right > cellRect.left:
                    playerRect.right = cellRect.left
            elif playerRect.left < cellRect.right:
                playerRect.left = cellRect.right
        else:
            down = self.player.direction[1] > 0
            if down:
                if playerRect.top < cellRect.bottom:
                    playerRect.bottom = cellRect.top
            elif playerRect.bottom > cellRect.top:
                playerRect.top = cellRect.bottom
            
        self.player.rect = playerRect
        self.player.coordinates = playerRect.topleft
    
    
    def updateLists(self, x=None, y=None):
        coordinates = (x, y) if x != None and y != None else None

        for cell in self.cells:
            if coordinates != None:
                if cell.rect.collidepoint(x, y):
                    self.addCell(cell)
                    return
            else:
                self.addCell(cell)


    def addCell(self, cell):
        if cell.dead and (cell in self.living): # cell is dead, but in living list
            self.living.remove(cell)
            if cell not in self.dead:
                self.dead.append(cell)
        elif not cell.dead and (cell in self.dead): # cell is alive, but in dead list
            self.dead.remove(cell)
            if cell not in self.living:
                self.living.append(cell)


    def __str__(self):
        return f"Board size: {len(self.board)}x{len(self.board[0])}\n- Dead: {len(self.dead)}\n- Living: {len(self.living)}"
