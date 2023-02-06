from GameObject import GameObject
import random
import Notif

DEADCOLOR = (255,255,255)

""" Cell class for Maze Generator/Game.

Cells used by Maze for game. Keeps track of
it's own state depending on it's neighbors. Maze
sets the neighbors for a cell upon creating it 
and adding it to the board. Cell sets it's own 
state when clicked through MBDEvents in Notif.

Attributes:
    color: (R,G,B) tuple of current color of the cell
    neighbors: list of cell neighbors (populated by Maze)
    dead: boolean indicating if cell is dead or not
    size: dimensions of cell (square so sizexsize)
    
"""
class Cell(GameObject):
    """Initializes Cell.x
    Args:
        position: Cell's position on display.
        cellSize: size of cell (sizexsize)
        group: Sprite group for cell

    Returns:
        a new Cell object
    """
    def __init__(self, position, cellSize, group):
        super().__init__(coordinates=position, size=(cellSize,cellSize), group=group)
        self.setColor(color=DEADCOLOR)
        self.image.fill(self.color)
        self.neighbors = []
        self.dead = True
        self.size = cellSize
        Notif.registerMBDEvent(self.click) # REMOVE (use maze)

    
    """Set cell's color
    Args:
        color: (R,G,B) tuple of color to set cell to
    """
    def setColor(self, color):
        self.color = color
        self.image.fill(self.color)


    """Handle click
    Changes color of cell depending on 
    current state of cell.
    Args:
        x: x-coordinate of clicked-cell
        y: y-coordinate of clicked-cell
    """
    def click(self, x, y):
        if self.rect.collidepoint(x,y):
            newcolor = self.getRandomColor()
            self.setColor(color=(newcolor if self.dead else DEADCOLOR))
            self.dead = not self.dead


    """Update cell's state
    Sets the state of the cell and it's color
    depending on it's neighbors states.
    """
    def update(self):
        self.setState()


    """Set state of cell
    Set's the state of cell if 
    state has changed. Also set's the color
    of the cell.
    """
    def setState(self):
        dead = self.getState() 
        if dead != self.dead:
            self.dead = dead
            
        self.setColor(color=(DEADCOLOR if self.dead else self.getRandomColor()))


    """Get cell state.
    Checks cells current state depending
    on it's neighbors.
    A dead cell with 3 neighbors is reborn.
    Live cells with < 1 or > 4 neighbors dies.
    Returns:
        boolean representing cell's state;
        True if dead, False if alive
    """
    def getState(self):
        liveNeighbors = 0
        for cell in self.neighbors:
            if not cell.dead:
                liveNeighbors += 1

        if self.dead:
            return liveNeighbors != 3
        
        return liveNeighbors < 1 or liveNeighbors > 4


    """Get random RGB color.
    Gets a random color.
    Returns:
        (R,G,B) tuple of new color
    """
    def getRandomColor(self):
        R = random.randint(0,254)
        G = random.randint(0,254)
        B = random.randint(0,254)
        return (R, G, B)


    def __str__(self):
        return f"location: {self.coordinates}"
