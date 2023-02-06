import pygame

""" GameObject class.

Base class for game object in
Maze Generator. Maze, cells, and player
are all GameObjects (pygame.Sprites).

"""
class GameObject(pygame.sprite.Sprite):

    # location of game object
    coordinates = (-1, -1)

    """Initializes GameObject.x
    Args:
        coordinates: GameObject's position on display.
        size: size of game object
        group: sprite group of GameObject; default to none

    Returns:
        a new GameObject
    """
    def __init__(self, coordinates, size, group=None):
        self.coordinates = coordinates

        if group != None:
            super(GameObject, self).__init__(group)
            self.image = pygame.Surface([size[0], size[1]])
            self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], size[0], size[1])
        else:
            super(GameObject, self).__init__()

        