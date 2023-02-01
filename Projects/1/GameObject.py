import pygame

class GameObject(pygame.sprite.Sprite):

    coordinates = (-1, -1)

    def __init__(self, coordinates, group):
        super(GameObject, self).__init__(group)
        self.coordinates = coordinates

    def update(self):
        return