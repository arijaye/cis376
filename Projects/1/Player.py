from GameObject import GameObject
import pygame
import os
import Notif


class Player(GameObject):
     
    imagePath = os.path.join('Projects', '1', 'images', 'purple-glass-sphere-ball-download-png-11650715978ympcumd4es.png')

    def __init__(self, position, size, group):
        super().__init__(position, size, group)
        self.image = pygame.image.load(self.imagePath).convert_alpha()
        Notif.registerKeyEvent(self.move)
    

    def move(self, key):
        match key:
            case pygame.K_UP:
                self.y += 1
                print(self.y)

            case pygame.K_DOWN:
                self.y -= 1
                print(self.y)

            case pygame.K_LEFT:
                self.x -= 1
                print(self.x)

            case pygame.K_RIGHT:
                self.x += 1
                print(self.x)


    def update(self):
        return


    def __str__(self):
        return f"Location: {self.coordinates}"