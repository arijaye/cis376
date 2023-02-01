from GameObject import GameObject
import pygame
import random

DEADCOLOR = (0,0,0)

class Cell(GameObject):

    def __init__(self, position, cellSize, group):
        super().__init__(position, group)
        self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], cellSize, cellSize)
        self.image = pygame.Surface([cellSize, cellSize])
        self.setColor(color=DEADCOLOR)
        self.image.fill(self.color)

        self.neighbors = []
        self.dead = True
        self.size = cellSize
    

    def setColor(self, color):
        self.color = color
        self.image.fill(self.color)


    def getState(self):
        # check state of neighboring cells
        return self.dead


    def setState(self):
        liveNeighbors = 0
        for cell in self.neighbors:
            if not cell.dead:
                liveNeighbors += 1
        self.dead = liveNeighbors < 1 or liveNeighbors > 4 if not self.dead else liveNeighbors != 3
        self.setColor(color=(DEADCOLOR if self.dead else self.color))
        

    def neighboringCell(self, x, y):
        for cell in self.neighbors:
            if cell.rect.collidepoint(x, y):
                return True


    def getRandomColor(self):
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        return (R, G, B)


    def click(self):
        newcolor = self.getRandomColor()
        self.setColor(color=(newcolor if self.dead else DEADCOLOR))
        self.dead = not self.dead


    def update(self, x=None, y=None):
        if x != None and y != None:
            if not self.rect.collidepoint(x,y):
                if self.neighboringCell(x,y):
                    print(f'IM THE NEIGHBOR: {self}')
                return
            self.click()
        self.setState()


    def __str__(self):
        return f"Coordinates: {self.coordinates}"
