from GameObject import GameObject
import pygame
import random

class Cell(GameObject):

    def __init__(self, position, cellSize):
        super().__init__(position)
        self.neighbors = []
        self.dead = True
        self.size = cellSize
        self.color = self.getColor()
        self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], cellSize, cellSize)


    def getColor(self):
        dead = self.getState()
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        return (R, G, B) if not dead else (0, 0, 0)
    

    def getState(self):
        # check state of neighboring cells
        # return random.randint(0,1)
        return self.dead


    def setState(self):
        liveNeighbors = 0
        for cell in self.neighbors:
            if not cell.dead:
                liveNeighbors += 1
        self.dead = liveNeighbors < 1 or liveNeighbors > 4 if not self.dead else liveNeighbors == 3


    def __str__(self):
        return f"Coordinates: {self.coordinates}"
