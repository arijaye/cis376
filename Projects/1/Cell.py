from GameObject import GameObject
import pygame
import random

class Cell(GameObject):
    neighbors = []
    state = len(neighbors) > 1 # False == dead, True == alive

    def __init__(self, position, cellSize):
        super().__init__(position)
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
        return 1
    

   

    def __str__(self):
        return f"Coordinates: {self.coordinates}"
