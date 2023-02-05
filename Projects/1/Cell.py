from GameObject import GameObject
import random
import Notif

DEADCOLOR = (255,255,255)

class Cell(GameObject):

    def __init__(self, position, cellSize, group):
        super().__init__(coordinates=position, size=(cellSize,cellSize), group=group)
        self.setColor(color=DEADCOLOR)
        self.image.fill(self.color)
        Notif.registerMBDEvent(self.click) # REMOVE (use maze)

        self.neighbors = []
        self.dead = True
        self.size = cellSize
    

    def setColor(self, color):
        self.color = color
        self.image.fill(self.color)


    def click(self, x, y):
        if self.rect.collidepoint(x,y):
            newcolor = self.getRandomColor()
            self.setColor(color=(newcolor if self.dead else DEADCOLOR))
            self.dead = not self.dead


    def update(self):
        self.setState()


    def setState(self):
        dead = self.getState() 
        if dead != self.dead:
            self.dead = dead
            
        self.setColor(color=(DEADCOLOR if self.dead else self.getRandomColor()))


    def getState(self):
        liveNeighbors = 0
        for cell in self.neighbors:
            if not cell.dead:
                liveNeighbors += 1

        if self.dead:
            return liveNeighbors != 3
        
        return liveNeighbors < 1 or liveNeighbors > 4


    def getRandomColor(self):
        R = random.randint(0,254)
        G = random.randint(0,254)
        B = random.randint(0,254)
        return (R, G, B)


    def __str__(self):
        return f"location: {self.coordinates}"
