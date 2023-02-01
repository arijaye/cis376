from GameObject import GameObject
import pygame
import random
import Notif

DEADCOLOR = (0,0,0)

class Cell(GameObject):

    def __init__(self, position, cellSize, group):
        super().__init__(position, cellSize, group)
        self.setColor(color=DEADCOLOR)
        self.image.fill(self.color)
        Notif.registerMBDEvent(self.click)


        self.neighbors = []
        self.dead = True
        self.size = cellSize
    

    def setColor(self, color):
        self.color = color
        self.image.fill(self.color)


    def setState(self):
        liveNeighbors = 0
        for cell in self.neighbors:
            if not cell.dead:
                liveNeighbors += 1
        self.dead = liveNeighbors < 1 or liveNeighbors > 4 if not self.dead else liveNeighbors != 3
        self.setColor(color=(DEADCOLOR if self.dead else self.color))
        

    def getRandomColor(self):
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        return (R, G, B)


    def click(self, x, y):
        if self.rect.collidepoint(x,y):
            newcolor = self.getRandomColor()
            self.setColor(color=(newcolor if self.dead else DEADCOLOR))
            self.dead = not self.dead


    def update(self):
        self.setState()


    def __str__(self):
        return f"Coordinates: {self.coordinates}"
