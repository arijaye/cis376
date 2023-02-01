import GameObject
import pygame
import os

class Player(GameObject, pygame.sprite.Sprite):
     
    imagePath = os.path.join("images", "purple-glass-sphere-ball-download-png-11650715978ympcumd4es.png")

    def __init__(self):
        """Initialize the player sprite"""
        super(Player, self).__init__()

        # Load the image, preserve alpha channel for transparency
        self.surf = pygame.image.load(self.imagePath).convert_alpha()

        # Save the rect so you can move it
        self.rect = self.surf.get_rect()

    def __str__(self):
        return f"Location: {self.coordinates}"