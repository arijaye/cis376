from GameObject import GameObject
import pygame
import os

"""Player object.
Player in Maze Generator/Game.
Checks for collisions with the 
outer edges of the display. 

Attributes:
    direction: A tuple indicating direction of movement (ex. (1,0) => right, (0,-1) => up, etc.).
"""
class Player(GameObject):
    """Initializes Player.x
    Args:
        position: Player's position on display.

    Returns:
        a new Player object
    """
    def __init__(self, position):
        self.imagePath = os.path.join('images', 'sprite.png')
        self.scaleAndSetImage()
        self.direction = (0,0)
        super().__init__(coordinates=position, size=(self.rect.width,self.rect.height))


    """Scales player image.
    Scales player image to fit to cell size.
    """
    def scaleAndSetImage(self):
        self.image = pygame.image.load(self.imagePath).convert_alpha()

        rect = self.image.get_rect()
        (scaledX, scaledY) = (rect.width/30, rect.height/30)

        self.image = pygame.transform.scale(self.image, (scaledX, scaledY))
        self.rect = self.image.get_rect()


    """Update player position.
    Updates the player's position depending on 
    key value. Checks for collisions with board
    boundaries.
    Args:
        key: key pressed by user (direction)
        delta: delta time from game loop
        boardsize: display size for collsion detection
    """
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


    """Checks for boundary collisions
    Updates the players location if they've
    collided with outer boundaries.
    Args:
        boardsize: display size
    """
    def checkForCollisions(self, boardsize):
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.right = boardsize if self.rect.right > boardsize else self.rect.right
        self.rect.bottom = boardsize if self.rect.bottom > boardsize else self.rect.bottom 
        self.rect.left = 0 if self.rect.left < 0 else self.rect.left


    def __str__(self):
        return f"location: {self.coordinates}"