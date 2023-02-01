import pygame

class GameObject(pygame.sprite.Sprite):

    coordinates = (-1, -1)

    def __init__(self, coordinates, size, group):
        super(GameObject, self).__init__(group)
        self.coordinates = coordinates
        self.image = pygame.Surface([size, size])
        self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], size, size)

    def update(self):
        return