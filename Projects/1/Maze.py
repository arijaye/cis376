import random
from Cell import Cell
from GameObject import GameObject
import pygame
import Notif

""" Maze class for Maze Generator/Game.
Maze used by Engine for game. Keeps track of
cells and their neighbors. Makes updates to the
cells and checks for collisions with player.

Attributes:
    size: dimensions of board
    player: player of game
    cellSize: dimensions of cells
    group: Sprite group for Maze 
    cells: Sprite group of cells in maze
    board: list of cells in board
    living: list of living cells
    dead: list of dead cells
"""
class Maze(GameObject):
    """Initializes Maze.x
    Args:
        size: Maze's dimensions
        player: player of game
        cellSize: dimensions of cells
        group: Sprite group for Maze 

    Returns:
        a new Maze object
    """
    def __init__(self, size, player, cellSize, group):
        super().__init__(coordinates=(0,0), size=(size, size), group=group)
        self.size = size
        self.player = player
        self.cellSize = cellSize
        self.group = group
        self.initVariables(size)
        self.initBoard(cellSize)
        Notif.registerMBDEvent(self.updateLists)


    """Initializes Maze variables.x
    Args:
        size: Maze's dimensions
    """
    def initVariables(self, size):
        self.cells = pygame.sprite.Group()
        self.board = [[None]*size for i in range(size)]
        self.living = []
        self.dead = []
        

    """Initializes board.x
    Middle 4 squares are given random colors
    to start. Initializes neighbor lists for 
    cells.
    Args:
        cellSize: cell dimensions
    """
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

    """Initializes cell neighbors.x
    Initializes neighbor lists for 
    cells.
    """
    def initCellNeighbors(self):
        for row in range(self.size):
            for col in range(self.size):
                cell = self.board[row][col]
                cell.neighbors = self.getNeighbors(row, col)


    """Get next cell in row.x
    Returns next cell in row based on 
    coordinates. Wraps to next row if reaches
    the end.
    Args:
        position: (x,y) tuple of coordinates for current
        cell
    Returns:
        (x,y) tuple of coordinates for next cell in 
        row or None if end of board is reached
    """
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
    

    """Get cell neighbors.x
    Returns list of all cell neighbors.
    Args:
        row: row of current cell
        col: column of current cell
    Returns:
        list of cell at (row, col)'s neighbors
    """
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


    """Update maze objects.x
    Update maze depending on game setting.
    If updating, update cells. If playing, 
    update player.
    Args:
        run: boolean determining updates to maze
        play: boolean determining updates to player
        key: default to none; key pressed if player
        needs to be updated
        delta: default to none; delta from game loop 
        if player needs to be updated
    """
    def update(self, run, play, key=None, delta=None):
        if run:
            self.cells.update()
        if play:
            if key != None and delta != None:
                boardsize = self.size * self.cellSize
                self.player.update(key, delta, boardsize)
                self.checkForCollisions()
        self.updateLists()


    """Check for player-cell collisions.x
    Check for collisions with cells.
    If there is one, update player pos.
    """
    def checkForCollisions(self):
        for cell in self.living:
            collision = pygame.Rect.colliderect(self.player.rect, cell.rect)
            if collision:
                self.updatePlayerPos(cell) 

    """Update player pos.
    Update player pos depending
    on colliding cell.
    Args:
        cell: colliding cell
    """
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
    
    
    """Update living/dead lists.
    Update lists of living and dead cells.
    Args:
        x: default to none; x coordinate
        of cell to add or remove
        y: default to none; y coordinate
        of cell to add or remove
    """
    def updateLists(self, x=None, y=None):
        coordinates = (x, y) if x != None and y != None else None

        for cell in self.cells:
            if coordinates != None:
                if cell.rect.collidepoint(x, y):
                    self.addCell(cell)
                    return
            else:
                self.addCell(cell)


    """Add cell to living/dead lists.
    Add cell to lists of living and dead cells.
    Args:
        cell: cell to add/remove
    """
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
