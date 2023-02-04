import pygame

class GameObject(pygame.sprite.Sprite):

    coordinates = (-1, -1)

    def __init__(self, coordinates, size, group=None):
        self.coordinates = coordinates

        if group != None:
            super(GameObject, self).__init__(group)
            self.image = pygame.Surface([size[0], size[1]])
            self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], size[0], size[1])
        else:
            super(GameObject, self).__init__()

        