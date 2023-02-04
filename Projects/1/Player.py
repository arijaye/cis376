from GameObject import GameObject
import pygame
import os

class Player(GameObject):
     
    imagePath = os.path.join('Projects', '1', 'images', 'sprite.png')

    def __init__(self, position):
        self.scaleAndSetImage()
        self.direction = (0,0)
        super().__init__(coordinates=position, size=(self.rect.width,self.rect.height))


    def scaleAndSetImage(self):
        self.image = pygame.image.load(self.imagePath).convert_alpha()

        rect = self.image.get_rect()
        (scaledX, scaledY) = (rect.width/30, rect.height/30)

        self.image = pygame.transform.scale(self.image, (scaledX, scaledY))
        self.rect = self.image.get_rect()


    def update(self, key, delta, boardsize):
        x = self.coordinates[0]
        y = self.coordinates[1]
        pixels = 100 * delta

        match key:
            case pygame.K_UP:
                self.direction = (0, -1)
                y -= pixels

            case pygame.K_DOWN:
                self.direction = (0, 1)
                y += pixels

            case pygame.K_LEFT:
                self.direction = (-1, 0)
                x -= pixels

            case pygame.K_RIGHT:
                self.direction = (1, 0)
                x += pixels
        
        self.rect = pygame.Rect(x, y, self.rect.width, self.rect.height)
        self.checkForCollisions(boardsize)
        self.coordinates = (self.rect.x, self.rect.y)


    def checkForCollisions(self, boardsize):
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.right = boardsize if self.rect.right > boardsize else self.rect.right
        self.rect.bottom = boardsize if self.rect.bottom > boardsize else self.rect.bottom 
        self.rect.left = 0 if self.rect.left < 0 else self.rect.left


    def __str__(self):
        return f"location: {self.coordinates}"