import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, coordinates, size, group):
        super(GameObject, self).__init__(group)
        self.x = coordinates[0]
        self.y = coordinates[0]
        self.image = pygame.Surface([size, size])
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def update(self):
        return